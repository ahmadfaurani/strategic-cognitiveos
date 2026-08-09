-- Research Stack Evidence Store Schema
-- PostgreSQL-compatible DDL

-- ============================================================================
-- CORE TABLES
-- ============================================================================

-- Research Tasks: Top-level container for research work
CREATE TABLE research_tasks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(500) NOT NULL,
    objective TEXT NOT NULL,
    pir TEXT[], -- Priority Intelligence Requirements (array)
    mode VARCHAR(50) NOT NULL, -- cyber_threat_intel, vendor_due_diligence, etc.
    owner VARCHAR(100),
    frequency VARCHAR(20), -- one-time, daily, weekly, monthly
    status VARCHAR(20) DEFAULT 'planning', -- planning, discovery, acquisition, analysis, complete, archived
    handling_classification VARCHAR(20) DEFAULT 'Internal', -- Internal, Confidential, Public
    personal_data_involved BOOLEAN DEFAULT FALSE,
    review_required BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    started_at TIMESTAMP WITH TIME ZONE,
    completed_at TIMESTAMP WITH TIME ZONE,
    archived_at TIMESTAMP WITH TIME ZONE,
    
    -- Scope fields
    scope_geography VARCHAR(200),
    scope_sector VARCHAR(200),
    scope_timeframe VARCHAR(100),
    scope_language VARCHAR(50) DEFAULT 'English',
    
    -- Output tracking
    output_format VARCHAR(50),
    output_path VARCHAR(500),
    
    -- Metrics
    sources_discovered INTEGER DEFAULT 0,
    sources_acquired INTEGER DEFAULT 0,
    findings_count INTEGER DEFAULT 0,
    high_confidence_findings INTEGER DEFAULT 0,
    processing_time_seconds INTEGER,
    
    CONSTRAINT status_check CHECK (status IN ('planning', 'discovery', 'acquisition', 'analysis', 'complete', 'archived'))
);

CREATE INDEX idx_tasks_status ON research_tasks(status);
CREATE INDEX idx_tasks_mode ON research_tasks(mode);
CREATE INDEX idx_tasks_owner ON research_tasks(owner);
CREATE INDEX idx_tasks_created ON research_tasks(created_at);

-- Research Sources: Individual sources discovered and acquired
CREATE TABLE research_sources (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    task_id UUID NOT NULL REFERENCES research_tasks(id) ON DELETE CASCADE,
    
    -- Source identification
    source_url TEXT NOT NULL,
    canonical_url TEXT,
    source_title VARCHAR(1000),
    domain VARCHAR(255),
    publisher VARCHAR(500),
    
    -- Classification
    source_type VARCHAR(50), -- news, official, technical, social, academic, regulatory, commercial
    discovery_query TEXT, -- The query that found this source
    
    -- Timing
    retrieved_at TIMESTAMP WITH TIME ZONE NOT NULL,
    published_at TIMESTAMP WITH TIME ZONE,
    
    -- Content storage (paths to files)
    content_hash VARCHAR(64), -- SHA-256 of content for deduplication
    markdown_path VARCHAR(500),
    json_path VARCHAR(500),
    screenshot_path VARCHAR(500),
    html_snapshot_path VARCHAR(500),
    
    -- Scoring
    authority_score DECIMAL(3,2) CHECK (authority_score >= 0 AND authority_score <= 1),
    relevance_score DECIMAL(3,2) CHECK (relevance_score >= 0 AND relevance_score <= 1),
    confidence_score DECIMAL(3,2) CHECK (confidence_score >= 0 AND confidence_score <= 1),
    
    -- Acquisition metadata
    acquisition_method VARCHAR(20), -- scrape, crawl, map, extract, screenshot, batch
    extraction_status VARCHAR(20) DEFAULT 'pending', -- pending, success, partial, failed
    extraction_time_ms INTEGER,
    firecrawl_job_id VARCHAR(100),
    
    -- Content metadata
    word_count INTEGER,
    language VARCHAR(10),
    
    -- Processing notes
    notes TEXT,
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    CONSTRAINT source_type_check CHECK (source_type IN ('news', 'official', 'technical', 'social', 'academic', 'regulatory', 'commercial', 'other')),
    CONSTRAINT extraction_status_check CHECK (extraction_status IN ('pending', 'success', 'partial', 'failed'))
);

