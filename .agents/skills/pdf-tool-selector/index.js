#!/usr/bin/env node

/**
 * PDF Tool Selector
 * 
 * Intelligently selects between PyMuPDF, pdfplumber, and Apache Tika
 * based on document characteristics and use case requirements.
 */

/**
 * @typedef {Object} DocumentCharacteristics
 * @property {boolean} isScanned - Document is image-based (requires OCR)
 * @property {boolean} hasTables - Document contains tabular data
 * @property {string} format - Document format (pdf, docx, pptx, etc.)
 * @property {string} volume - Processing volume (low, medium, high)
 * @property {boolean} needsMetadata - Need comprehensive metadata extraction
 * @property {boolean} needsLayoutCoordinates - Need precise text positions
 * @property {boolean} enterpriseJava - Running in Java environment
 * @property {string} language - Document language
 */

/**
 * @typedef {Object} ToolRecommendation
 * @property {string} tool - Recommended tool name
 * @property {number} confidence - Confidence score (0-1)
 * @property {string} reasoning - Explanation for recommendation
 * @property {Array} alternatives - Alternative tools with trade-offs
 * @property {string} installCommand - Installation command
 * @property {string} codeExample - Usage example
 */

const TOOLS = {
  PYMUPDF: {
    name: 'PyMuPDF',
    formats: ['pdf'],
    strengths: ['speed', 'low-memory', 'text-extraction', 'image-extraction'],
    weaknesses: ['no-ocr', 'basic-tables', 'pdf-only'],
    install: {
      pip: 'pip install PyMuPDF',
      npm: 'npm install pymupdf'
    }
  },
  PDFPLUMBER: {
    name: 'pdfplumber',
    formats: ['pdf'],
    strengths: ['tables', 'layout-coordinates', 'structured-data', 'forms'],
    weaknesses: ['slower', 'higher-memory', 'no-ocr', 'pdf-only'],
    install: {
      pip: 'pip install pdfplumber'
    }
  },
  TIKAS: {
    name: 'Apache Tika',
    formats: ['pdf', 'docx', 'pptx', 'xls', 'xlsx', 'txt', 'rtf', 'odt', 'html', 'epub', 'many-more'],
    strengths: ['multi-format', 'metadata', 'ocr-via-tesseract', 'enterprise'],
    weaknesses: ['slow', 'high-memory', 'java-required', 'lower-layout-fidelity'],
    install: {
      pip: 'pip install tika',
      docker: 'docker pull apache/tika',
      java: 'Requires Java 8+'
    }
  }
};

/**
 * Calculate confidence score for a tool given document characteristics
 * @param {string} toolKey - Tool identifier
 * @param {DocumentCharacteristics} doc - Document characteristics
 * @returns {number} Confidence score 0-1
 */
function calculateConfidence(toolKey, doc) {
  let score = 0.5; // Base score
  
  const tool = TOOLS[toolKey];
  
  // Format compatibility (critical)
  if (!tool.formats.includes(doc.format) && doc.format !== 'pdf') {
    if (toolKey === 'TIKAS') {
      score += 0.4; // Tika supports most formats
    } else {
      return 0.0; // PyMuPDF/pdfplumber only support PDF
    }
  }
  
  // Table extraction
  if (doc.hasTables) {
    if (toolKey === 'PDFPLUMBER') score += 0.35;
    else if (toolKey === 'PYMUPDF') score -= 0.15;
    else if (toolKey === 'TIKAS') score -= 0.10;
  }
  
  // Scanned documents (OCR needed) - critical factor
  if (doc.isScanned) {
    if (toolKey === 'TIKAS') score += 0.40; // Tika + Tesseract is only viable option
    else {
      score -= 0.50; // PyMuPDF/pdfplumber can't handle scans at all
    }
  }
  
  // Volume/performance
  if (doc.volume === 'high') {
    if (toolKey === 'PYMUPDF') score += 0.20;
    else if (toolKey === 'PDFPLUMBER') score -= 0.10;
    else if (toolKey === 'TIKAS') score -= 0.25;
  } else if (doc.volume === 'low') {
    // Performance less critical
    if (toolKey === 'TIKAS') score += 0.05;
  }
  
  // Layout coordinates
  if (doc.needsLayoutCoordinates) {
    if (toolKey === 'PDFPLUMBER') score += 0.30;
    else if (toolKey === 'PYMUPDF') score += 0.10;
    else if (toolKey === 'TIKAS') score -= 0.15;
  }
  
  // Metadata extraction
  if (doc.needsMetadata) {
    if (toolKey === 'TIKAS') score += 0.20;
    else if (toolKey === 'PYMUPDF' || toolKey === 'PDFPLUMBER') score += 0.05;
  }
  
  // Enterprise Java environment - strong preference for Tika
  if (doc.enterpriseJava) {
    if (toolKey === 'TIKAS') {
      score += 0.35; // Native Java integration, strongest boost
    } else {
      score -= 0.10; // Non-Java tools less ideal but still usable
    }
  }
  
  // Normalize to 0-1 range
  return Math.max(0, Math.min(1, score));
}

