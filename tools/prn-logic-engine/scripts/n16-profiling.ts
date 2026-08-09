/**
 * N16 Sungai Balang - Full DUN Profiling Workflow
 * Corrected Tier Logic (2026-07-01):
 * - Tier 2A: 90%+ Malay (rural heartland)
 * - Tier 2B: 75–90% Malay (mixed rural)
 * - Tier 3: 75–100% Chinese (concentration PDs)
 * - Tier 1: 50–75% Chinese (kingmaker/mixed urban)
 */

import { n16SungaiBalang } from '../src/data/n16-sungai-balang';

// Corrected tier classification
function classifyTier(malayPct: number, chinesePct: number): string {
  if (chinesePct >= 75) return 'Tier 3 (Chinese Concentration)';
  if (chinesePct >= 50) return 'Tier 1 (Kingmaker/Chinese Base)';
  if (malayPct >= 90) return 'Tier 2A (Malay Heartland)';
  if (malayPct >= 75) return 'Tier 2B (Mixed Rural)';
  return 'Tier 2B (Mixed)';
}

console.log('═══════════════════════════════════════════════════════════');
console.log('  N16 SUNGAI BALANG — DUN PROFILING V1 (CORRECTED LOGIC)');
console.log('═══════════════════════════════════════════════════════════\n');

console.log('📊 SEAT SNAPSHOT');
console.log('───────────────────────────────────────────────────────────');
console.log(`Federal Constituency: ${n16SungaiBalang.federalCode} ${n16SungaiBalang.federalName}`);
console.log(`Total Electorate: ${n16SungaiBalang.totalElectorate.toLocaleString()}`);

// Calculate aggregate demographics
let totalMalay = 0, totalChinese = 0, totalIndian = 0, totalOthers = 0;
n16SungaiBalang.pollingDistricts.forEach(pd => {
  totalMalay += pd.demographics.malay;
  totalChinese += pd.demographics.chinese;
  totalIndian += pd.demographics.indian;
  totalOthers += pd.demographics.others;
});

const malayPct = (totalMalay / n16SungaiBalang.totalElectorate * 100).toFixed(2);
const chinesePct = (totalChinese / n16SungaiBalang.totalElectorate * 100).toFixed(2);
const indianPct = (totalIndian / n16SungaiBalang.totalElectorate * 100).toFixed(2);
const othersPct = (totalOthers / n16SungaiBalang.totalElectorate * 100).toFixed(2);

console.log(`\nDemographics:`);
console.log(`  Malay: ${totalMalay.toLocaleString()} (${malayPct}%)`);
console.log(`  Chinese: ${totalChinese.toLocaleString()} (${chinesePct}%)`);
console.log(`  Indian: ${totalIndian.toLocaleString()} (${indianPct}%)`);
console.log(`  Others: ${totalOthers.toLocaleString()} (${othersPct}%)`);

// Tier classification with corrected logic
console.log('\n📋 POLLING DISTRICT TIER CLASSIFICATION (CORRECTED)');
console.log('───────────────────────────────────────────────────────────');
console.log('PD Name'.padEnd(35) + 'Electorate'.padEnd(12) + 'Malay %'.padEnd(10) + 'Chinese %'.padEnd(12) + 'Tier');
console.log('───────────────────────────────────────────────────────────');

const tierCounts: Record<string, number> = {};
n16SungaiBalang.pollingDistricts.forEach(pd => {
  const tier = classifyTier(pd.demographics.malayPct, pd.demographics.chinesePct);
  tierCounts[tier] = (tierCounts[tier] || 0) + 1;
  
  console.log(
    pd.name.padEnd(35) +
    pd.electorate.toString().padEnd(12) +
    pd.demographics.malayPct.toFixed(2).padEnd(10) +
    pd.demographics.chinesePct.toFixed(2).padEnd(12) +
    tier
  );
});

console.log('\n📊 TIER SUMMARY');
console.log('───────────────────────────────────────────────────────────');
Object.entries(tierCounts).forEach(([tier, count]) => {
  console.log(`${tier}: ${count} PDs`);
});

// Calculate youth estimate (assuming ~26% based on similar Muar seats)
const youthEstimate = Math.round(n16SungaiBalang.totalElectorate * 0.26);
console.log(`\nYouth (18–29): ~${youthEstimate.toLocaleString()} (26.0%)`);

console.log('\n═══════════════════════════════════════════════════════════');
console.log('  CORRECTED LOGIC APPLIED ✅');
console.log('═══════════════════════════════════════════════════════════');