CREATE INDEX idx_sources_task ON research_sources(task_id);
CREATE INDEX idx_sources_url ON research_sources(source_url);
CREATE INDEX idx_sources_domain ON research_sources(domain);
CREATE INDEX idx_sources_type ON research_sources(source_type);
CREATE INDEX idx_sources_confidence ON research_sources(confidence_score);
CREATE INDEX idx_sources_retrieved ON research_sources(retrieved_at);

-- Research Findings: Extracted and analyzed insights
CREATE TABLE research_findings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    task_id UUID NOT NULL REFERENCES research_tasks(id) ON DELETE CASCADE,
    
    -- Finding content
    finding_title VARCHAR(500),
    finding_summary TEXT,
    finding_type VARCHAR(50), -- fact, claim, statistic, quote, event, recommendation
    content TEXT, -- Full finding content
    
    -- Analysis
    implication TEXT, -- What this means
    recommended_action TEXT, -- Suggested follow-up
    
    -- Confidence & verification
    confidence_level VARCHAR(20), -- high, medium, low
    confidence_score DECIMAL(3,2) CHECK (confidence_score >= 0 AND confidence_score <= 1),
    verified BOOLEAN DEFAULT FALSE,
    verified_by VARCHAR(100), -- Agent ID or human reviewer
    verified_at TIMESTAMP WITH TIME ZONE,
    verification_method VARCHAR(100), -- cross_source, official_confirmation, logical_inference
    
    -- Tagging
    tags VARCHAR(100)[],
    entities JSONB, -- Extracted entities (people, orgs, locations, dates)
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    CONSTRAINT confidence_level_check CHECK (confidence_level IN ('high', 'medium', 'low'))
);

CREATE INDEX idx_findings_task ON research_findings(task_id);
CREATE INDEX idx_findings_confidence ON research_findings(confidence_level);
CREATE INDEX idx_findings_type ON research_findings(finding_type);
CREATE INDEX idx_findings_tags ON research_findings USING GIN(tags);
CREATE INDEX idx_findings_entities ON research_findings USING GIN(entities);

-- ============================================================================
-- RELATIONSHIP TABLES
-- ============================================================================

-- Finding-to-Source: Many-to-many relationship
CREATE TABLE finding_sources (
    finding_id UUID NOT NULL REFERENCES research_findings(id) ON DELETE CASCADE,
    source_id UUID NOT NULL REFERENCES research_sources(id) ON DELETE CASCADE,
    citation_text TEXT, -- Exact quoted text from source
    paragraph_number INTEGER,
    sentence_number INTEGER,
    
    PRIMARY KEY (finding_id, source_id)
);

CREATE INDEX idx_finding_sources_finding ON finding_sources(finding_id);
CREATE INDEX idx_finding_sources_source ON finding_sources(source_id);

-- Finding relationships: Related findings
CREATE TABLE finding_relationships (
    finding_id UUID NOT NULL REFERENCES research_findings(id) ON DELETE CASCADE,
    related_finding_id UUID NOT NULL REFERENCES research_findings(id) ON DELETE CASCADE,
    relationship_type VARCHAR(50), -- supports, contradicts, elaborates, supersedes
    
    PRIMARY KEY (finding_id, related_finding_id)
);

CREATE INDEX idx_finding_relationships_1 ON finding_relationships(finding_id);
CREATE INDEX idx_finding_relationships_2 ON finding_relationships(related_finding_id);

-- ============================================================================
-- OUTPUT TABLES
-- ============================================================================

-- Research Outputs: Generated reports, briefs, alerts
CREATE TABLE research_outputs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    task_id UUID NOT NULL REFERENCES research_tasks(id) ON DELETE CASCADE,
    
    -- Output metadata
    output_type VARCHAR(50), -- digest, alert, report, brief, matrix, tracker
    output_format VARCHAR(20), -- markdown, json, pdf, html
    title VARCHAR(500) NOT NULL,
    
    -- Content storage
    content_path VARCHAR(500), -- Path to output file
    content_markdown TEXT, -- Inline content (for smaller outputs)
    
    -- Quality metrics
    overall_confidence VARCHAR(20), -- high, medium, low
    findings_count INTEGER,
    verified_findings_count INTEGER,
    citation_count INTEGER,
    source_diversity_score DECIMAL(3,2),
    
    -- Distribution
    delivered_to VARCHAR(100)[], -- User IDs or channel IDs
    delivered_at TIMESTAMP WITH TIME ZONE,
    delivery_method VARCHAR(50), -- telegram, email, slack, api
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    CONSTRAINT output_confidence_check CHECK (overall_confidence IN ('high', 'medium', 'low'))
);