/**
 * Select the optimal PDF tool based on document characteristics
 * @param {DocumentCharacteristics} doc - Document characteristics
 * @returns {ToolRecommendation} Recommendation with confidence and reasoning
 */
function selectPdfTool(doc) {
  // Normalize input
  const characteristics = {
    isScanned: doc.isScanned || false,
    hasTables: doc.hasTables || false,
    format: (doc.format || 'pdf').toLowerCase(),
    volume: (doc.volume || 'medium').toLowerCase(),
    needsMetadata: doc.needsMetadata || false,
    needsLayoutCoordinates: doc.needsLayoutCoordinates || false,
    enterpriseJava: doc.enterpriseJava || false,
    language: doc.language || 'en'
  };
  
  // Calculate confidence for each tool
  const scores = {
    PYMUPDF: calculateConfidence('PYMUPDF', characteristics),
    PDFPLUMBER: calculateConfidence('PDFPLUMBER', characteristics),
    TIKAS: calculateConfidence('TIKAS', characteristics)
  };
  
  // Find best tool (start with first valid tool, not hardcoded PYMUPDF)
  let bestTool = null;
  let bestScore = -1;
  
  for (const [tool, score] of Object.entries(scores)) {
    if (score > bestScore) {
      bestScore = score;
      bestTool = tool;
    }
  }
  
  // Fallback to PyMuPDF only if all scores are equal (shouldn't happen)
  if (bestTool === null) {
    bestTool = 'PYMUPDF';
    bestScore = scores.PYMUPDF;
  }
  
  // Generate reasoning
  const reasoning = generateReasoning(bestTool, characteristics, scores);
  
  // Generate alternatives
  const alternatives = generateAlternatives(bestTool, characteristics, scores);
  
  // Get install command
  const installCommand = getInstallCommand(bestTool);
  
  // Get code example
  const codeExample = getCodeExample(bestTool);
  
  return {
    tool: TOOLS[bestTool].name,
    confidence: Math.round(bestScore * 100) / 100,
    reasoning,
    alternatives,
    installCommand,
    codeExample
  };
}

/**
 * Generate human-readable reasoning for the recommendation
 */
function generateReasoning(bestTool, doc, scores) {
  const reasons = [];
  
  if (doc.format !== 'pdf') {
    reasons.push(`Only Apache Tika supports ${doc.format} format`);
  } else if (doc.isScanned) {
    reasons.push('Document is scanned; OCR capability required');
  } else if (doc.hasTables) {
    reasons.push('Document contains tables requiring precise extraction');
  }
  
  if (doc.volume === 'high' && bestTool === 'PYMUPDF') {
    reasons.push('High volume favors PyMuPDF for performance');
  }
  
  if (doc.needsLayoutCoordinates && bestTool === 'PDFPLUMBER') {
    reasons.push('Layout coordinate precision is critical');
  }
  
  if (doc.enterpriseJava && bestTool === 'TIKAS') {
    reasons.push('Enterprise Java environment favors Tika integration');
  }
  
  return reasons.length > 0 ? reasons.join('. ') : 'Default recommendation for clean native PDFs';
}

/**
 * Generate alternative recommendations with trade-offs
 */
function generateAlternatives(bestTool, doc, scores) {
  const alternatives = [];
  
  for (const [toolKey, score] of Object.entries(scores)) {
    if (TOOLS[toolKey].name === TOOLS[bestTool].name) continue;
    
    let tradeoff = '';
    if (toolKey === 'PYMUPDF') {
      tradeoff = doc.hasTables ? 'Faster but poor table support' : 'Good default for simple PDFs';
    } else if (toolKey === 'PDFPLUMBER') {
      tradeoff = doc.volume === 'high' ? 'Better tables but slower for bulk' : 'Best for structured data';
    } else if (toolKey === 'TIKAS') {
      tradeoff = doc.format === 'pdf' ? 'Multi-format but overkill for PDF-only' : 'Only option for this format';
    }
    
    alternatives.push({
      tool: TOOLS[toolKey].name,
      confidence: Math.round(score * 100) / 100,
      tradeoff
    });
  }
  
  return alternatives.sort((a, b) => b.confidence - a.confidence);
}

/**
 * Get installation command for the recommended tool
 */
function getInstallCommand(toolKey) {
  const tool = TOOLS[toolKey];
  return tool.install.pip || tool.install.npm || tool.install.docker || 'See documentation';
}

/**
 * Get code example for the recommended tool
 */
function getCodeExample(toolKey) {
  const examples = {
    PYMUPDF: `import fitz  # PyMuPDF

doc = fitz.open("document.pdf")
for page in doc:
    text = page.get_text()
    images = page.get_images()`,
    
    PDFPLUMBER: `import pdfplumber

with pdfplumber.open("report.pdf") as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()
        cells = page.chars  # Character positions`,
    
    TIKAS: `from tika import parser

raw = parser.from_file("document.pdf")
text = raw["content"]
metadata = raw["metadata"]`
  };
  
  return examples[toolKey] || 'See documentation';
}

