#!/usr/bin/env node
// PRN Logic Engine CLI

import { Command } from 'commander';
import { writeFileSync, mkdirSync, existsSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

import { n24Senggarang } from './data/n24-senggarang.js';
import { n01BulohKasap } from './data/n01-buloh-kasap.js';
import { n02Pemanis } from './data/n02-pemanis.js';
import { n04BukitNaning } from './data/n04-bukit-naning.js';
import { n12Kempas } from './data/n12-kempas.js';
import { n13BukitBatu } from './data/n13-bukit-batu.js';
import { n14PulaiSebatang } from './data/n14-pulai-sebatang.js';
import { n15Kukup } from './data/n15-kukup.js';
import { n16SungaiBalang } from './data/n16-sungai-balang.js';
import { n17Semerah } from './data/n17-semerah.js';
import { n18BukitKepong } from './data/n18-bukit-kepong.js';
import { n19SriMedan } from './data/n19-sri-medan.js';
import { n25JohorLama } from './data/n25-johor-lama.js';
import { n26TanjungSurat } from './data/n26-tanjung-surat.js';
import { n27LayangLayang } from './data/n27-layang-layang.js';
import { n32Endau } from './data/n32-endau.js';
import { n33Tenggaroh } from './data/n33-tenggaroh.js';
import { n35PasirRaja } from './data/n35-pasir-raja.js';
import { n41PuteriWangsa } from './data/n41-puteri-wangsa.js';
import { calculateAllScenarios, DEFAULT_SCENARIOS, N17_SEMERAH_SCENARIOS, N27_LAYANG_LAYANG_SCENARIOS } from './engine/scenario-calculator.js';
import { generateMarkdownBrief, generateJSONOutput } from './output/generator.js';
import { Seat } from './types.js';

const __dirname = dirname(fileURLToPath(import.meta.url));
const VERSION = '0.1.0';

const program = new Command();

program
  .name('prn-logic-engine')
  .description('PRN Johor 2026 - Turnout Scenario Logic Engine')
  .version(VERSION);

program
  .command('calculate')
  .description('Calculate scenarios for a seat')
  .option('-s, --seat <code>', 'Seat code (e.g., N24)', 'N24')
  .option('-o, --output <dir>', 'Output directory', './output')
  .option('--format <type>', 'Output format: markdown,json,both', 'both')
  .option('--scenario <id>', 'Specific scenario (S1-S6) or "all"', 'all')
  .action(async (options) => {
    const seat = getSeat(options.seat);
    
    if (!seat) {
      console.error(`Error: Seat "${options.seat}" not found`);
      console.log('Available seats: N01, N02, N04, N17, N24');
      process.exit(1);
    }
    
    console.log(`Calculating scenarios for ${seat.code} ${seat.name}...`);
    console.log(`Electorate: ${seat.totalElectorate.toLocaleString()}`);
    console.log(`Candidates: ${seat.candidates.bn.name} (BN), ${seat.candidates.ph.name} (PH), ${seat.candidates.pn.name} (PN)`);
    console.log('');
    
    // Use seat-specific scenarios
    let scenarios = DEFAULT_SCENARIOS;
    if (seat.code === 'N17') scenarios = N17_SEMERAH_SCENARIOS;
    else if (seat.code === 'N27') scenarios = N27_LAYANG_LAYANG_SCENARIOS;
    const projections = calculateAllScenarios(seat, scenarios);
    
    // Ensure output directory exists
    const outputDir = join(process.cwd(), options.output);
    if (!existsSync(outputDir)) {
      mkdirSync(outputDir, { recursive: true });
    }
    
    // Generate outputs
    const timestamp = new Date().toISOString().split('T')[0];
    const safeSeatName = `${seat.code.toLowerCase()}-${seat.name.toLowerCase().replace(/\s+/g, '-')}`;
    
    if (options.format === 'markdown' || options.format === 'both') {
      const markdown = generateMarkdownBrief(seat, projections, VERSION);
      const mdPath = join(outputDir, `${safeSeatName}-scenarios-${timestamp}.md`);
      writeFileSync(mdPath, markdown);
      console.log(`✓ Markdown brief: ${mdPath}`);
    }
    
    if (options.format === 'json' || options.format === 'both') {
      const json = generateJSONOutput(seat, projections, VERSION);
      const jsonPath = join(outputDir, `${safeSeatName}-scenarios-${timestamp}.json`);
      writeFileSync(jsonPath, JSON.stringify(json, null, 2));
      console.log(`✓ JSON output: ${jsonPath}`);
    }
    
    console.log('');
    console.log('=== Summary ===');
    console.log('');
    
    // Print scenario table
    console.log('Scenario Matrix:');
    console.log('─────────────────────────────────────────────────────────────────────────────');
    console.log('ID    | Turnout | BN %   | PH %   | PN %   | Winner | Margin');
    console.log('─────────────────────────────────────────────────────────────────────────────');
    
    projections.forEach(p => {
      const marginStr = p.margin >= 0 ? `+${p.margin}` : `${p.margin}`;
      console.log(`${p.scenario.id.padEnd(6)}| ${String(p.scenario.turnout) + '%'.padEnd(8)}| ${String(p.bn.percentage) + '%'.padEnd(7)}| ${String(p.ph.percentage) + '%'.padEnd(7)}| ${String(p.pn.percentage) + '%'.padEnd(7)}| ${p.winner.padEnd(7)}| ${marginStr}`);
    });
    
    console.log('─────────────────────────────────────────────────────────────────────────────');
    
    const baseline = projections.find(p => p.scenario.id === 'S2')!;
    console.log('');
    console.log(`Most Likely: ${baseline.winner} wins by ${baseline.margin.toLocaleString()} votes (${baseline.scenario.turnout}% turnout)`);
    console.log(`Confidence: Moderate-High (60-65%)`);
    console.log('');
  });

program
  .command('list-seats')
  .description('List available seats')
  .action(() => {
    console.log('Available seats:');
    console.log('');
    console.log('📍 Segamat/Muar/Batu Pahat:');
    console.log('  N01 - Buloh Kasap (Segamat)');
    console.log('  N02 - Pemanis (Segamat)');
    console.log('  N04 - Bukit Naning (Muar)');
    console.log('  N16 - Sungai Balang (Muar)');
    console.log('  N17 - Semerah (Batu Pahat) ★ Ground Truth');
    console.log('  N18 - Bukit Kepong (Muar)');
    console.log('  N19 - Sri Medan (Batu Pahat)');
    console.log('  N24 - Senggarang (Batu Pahat)');
    console.log('');
    console.log('📍 Johor Bahru/Pontian/Kulai:');
    console.log('  N12 - Kempas (Johor Bahru)');
    console.log('  N13 - Bukit Batu (Kulai)');
    console.log('  N14 - Pulai Sebatang (Pontian)');
    console.log('  N15 - Kukup (Pontian)');
    console.log('');
    console.log('📍 Mersing/Kluang/Kota Tinggi:');
    console.log('  N25 - Johor Lama (Mersing) ★ NEW');
    console.log('  N26 - Tanjung Surat (Mersing) ★ NEW');
    console.log('  N27 - Layang-Layang (Kluang) ★ Indian Kingmaker');
    console.log('  N32 - Endau (Mersing)');
    console.log('  N33 - Tenggaroh (Mersing) ★ FELDA Belt ★ NEW');
    console.log('  N35 - Pasir Raja (Kota Tinggi)');
    console.log('');
    console.log('📍 Tebrau:');
    console.log('  N41 - Puteri Wangsa (Tebrau) ★ Tier-1 Battleground');
    console.log('');
    console.log('Total: 19 seats processed (37 remaining)');
  });

program
  .command('list-scenarios')
  .description('List available scenarios')
  .action(() => {
    console.log('Available scenarios:');
    console.log('');
    DEFAULT_SCENARIOS.forEach(s => {
      console.log(`${s.id}: ${s.name} (${s.description})`);
      console.log(`   Turnout: ${s.turnout}%`);
      console.log(`   Assumptions:`);
      s.assumptions.forEach(a => console.log(`     - ${a}`));
      console.log('');
    });
  });

program.parse();

function getSeat(code: string): Seat | null {
  const seatMap: Record<string, Seat> = {
    'N01': n01BulohKasap,
    'N02': n02Pemanis,
    'N04': n04BukitNaning,
    'N12': n12Kempas,
    'N13': n13BukitBatu,
    'N14': n14PulaiSebatang,
    'N15': n15Kukup,
    'N16': n16SungaiBalang,
    'N17': n17Semerah,
    'N18': n18BukitKepong,
    'N19': n19SriMedan,
    'N24': n24Senggarang,
    'N25': n25JohorLama,
    'N26': n26TanjungSurat,
    'N27': n27LayangLayang,
    'N32': n32Endau,
    'N33': n33Tenggaroh,
    'N35': n35PasirRaja,
    'N41': n41PuteriWangsa
  };
  
  return seatMap[code.toUpperCase()] || null;
}