CREATE INDEX idx_outputs_task ON research_outputs(task_id);
CREATE INDEX idx_outputs_type ON research_outputs(output_type);
CREATE INDEX idx_outputs_delivered ON research_outputs(delivered_at);

-- ============================================================================
-- SKILL LIBRARY
-- ============================================================================

-- Skills: Reusable workflow definitions
CREATE TABLE skills (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL UNIQUE, -- e.g., "cyber/cve-monitoring"
    category VARCHAR(50) NOT NULL, -- cyber_threat_intel, vendor_due_diligence, etc.
    version VARCHAR(20) DEFAULT '1.0.0',
    description TEXT,
    
    -- Workflow definition
    trigger_patterns TEXT[], -- Patterns that activate this skill
    workflow_definition JSONB, -- Full workflow JSON
    parameters_schema JSONB, -- Parameter definitions
    output_template VARCHAR(100), -- Reference to template
    
    -- Quality thresholds
    min_confidence DECIMAL(3,2) DEFAULT 0.7,
    min_sources INTEGER DEFAULT 2,
    require_official_source BOOLEAN DEFAULT FALSE,
    
    -- Metrics
    times_executed INTEGER DEFAULT 0,
    avg_processing_time_seconds DECIMAL(10,2),
    avg_confidence_score DECIMAL(3,2),
    user_satisfaction DECIMAL(3,2), -- If rated
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    CONSTRAINT category_check CHECK (category IN ('cyber_threat_intel', 'vendor_due_diligence', 'competitive_intel', 'regulatory_monitoring', 'strategic_account_intel', 'tender_monitoring', 'media_registry'))
);

CREATE INDEX idx_skills_category ON skills(category);
CREATE INDEX idx_skills_name ON skills(name);

-- Skill executions: Track skill usage
CREATE TABLE skill_executions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    skill_id UUID NOT NULL REFERENCES skills(id) ON DELETE CASCADE,
    task_id UUID REFERENCES research_tasks(id) ON DELETE SET NULL,
    
    -- Execution context
    parameters JSONB, -- Parameters used for this execution
    started_at TIMESTAMP WITH TIME ZONE NOT NULL,
    completed_at TIMESTAMP WITH TIME ZONE,
    status VARCHAR(20), -- running, success, failed, cancelled
    
    -- Results
    output_path VARCHAR(500),
    confidence_score DECIMAL(3,2),
    findings_count INTEGER,
    
    -- Errors
    error_message TEXT,
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    CONSTRAINT execution_status_check CHECK (status IN ('running', 'success', 'failed', 'cancelled'))
);

CREATE INDEX idx_skill_executions_skill ON skill_executions(skill_id);
CREATE INDEX idx_skill_executions_task ON skill_executions(task_id);
CREATE INDEX idx_skill_executions_status ON skill_executions(status);

-- ============================================================================
-- AUDIT & MAINTENANCE
-- ============================================================================

-- Processing history: Track all actions on evidence
CREATE TABLE processing_history (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    task_id UUID NOT NULL REFERENCES research_tasks(id) ON DELETE CASCADE,
    source_id UUID REFERENCES research_sources(id) ON DELETE SET NULL,
    finding_id UUID REFERENCES research_findings(id) ON DELETE SET NULL,
    
    action VARCHAR(50) NOT NULL, -- acquired, analyzed, verified, summarized, exported, deleted
    agent_id VARCHAR(100), -- Which agent performed the action
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    notes TEXT,
    metadata JSONB
);

CREATE INDEX idx_processing_history_task ON processing_history(task_id);
CREATE INDEX idx_processing_history_action ON processing_history(action);
CREATE INDEX idx_processing_history_timestamp ON processing_history(timestamp);

