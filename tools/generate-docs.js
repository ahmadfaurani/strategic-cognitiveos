#!/usr/bin/env node

import { OpenAI } from 'openai';
import { readdir, readFile, stat } from 'fs/promises';
import { join, relative } from 'path';

const API_KEY = process.env.OPENAI_API_KEY;
const BASE_URL = 'https://model.arasintegrasi.ai/v1';
const MODEL = 'Qwen/Qwen3.5-397B-A17B';

const client = new OpenAI({
  apiKey: API_KEY,
  baseURL: BASE_URL,
});

async function scanDirectory(dir, maxFiles = 50) {
  const files = [];
  
  async function walk(currentPath) {
    if (files.length >= maxFiles) return;
    
    const entries = await readdir(currentPath, { withFileTypes: true });
    for (const entry of entries) {
      if (files.length >= maxFiles) break;
      if (entry.name.startsWith('.') || entry.name === 'node_modules') continue;
      
      const fullPath = join(currentPath, entry.name);
      if (entry.isDirectory()) {
        await walk(fullPath);
      } else if (entry.isFile()) {
        const ext = entry.name.split('.').pop().toLowerCase();
        if (['js', 'ts', 'md', 'json', 'yaml', 'yml', 'py', 'sh'].includes(ext)) {
          const s = await stat(fullPath);
          if (s.size < 50000) { // Skip large files
            files.push(fullPath);
          }
        }
      }
    }
  }
  
  await walk(dir);
  return files;
}

async function main() {
  console.log('📄 Scanning workspace...');
  const workspaceDir = process.cwd();
  const files = await scanDirectory(workspaceDir, 30);
  
  console.log(`Found ${files.length} files to analyze\n`);
  
  const fileContents = [];
  for (const file of files) {
    try {
      const content = await readFile(file, 'utf-8');
      const relPath = relative(workspaceDir, file);
      fileContents.push(`\n\n---\nFile: ${relPath}\n---\n${content.slice(0, 3000)}`);
    } catch (e) {
      // Skip binary or unreadable files
    }
  }
  
  const prompt = `You are a documentation generator. Based on the following files from a workspace, generate a comprehensive README.md that explains:
1. What this project/workspace is about
2. Key features and capabilities
3. Directory structure overview
4. How to get started
5. Configuration and usage

Here are the files (truncated for brevity):
${fileContents.join('\n')}

Generate a well-structured README.md in Markdown format.`;

  console.log('🤖 Generating documentation...\n');
  
  const response = await client.chat.completions.create({
    model: MODEL,
    messages: [
      { role: 'user', content: prompt }
    ],
    temperature: 0.7,
    max_tokens: 4000,
  });
  
  console.log('✅ Documentation generated:\n');
  console.log('='.repeat(60));
  console.log(response.choices[0].message.content);
  console.log('='.repeat(60));
}

main().catch(console.error);
