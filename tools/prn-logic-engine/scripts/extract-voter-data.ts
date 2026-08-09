#!/usr/bin/env tsx
/**
 * Extract voter roll data from Excel files
 * Usage: tsx scripts/extract-voter-data.ts <path-to-xlsx>
 */

import ExcelJS from 'exceljs';
import * as fs from 'fs';
import * as path from 'path';

async function extractVoterData(filePath: string) {
  const workbook = new ExcelJS.Workbook();
  await workbook.xlsx.readFile(filePath);
  
  console.log(`\n=== ${path.basename(filePath)} ===`);
  console.log(`Worksheets: ${workbook.worksheets.map(w => w.name).join(', ')}`);
  
  const worksheet = workbook.worksheets[0];
  
  // Read header row
  const headers: string[] = [];
  worksheet.getRow(1).eachCell(cell => {
    headers.push(cell.value?.toString() || '');
  });
  
  console.log('\nHeaders:', headers.join(' | '));
  
  // Read data rows
  const data: any[] = [];
  worksheet.eachRow((row, rowNumber) => {
    if (rowNumber === 1) return; // Skip header
    
    const rowData: any = {};
    headers.forEach((header, index) => {
      rowData[header] = row.getCell(index + 1).value;
    });
    data.push(rowData);
  });
  
  console.log(`\nTotal rows: ${data.length}`);
  
  // Show first 3 rows as sample
  console.log('\nSample data (first 3 rows):');
  data.slice(0, 3).forEach((row, i) => {
    console.log(`Row ${i + 1}:`, JSON.stringify(row, null, 2));
  });
  
  return data;
}

// Main
const filePath = process.argv[2];
if (!filePath) {
  console.error('Usage: tsx scripts/extract-voter-data.ts <path-to-xlsx>');
  process.exit(1);
}

extractVoterData(filePath).catch(console.error);