-- Access log: Track who accessed what
CREATE TABLE access_log (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    task_id UUID REFERENCES research_tasks(id) ON DELETE SET NULL,
    source_id UUID REFERENCES research_sources(id) ON DELETE SET NULL,
    finding_id UUID REFERENCES research_findings(id) ON DELETE SET NULL,
    output_id UUID REFERENCES research_outputs(id) ON DELETE SET NULL,
    
    accessed_by VARCHAR(100) NOT NULL,
    accessed_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    access_type VARCHAR(20), -- view, download, export, edit
    
    CONSTRAINT access_type_check CHECK (access_type IN ('view', 'download', 'export', 'edit'))
);

CREATE INDEX idx_access_log_task ON access_log(task_id);
CREATE INDEX idx_access_log_user ON access_log(accessed_by);
CREATE INDEX idx_access_log_timestamp ON access_log(accessed_at);

-- ============================================================================
-- RETENTION & ARCHIVAL
-- ============================================================================

-- Retention policies
CREATE TABLE retention_policies (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    entity_type VARCHAR(50) NOT NULL, -- research_tasks, research_sources, research_findings
    retention_period_days INTEGER NOT NULL,
    archive_after_days INTEGER,
    auto_delete BOOLEAN DEFAULT FALSE,
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    CONSTRAINT entity_type_check CHECK (entity_type IN ('research_tasks', 'research_sources', 'research_findings', 'research_outputs'))
);

-- Archival queue
CREATE TABLE archival_queue (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    entity_type VARCHAR(50) NOT NULL,
    entity_id UUID NOT NULL,
    scheduled_date TIMESTAMP WITH TIME ZONE NOT NULL,
    action VARCHAR(20) NOT NULL, -- archive, delete
    
    processed BOOLEAN DEFAULT FALSE,
    processed_at TIMESTAMP WITH TIME ZONE,
    processed_by VARCHAR(100),
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    CONSTRAINT archival_action_check CHECK (action IN ('archive', 'delete'))
);

CREATE INDEX idx_archival_queue_scheduled ON archival_queue(scheduled_date);
CREATE INDEX idx_archival_queue_processed ON archival_queue(processed);

-- ============================================================================
-- VIEWS FOR COMMON QUERIES
-- ============================================================================

-- Task summary view
CREATE VIEW task_summary AS
SELECT 
    rt.id,
    rt.title,
    rt.mode,
    rt.status,
    rt.owner,
    rt.created_at,
    rt.completed_at,
    COUNT(DISTINCT rs.id) AS sources_count,
    COUNT(DISTINCT rf.id) AS findings_count,
    COUNT(DISTINCT ro.id) AS outputs_count,
    rt.high_confidence_findings,
    rt.processing_time_seconds
FROM research_tasks rt
LEFT JOIN research_sources rs ON rt.id = rs.task_id
LEFT JOIN research_findings rf ON rt.id = rf.task_id
LEFT JOIN research_outputs ro ON rt.id = ro.task_id
GROUP BY rt.id;

-- High-confidence findings view
CREATE VIEW high_confidence_findings AS
SELECT 
    rf.id,
    rf.finding_title,
    rf.finding_summary,
    rf.confidence_score,
    rf.verified,
    rt.title AS task_title,
    rt.mode AS task_mode
FROM research_findings rf
JOIN research_tasks rt ON rf.task_id = rt.id
WHERE rf.confidence_score >= 0.7
  AND rf.verified = TRUE
ORDER BY rf.confidence_score DESC, rf.created_at DESC;

-- Source coverage by task
CREATE VIEW task_source_coverage AS
SELECT 
    rt.id AS task_id,
    rt.title,
    COUNT(rs.id) AS total_sources,
    COUNT(CASE WHEN rs.source_type = 'official' THEN 1 END) AS official_sources,
    COUNT(CASE WHEN rs.source_type = 'news' THEN 1 END) AS news_sources,
    COUNT(CASE WHEN rs.source_type = 'technical' THEN 1 END) AS technical_sources,
    AVG(rs.confidence_score) AS avg_confidence,
    MAX(rs.retrieved_at) AS last_retrieval
FROM research_tasks rt
LEFT JOIN research_sources rs ON rt.id = rs.task_id
GROUP BY rt.id;

-- ============================================================================
-- INITIAL DATA
-- ============================================================================

-- Default retention policies
INSERT INTO retention_policies (entity_type, retention_period_days, archive_after_days, auto_delete) VALUES
('research_tasks', 730, 365, FALSE),
('research_sources', 365, 90, FALSE),
('research_findings', 730, 365, FALSE),
('research_outputs', 730, 365, FALSE);
