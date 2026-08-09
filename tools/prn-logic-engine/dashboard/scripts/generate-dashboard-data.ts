#!/usr/bin/env tsx
/**
 * Generate dashboard JSON data from coalition daily reports
 * Reads markdown reports and converts to structured JSON for the React dashboard
 */

import { readFileSync, writeFileSync, readdirSync } from 'fs'
import { join } from 'path'

const REPORTS_DIR = join(process.cwd(), '..', 'coalition-analysis')
const OUTPUT_FILE = join(process.cwd(), 'src', 'data', 'dashboard-data.json')

interface Candidate {
  name: string
  seat: string
  party: string
  activityLevel: 'high' | 'medium' | 'low'
  keyEvent: string
}

interface SeatStatus {
  seat: string
  candidate: string
  status: 'safe' | 'contested' | 'vulnerable'
  threatLevel: 'low' | 'medium' | 'high'
  notes: string
}

interface CoalitionMetrics {
  ceramahsHeld: number
  ceramahsTarget: number
  voterContacts: number
  voterContactsTarget: number
  socialMediaReach: number
  socialMediaTarget: number
  volunteerDeployment: number
  volunteerTarget: number
}

interface CoalitionData {
  name: string
  candidates: Candidate[]
  seats: SeatStatus[]
  metrics: CoalitionMetrics
  developments: string[]
}

function parseMarkdownReport(content: string, coalition: string): CoalitionData {
  const lines = content.split('\n')
  
  // Extract developments
  const developments: string[] = []
  let inDevelopments = false
  for (let i = 0; i < lines.length; i++) {
    if (lines[i].includes('**Top 3') || lines[i].includes('Top 3')) {
      inDevelopments = true
      continue
    }
    if (inDevelopments) {
      if (lines[i].startsWith('1. **') || lines[i].startsWith('2. **') || lines[i].startsWith('3. **')) {
        const text = lines[i].replace(/^\d\. \*\*/, '').replace(/\*\*$/, '')
        developments.push(text)
      }
      if (lines[i].includes('Key Rally') || lines[i].includes('## Candidate')) {
        inDevelopments = false
      }
    }
  }

  // Extract candidates from heatmap table
  const candidates: Candidate[] = []
  let inCandidateTable = false
  for (let i = 0; i < lines.length; i++) {
    if (lines[i].includes('Candidate') && lines[i].includes('Activity Level')) {
      inCandidateTable = true
      continue
    }
    if (inCandidateTable) {
      if (lines[i].startsWith('|') && lines[i].includes('|')) {
        const parts = lines[i].split('|').map(p => p.trim()).filter(p => p)
        if (parts.length >= 5 && !parts[0].includes('---')) {
          const [name, seat, party, activity, event] = parts
          if (name && !name.includes('Name')) {
            candidates.push({
              name: name.replace(/^\d+\s*/, ''),
              seat,
              party,
              activityLevel: activity.includes('🔴') ? 'high' : activity.includes('🟡') ? 'medium' : 'low',
              keyEvent: event
            })
          }
        }
      }
      if (lines[i].includes('Activity Level Legend') || lines[i].includes('## Seat')) {
        inCandidateTable = false
      }
    }
  }

  // Extract seats from status tables
  const seats: SeatStatus[] = []
  const statusSections = ['Strongholds', 'Battlegrounds', 'Challenges']
  for (let i = 0; i < lines.length; i++) {
    for (const section of statusSections) {
      if (lines[i].includes(section)) {
        let j = i + 2 // Skip header
        while (j < lines.length && lines[j].startsWith('|') && !lines[j].includes('---')) {
          const parts = lines[j].split('|').map(p => p.trim()).filter(p => p)
          if (parts.length >= 4) {
            const [seat, candidate, status] = parts
            if (seat && !seat.includes('Seat')) {
              seats.push({
                seat,
                candidate: candidate.replace(/\?.*/, 'TBD'),
                status: section.includes('Stronghold') ? 'safe' : section.includes('Battleground') ? 'contested' : 'vulnerable',
                threatLevel: section.includes('Stronghold') ? 'low' : section.includes('Battleground') ? 'medium' : 'high',
                notes: parts[parts.length - 1] || ''
              })
            }
          }
          j++
        }
        break
      }
    }
  }

  // Extract metrics
  const metrics: CoalitionMetrics = {
    ceramahsHeld: extractMetric(content, 'Ceramahs Held'),
    ceramahsTarget: extractMetric(content, 'Ceramahs Held', true),
    voterContacts: extractMetric(content, 'Voter Contacts'),
    voterContactsTarget: extractMetric(content, 'Voter Contacts', true),
    socialMediaReach: extractMetric(content, 'Social Media Reach'),
    socialMediaTarget: extractMetric(content, 'Social Media Reach', true),
    volunteerDeployment: extractMetric(content, 'Volunteer Deployment'),
    volunteerTarget: extractMetric(content, 'Volunteer Deployment', true)
  }

  return {
    name: coalition.toUpperCase(),
    candidates: candidates.slice(0, 5),
    seats: seats.slice(0, 3),
    metrics,
    developments: developments.slice(0, 3)
  }
}

function extractMetric(content: string, metricName: string, isTarget = false): number {
  const lines = content.split('\n')
  for (let i = 0; i < lines.length; i++) {
    if (lines[i].includes(metricName)) {
      const parts = lines[i].split('|').map(p => p.trim())
      if (parts.length >= 3) {
        const value = isTarget ? parts[2] : parts[1]
        const num = parseInt(value.replace(/,/g, '').replace(/K$/, '000'))
        return isNaN(num) ? 0 : num
      }
    }
  }
  return 0
}

function main() {
  console.log('🔍 Scanning coalition reports...')
  
  const coalitions = ['pn', 'bn', 'ph', 'independent']
  const dashboardData: Record<string, CoalitionData> = {}
  
  for (const coalition of coalitions) {
    const files = readdirSync(REPORTS_DIR)
      .filter(f => f.includes(`${coalition}-daily-`) && f.endsWith('.md'))
      .sort()
      .reverse()
    
    if (files.length > 0) {
      const latestFile = files[0]
      console.log(`📊 Processing ${coalition}: ${latestFile}`)
      
      const content = readFileSync(join(REPORTS_DIR, latestFile), 'utf-8')
      dashboardData[coalition] = parseMarkdownReport(content, coalition)
    } else {
      console.warn(`⚠️  No reports found for ${coalition}`)
    }
  }
  
  // Ensure output directory exists
  const outputDir = join(process.cwd(), 'src', 'data')
  if (!dashboardData.pn) {
    console.log('⚠️  No data found, using mock data')
    process.exit(0)
  }
  
  // Write JSON
  writeFileSync(OUTPUT_FILE, JSON.stringify(dashboardData, null, 2))
  console.log(`✅ Dashboard data generated: ${OUTPUT_FILE}`)
  console.log(`📊 Coalitions processed: ${Object.keys(dashboardData).length}`)
  console.log(`📈 Total candidates: ${Object.values(dashboardData).reduce((sum, c) => sum + c.candidates.length, 0)}`)
}

main()
