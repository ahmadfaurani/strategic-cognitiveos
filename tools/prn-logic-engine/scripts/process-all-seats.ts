#!/usr/bin/env tsx
/**
 * Process all three voter roll Excel files and generate seat data
 */

import ExcelJS from 'exceljs';
import * as fs from 'fs';

interface PollingDistrict {
  code: string;
  name: string;
  electorate: number;
  malay: number;
  chinese: number;
  indian: number;
  others: number;
  turnout2022?: number;
  tier: 1 | 2 | 3;
}

async function extractSeatData(filePath: string): Promise<{ seatName: string; parliament: string; totalElectorate: number; pollingDistricts: PollingDistrict[] }> {
  const workbook = new ExcelJS.Workbook();
  await workbook.xlsx.readFile(filePath);
  
  const worksheet = workbook.worksheets[0];
  const headers: string[] = [];
  worksheet.getRow(1).eachCell(cell => {
    headers.push(cell.value?.toString() || '');
  });
  
  const data: any[] = [];
  worksheet.eachRow((row, rowNumber) => {
    if (rowNumber === 1) return;
    const rowData: any = {};
    headers.forEach((header, index) => {
      rowData[header] = row.getCell(index + 1).value;
    });
    data.push(rowData);
  });
  
  let seatName = '';
  let parliament = '';
  let totalElectorate = 0;
  const pollingDistricts: PollingDistrict[] = [];
  
  data.forEach(row => {
    if (!seatName) {
      seatName = row['DUN']?.toString().trim() || '';
      parliament = row['PARLIMEN']?.toString().trim() || '';
    }
    
    totalElectorate += row['PEMILIH BERDAFTAR'] || 0;
    
    const malay = row['MELAYU'] || 0;
    const chinese = row['CINA'] || 0;
    const indian = row['INDIA'] || 0;
    const others = (row['BUMIPUTERA SABAH'] || 0) + 
                   (row['BUMIPUTERA SARAWAK'] || 0) + 
                   (row['ORANG ASLI'] || 0) + 
                   (row['LAIN-LAIN'] || 0);
    
    const total = malay + chinese + indian + others;
    const malayPct = total > 0 ? Math.round((malay / total) * 100) : 0;
    const chinesePct = total > 0 ? Math.round((chinese / total) * 100) : 0;
    const indianPct = total > 0 ? Math.round((indian / total) * 100) : 0;
    const othersPct = Math.max(0, 100 - malayPct - chinesePct - indianPct);
    
    // Determine tier based on demographics
    let tier: 1 | 2 | 3 = 2;
    if (malayPct >= 75 || chinesePct >= 75) tier = 3;
    else if (malayPct >= 50 || chinesePct >= 50) tier = 1;
    
    pollingDistricts.push({
      code: row['KOD DM']?.toString().split('/')[2] || '',
      name: row['DAERAH MENGUNDI']?.toString().trim() || '',
      electorate: row['PEMILIH BERDAFTAR'] || 0,
      malay: malayPct,
      chinese: chinesePct,
      indian: indianPct,
      others: othersPct,
      tier
    });
  });
  
  return { seatName, parliament, totalElectorate, pollingDistricts };
}

async function main() {
  const files = [
    '/home/p62operator/.openclaw/media/inbound/1_BULOH_KASAP_as_of_190626---174593bf-f325-4ee3-ad5f-5e9f3e6378d5.xlsx',
    '/home/p62operator/.openclaw/media/inbound/2_PEMANIS_as_of_190626---34d9d611-362e-4962-b300-d4f245f8fd69.xlsx',
    '/home/p62operator/.openclaw/media/inbound/4_BUKIT_NANING_as_of_190626---8cd33f15-c1df-402c-b45c-f7e3f09d60a3.xlsx'
  ];
  
  for (const file of files) {
    console.log(`\nProcessing ${file.split('/').pop()}...`);
    const result = await extractSeatData(file);
    
    console.log(`Seat: ${result.seatName}`);
    console.log(`Parliament: ${result.parliament}`);
    console.log(`Total Electorate: ${result.totalElectorate}`);
    console.log(`Polling Districts: ${result.pollingDistricts.length}`);
    
    // Calculate demographics
    const totalMalay = result.pollingDistricts.reduce((sum, pd) => {
      return sum + Math.round(pd.electorate * pd.malay / 100);
    }, 0);
    const totalChinese = result.pollingDistricts.reduce((sum, pd) => {
      return sum + Math.round(pd.electorate * pd.chinese / 100);
    }, 0);
    const totalIndian = result.pollingDistricts.reduce((sum, pd) => {
      return sum + Math.round(pd.electorate * pd.indian / 100);
    }, 0);
    
    const malayPct = ((totalMalay / result.totalElectorate) * 100).toFixed(1);
    const chinesePct = ((totalChinese / result.totalElectorate) * 100).toFixed(1);
    const indianPct = ((totalIndian / result.totalElectorate) * 100).toFixed(1);
    
    console.log(`Demographics: Malay ${malayPct}%, Chinese ${chinesePct}%, Indian ${indianPct}%`);
    console.log('---');
  }
}

main().catch(console.error);
