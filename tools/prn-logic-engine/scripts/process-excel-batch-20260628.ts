#!/usr/bin/env ts-node
/**
 * Process Excel Intelligence Batch - 2026-06-28
 * 
 * Processes 10 DUN intelligence Excel files:
 * 1. N01 Buloh Kasap (already processed)
 * 2. N02 Pemanis (already processed)
 * 3. N04 Bukit Naning (already processed)
 * 4. N16 Sungai Balang (NEW)
 * 5. N17 Semerah (already processed)
 * 6. N24 Senggarang (already processed)
 * 7. N27 Layang-Layang (already processed)
 * 8. N32 Endau (NEW)
 * 9. N35 Pasir Raja (NEW)
 * 10. N41 Puteri Wangsa (NEW - Tier-1 battleground)
 * 
 * Usage: npm run ts-node scripts/process-excel-batch-20260628.ts
 */

import * as fs from 'fs';
import * as path from 'path';

const EXCEL_DIR = '/home/p62operator/.openclaw/media/inbound';
const OUTPUT_DIR = '/home/p62operator/.openclaw/workspace/tools/prn-logic-engine/src/data';

interface ExcelFile {
  filename: string;
  seatCode: string;
  seatName: string;
  status: 'processed' | 'new';
}

const excelFiles: ExcelFile[] = [
  { filename: '1_BULOH_KASAP_as_of_190626---53f174d9-a98c-4fdb-808c-0d66778759af.xlsx', seatCode: 'N01', seatName: 'Buloh Kasap', status: 'processed' },
  { filename: '2_PEMANIS_as_of_190626---9e88fed1-c787-4758-8b94-0972004ebee8.xlsx', seatCode: 'N02', seatName: 'Pemanis', status: 'processed' },
  { filename: '4_BUKIT_NANING_as_of_190626---5e2e6345-711c-4cb1-8ff9-3515485afecc.xlsx', seatCode: 'N04', seatName: 'Bukit Naning', status: 'processed' },
  { filename: '5_SUNGAI_BALANG_as_of_190626---190553de-daf5-47ee-8f7a-471bdb1a9dd1.xlsx', seatCode: 'N16', seatName: 'Sungai Balang', status: 'new' },
  { filename: '6_SEMERAH_as_of_190626---e85f3d61-baa9-44c8-abab-1a2817c225f7.xlsx', seatCode: 'N17', seatName: 'Semerah', status: 'processed' },
  { filename: '7_SENGGARANG_as_of_190626---6595ab4d-bc65-41ad-8420-7082aa54cd90.xlsx', seatCode: 'N24', seatName: 'Senggarang', status: 'processed' },
  { filename: '8_LAYANG_LAYANG_as_of_190626---35b015ba-14b8-471a-8a73-2cefe33f399f.xlsx', seatCode: 'N27', seatName: 'Layang-Layang', status: 'processed' },
  { filename: '9_ENDAU_as_of_190626---ecda7b55-9bab-42ae-829b-fd2b508f67d5.xlsx', seatCode: 'N32', seatName: 'Endau', status: 'new' },
  { filename: '10_PASIR_RAJA_as_of_190626---2315db07-00df-4a4e-9473-837099ea6b3c.xlsx', seatCode: 'N35', seatName: 'Pasir Raja', status: 'new' },
  { filename: '11_PUTERI_WANGSA_as_of_190626---960f7a4d-cf0d-4cd4-9e9d-dfe29db6a9e4.xlsx', seatCode: 'N41', seatName: 'Puteri Wangsa', status: 'new' },
];

console.log('📊 DUN Intelligence Excel Batch Processing');
console.log('==========================================\n');

console.log('Files to process:');
excelFiles.forEach((file, idx) => {
  const statusIcon = file.status === 'processed' ? '✅' : '🆕';
  console.log(`${idx + 1}. ${statusIcon} ${file.seatCode} ${file.seatName}`);
  const filePath = path.join(EXCEL_DIR, file.filename);
  const exists = fs.existsSync(filePath);
  console.log(`   File: ${file.filename}`);
  console.log(`   Exists: ${exists ? '✓' : '✗ MISSING'}`);
  console.log(`   Status: ${file.status.toUpperCase()}`);
  console.log('');
});

console.log('\n📝 Next Steps:');
console.log('- N16 Sungai Balang: Create data file + scenarios');
console.log('- N32 Endau: Create data file + scenarios');
console.log('- N35 Pasir Raja: Create data file + scenarios');
console.log('- N41 Puteri Wangsa: Create data file + scenarios (TIER-1 BATTLEGROUND)');
console.log('\nRun: npm run dev -- calculate --seat N16 (etc.) after creating data files');