/**
 * Run test scenarios to validate decision matrix
 */
function runTests() {
  const scenarios = [
    {
      name: 'Financial Reports with Tables',
      input: { isScanned: false, hasTables: true, format: 'pdf', volume: 'medium', needsLayoutCoordinates: true },
      expected: 'pdfplumber'
    },
    {
      name: 'High-Volume Native PDFs',
      input: { isScanned: false, hasTables: false, format: 'pdf', volume: 'high' },
      expected: 'PyMuPDF'
    },
    {
      name: 'Multi-Format Document Archive',
      input: { isScanned: false, hasTables: false, format: 'docx', volume: 'medium' },
      expected: 'Apache Tika'
    },
    {
      name: 'Scanned PDFs with OCR',
      input: { isScanned: true, hasTables: false, format: 'pdf', volume: 'low' },
      expected: 'Apache Tika'
    },
    {
      name: 'Research Paper RAG Pipeline',
      input: { isScanned: false, hasTables: false, format: 'pdf', volume: 'high', needsMetadata: true },
      expected: 'PyMuPDF'
    },
    {
      name: 'Invoice Processing (Mixed)',
      input: { isScanned: false, hasTables: true, format: 'pdf', volume: 'medium', needsLayoutCoordinates: true },
      expected: 'pdfplumber'
    },
    {
      name: 'Enterprise Java Environment',
      input: { isScanned: false, hasTables: false, format: 'pdf', volume: 'medium', enterpriseJava: true },
      expected: 'Apache Tika'
    }
  ];
  
  console.log('Running PDF Tool Selector Tests\n');
  console.log('=' .repeat(60));
  
  let passed = 0;
  let failed = 0;
  
  for (const scenario of scenarios) {
    const result = selectPdfTool(scenario.input);
    const success = result.tool === scenario.expected;
    
    console.log(`\nTest: ${scenario.name}`);
    console.log(`  Input: ${JSON.stringify(scenario.input)}`);
    console.log(`  Expected: ${scenario.expected}`);
    console.log(`  Got: ${result.tool} (confidence: ${result.confidence})`);
    console.log(`  Status: ${success ? '✅ PASS' : '❌ FAIL'}`);
    
    if (success) passed++;
    else failed++;
  }
  
  console.log('\n' + '='.repeat(60));
  console.log(`\nResults: ${passed} passed, ${failed} failed`);
  
  return failed === 0;
}

/**
 * Parse command-line arguments
 */
function parseArgs(args) {
  const parsed = {};
  
  for (const arg of args) {
    const [key, value] = arg.split('=');
    if (key.startsWith('--')) {
      const cleanKey = key.slice(2);
      
      if (value === 'true') parsed[cleanKey] = true;
      else if (value === 'false') parsed[cleanKey] = false;
      else if (value !== undefined) parsed[cleanKey] = value;
    }
  }
  
  return parsed;
}

// CLI entry point
if (require.main === module) {
  const args = process.argv.slice(2);
  
  if (args.includes('--test')) {
    const success = runTests();
    process.exit(success ? 0 : 1);
  } else if (args.includes('--help') || args.includes('-h')) {
    console.log(`
PDF Tool Selector - Choose the optimal PDF processing tool

Usage:
  node index.js [options]
  node index.js --test

Options:
  --isScanned=true|false      Document is image-based (requires OCR)
  --hasTables=true|false      Document contains tabular data
  --format=<format>           Document format (pdf, docx, pptx, etc.)
  --volume=<level>            Processing volume (low, medium, high)
  --needsMetadata=true|false  Extract comprehensive metadata
  --needsLayoutCoordinates    Need precise text positions
  --enterpriseJava=true|false Running in Java environment
  --language=<code>           Document language (en, es, zh, etc.)
  --test                      Run test scenarios
  --help, -h                  Show this help

Examples:
  node index.js --hasTables=true --format=pdf --volume=high
  node index.js --isScanned=true --format=pdf
  node index.js --format=docx --needsMetadata=true
`);
  } else {
    const input = parseArgs(args);
    
    if (Object.keys(input).length === 0) {
      console.log('No arguments provided. Use --help for usage or --test to run tests.');
      console.log('\nRunning default scenario (clean native PDF):');
      input.format = 'pdf';
      input.isScanned = false;
      input.hasTables = false;
      input.volume = 'medium';
    }
    
    const result = selectPdfTool(input);
    console.log('\nPDF Tool Recommendation\n');
    console.log('=' .repeat(60));
    console.log(`Tool:       ${result.tool}`);
    console.log(`Confidence: ${result.confidence}`);
    console.log(`Reasoning:  ${result.reasoning}`);
    console.log(`\nInstall:    ${result.installCommand}`);
    console.log(`\nAlternatives:`);
    for (const alt of result.alternatives) {
      console.log(`  - ${alt.tool} (${alt.confidence}): ${alt.tradeoff}`);
    }
    console.log(`\nCode Example:\n${result.codeExample}`);
  }
}

module.exports = { selectPdfTool, TOOLS, runTests };
