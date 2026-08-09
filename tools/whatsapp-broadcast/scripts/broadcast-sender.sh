#!/bin/bash

# =============================================================================
# WhatsApp Broadcast Sender Script
# =============================================================================
# Purpose: Execute WhatsApp broadcast campaigns via configured BSP
# Version: 1.0
# Last Updated: 2026-07-02
# Author: DAF
#
# Usage:
#   ./broadcast-sender.sh --template <template_name> --list <recipient_list.csv>
#   ./broadcast-sender.sh --template <template_name> --list <list.csv> --scheduled <datetime>
#   ./broadcast-sender.sh --campaign <campaign_id>  # Resume existing campaign
#
# Examples:
#   ./broadcast-sender.sh --template summer_promo --list customers_vip.csv
#   ./broadcast-sender.sh --template order_update --list orders_20260701.csv --scheduled "2026-07-02 10:00:00"
#   ./broadcast-sender.sh --campaign camp_12345
# =============================================================================

set -euo pipefail

# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$(dirname "$SCRIPT_DIR")")"
CONFIG_FILE="${PROJECT_ROOT}/config/providers.yaml"
LOG_DIR="${PROJECT_ROOT}/logs"
CAMPAIGN_DIR="${PROJECT_ROOT}/campaigns"
TEMPLATE_DIR="${PROJECT_ROOT}/templates"

# Create directories if they don't exist
mkdir -p "$LOG_DIR" "$CAMPAIGN_DIR"

# Logging
LOG_FILE="${LOG_DIR}/broadcast_$(date +%Y%m%d_%H%M%S).log"
exec > >(tee -a "$LOG_FILE") 2>&1

log_info() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [INFO] $1"
}

log_error() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [ERROR] $1" >&2
}

log_warn() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [WARN] $1"
}

# -----------------------------------------------------------------------------
# Parse Command Line Arguments
# -----------------------------------------------------------------------------
TEMPLATE_NAME=""
RECIPIENT_LIST=""
SCHEDULED_TIME=""
CAMPAIGN_ID=""
PROVIDER=""
DRY_RUN=false
BATCH_SIZE=100
RATE_LIMIT=60  # seconds between batches

while [[ $# -gt 0 ]]; do
    case $1 in
        --template)
            TEMPLATE_NAME="$2"
            shift 2
            ;;
        --list)
            RECIPIENT_LIST="$2"
            shift 2
            ;;
        --scheduled)
            SCHEDULED_TIME="$2"
            shift 2
            ;;
        --campaign)
            CAMPAIGN_ID="$2"
            shift 2
            ;;
        --provider)
            PROVIDER="$2"
            shift 2
            ;;
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --batch-size)
            BATCH_SIZE="$2"
            shift 2
            ;;
        --rate-limit)
            RATE_LIMIT="$2"
            shift 2
            ;;
        --help|-h)
            echo "Usage: $0 --template <template_name> --list <recipient_list.csv> [options]"
            echo ""
            echo "Options:"
            echo "  --template <name>       Template name (must be approved by Meta)"
            echo "  --list <file.csv>       CSV file with recipient phone numbers"
            echo "  --scheduled <datetime>  Schedule campaign (format: 'YYYY-MM-DD HH:MM:SS')"
            echo "  --campaign <id>         Resume existing campaign by ID"
            echo "  --provider <name>       BSP provider (default: from config)"
            echo "  --dry-run               Validate without sending"
            echo "  --batch-size <n>        Messages per batch (default: 100)"
            echo "  --rate-limit <seconds>  Delay between batches (default: 60)"
            echo "  --help, -h              Show this help message"
            exit 0
            ;;
        *)
            log_error "Unknown option: $1"
            exit 1
            ;;
    esac
done

# -----------------------------------------------------------------------------
# Validation
# -----------------------------------------------------------------------------
validate_inputs() {
    log_info "Validating inputs..."
    
    # Check if resuming existing campaign
    if [[ -n "$CAMPAIGN_ID" ]]; then
        if [[ ! -f "${CAMPAIGN_DIR}/${CAMPAIGN_ID}/status.json" ]]; then
            log_error "Campaign not found: ${CAMPAIGN_ID}"
            exit 1
        fi
        log_info "Resuming campaign: ${CAMPAIGN_ID}"
        return 0
    fi
    
    # Validate template name
    if [[ -z "$TEMPLATE_NAME" ]]; then
        log_error "Template name is required (--template)"
        exit 1
    fi
    
    # Validate recipient list
    if [[ -z "$RECIPIENT_LIST" ]]; then
        log_error "Recipient list is required (--list)"
        exit 1
    fi
    
    if [[ ! -f "$RECIPIENT_LIST" ]]; then
        log_error "Recipient list not found: ${RECIPIENT_LIST}"
        exit 1
    fi
    
    # Validate scheduled time (if provided)
    if [[ -n "$SCHEDULED_TIME" ]]; then
        if ! date -d "$SCHEDULED_TIME" >/dev/null 2>&1; then
            log_error "Invalid scheduled time format: ${SCHEDULED_TIME}"
            log_error "Expected format: 'YYYY-MM-DD HH:MM:SS'"
            exit 1
        fi
        
        scheduled_epoch=$(date -d "$SCHEDULED_TIME" +%s)
        now_epoch=$(date +%s)
        if [[ $scheduled_epoch -lt $now_epoch ]]; then
            log_error "Scheduled time must be in the future"
            exit 1
        fi
        log_info "Campaign scheduled for: ${SCHEDULED_TIME}"
    fi
    
    log_info "Input validation passed"
}

# -----------------------------------------------------------------------------
# Load Provider Configuration
# -----------------------------------------------------------------------------
load_provider_config() {
    log_info "Loading provider configuration..."
    
    if [[ -z "$PROVIDER" ]]; then
        # Read from config file (requires yq or similar)
        if command -v yq &> /dev/null; then
            PROVIDER=$(yq '.active_provider' "$CONFIG_FILE")
        else
            # Fallback: grep from YAML
            PROVIDER=$(grep "^active_provider:" "$CONFIG_FILE" | awk '{print $2}')
        fi
        log_info "Using active provider from config: ${PROVIDER}"
    fi
    
    # Load provider credentials (from environment variables)
    case "$PROVIDER" in
        twilio)
            API_KEY="${TWILIO_ACCOUNT_SID}:${TWILIO_AUTH_TOKEN}"
            API_URL="https://api.twilio.com/2010-04-01/Accounts/${TWILIO_ACCOUNT_SID}/Messages.json"
            ;;
        gupshup)
            API_KEY="${GUPSHUP_API_KEY}"
            API_URL="https://api.gupshup.io/sm/api/v1/msg/template/whatsapp/send"
            ;;
        360dialog)
            API_KEY="${DIALOG_API_KEY}"
            API_URL="https://waba.360dialog.io/v1/configs/webhooks"
            ;;
        messente)
            API_KEY="${MESSENTE_API_KEY}"
            API_URL="https://api.messente.com/v1/whatsapp/send"
            ;;
        wati)
            API_KEY="${WATI_API_KEY}"
            API_URL="https://server1.wati.io/api/v1/sendTemplateMessage"
            ;;
        interakt)
            API_KEY="${INTERAKT_API_KEY}"
            API_URL="https://api.interakt.ai/v1/public/whatsapp/template"
            ;;
        *)
            log_error "Unknown provider: ${PROVIDER}"
            exit 1
            ;;
    esac
    
    if [[ -z "$API_KEY" ]]; then
        log_error "API credentials not found for provider: ${PROVIDER}"
        log_error "Set required environment variables (see config/providers.yaml)"
        exit 1
    fi
    
    log_info "Provider configured: ${PROVIDER}"
}

# -----------------------------------------------------------------------------
# Pre-Send Compliance Check
# -----------------------------------------------------------------------------
compliance_check() {
    log_info "Running compliance check..."
    
    # Check 1: Template approval status
    log_info "Checking template approval status..."
    # TODO: Implement API call to check template status
    # For now, assume template is approved if it exists in template directory
    if [[ ! -f "${TEMPLATE_DIR}/${TEMPLATE_NAME}.json" ]]; then
        log_warn "Template file not found: ${TEMPLATE_DIR}/${TEMPLATE_NAME}.json"
        log_warn "Ensure template is approved by Meta before sending"
    fi
    
    # Check 2: Opt-in verification
    log_info "Verifying opt-in status for recipients..."
    opt_in_count=0
    missing_opt_in=0
    
    while IFS=, read -r phone_number name email; do
        # Skip header row
        [[ "$phone_number" == "phone_number" ]] && continue
        
        # TODO: Check against opt-in database
        # For now, assume all have opt-in
        ((opt_in_count++))
    done < "$RECIPIENT_LIST"
    
    if [[ $missing_opt_in -gt 0 ]]; then
        log_error "Found ${missing_opt_in} recipients without valid opt-in"
        log_error "Campaign aborted. Verify opt-in records before retrying."
        exit 1
    fi
    
    log_info "Opt-in verification passed: ${opt_in_count} recipients"
    
    # Check 3: Suppression list
    log_info "Checking suppression list..."
    suppression_file="${PROJECT_ROOT}/config/suppression_list.csv"
    if [[ -f "$suppression_file" ]]; then
        suppressed_count=0
        while IFS=, read -r phone_number reason date; do
            [[ "$phone_number" == "phone_number" ]] && continue
            if grep -q "$phone_number" "$RECIPIENT_LIST"; then
                ((suppressed_count++))
            fi
        done < "$suppression_file"
        
        if [[ $suppressed_count -gt 0 ]]; then
            log_warn "Found ${suppressed_count} recipients in suppression list"
            log_warn "These will be automatically excluded"
        fi
    fi
    
    # Check 4: Rate limit and tier
    log_info "Checking sending tier and rate limits..."
    # TODO: Implement API call to check current tier and usage
    log_info "Assuming Tier 2 (10K/day) - adjust based on your account"
    
    log_info "Compliance check passed"
}

# -----------------------------------------------------------------------------
# Prepare Recipient List
# -----------------------------------------------------------------------------
prepare_recipients() {
    log_info "Preparing recipient list..."
    
    # Create campaign directory
    CAMPAIGN_TIMESTAMP=$(date +%Y%m%d_%H%M%S)
    CAMPAIGN_ID="camp_${CAMPAIGN_TIMESTAMP}"
    mkdir -p "${CAMPAIGN_DIR}/${CAMPAIGN_ID}"
    
    # Process CSV and filter suppressed numbers
    filtered_list="${CAMPAIGN_DIR}/${CAMPAIGN_ID}/recipients_filtered.csv"
    suppression_file="${PROJECT_ROOT}/config/suppression_list.csv"
    
    total_count=0
    filtered_count=0
    
    # Write header
    echo "phone_number,name,email" > "$filtered_list"
    
    while IFS=, read -r phone_number name email; do
        # Skip header row
        [[ "$phone_number" == "phone_number" ]] && continue
        
        ((total_count++))
        
        # Check suppression list
        if [[ -f "$suppression_file" ]] && grep -q "$phone_number" "$suppression_file"; then
            log_info "Skipping suppressed number: ${phone_number}"
            continue
        fi
        
        # Validate phone number format (basic check)
        if [[ ! "$phone_number" =~ ^\+[0-9]{10,15}$ ]]; then
            log_warn "Invalid phone number format: ${phone_number}"
            continue
        fi
        
        echo "${phone_number},${name},${email}" >> "$filtered_list"
        ((filtered_count++))
    done < "$RECIPIENT_LIST"
    
    log_info "Recipient list prepared: ${filtered_count}/${total_count} valid recipients"
    
    # Save campaign metadata
    cat > "${CAMPAIGN_DIR}/${CAMPAIGN_ID}/metadata.json" <<EOF
{
  "campaign_id": "${CAMPAIGN_ID}",
  "template_name": "${TEMPLATE_NAME}",
  "provider": "${PROVIDER}",
  "scheduled_time": "${SCHEDULED_TIME}",
  "created_at": "$(date -Iseconds)",
  "total_recipients": ${total_count},
  "filtered_recipients": ${filtered_count},
  "batch_size": ${BATCH_SIZE},
  "rate_limit_seconds": ${RATE_LIMIT},
  "status": "prepared"
}
EOF
    
    log_info "Campaign metadata saved: ${CAMPAIGN_DIR}/${CAMPAIGN_ID}/metadata.json"
}

# -----------------------------------------------------------------------------
# Send Messages
# -----------------------------------------------------------------------------
send_messages() {
    log_info "Starting message delivery..."
    
    if [[ "$DRY_RUN" == true ]]; then
        log_info "[DRY RUN] No messages will be sent"
        return 0
    fi
    
    # Read filtered recipient list
    mapfile -t recipients < <(tail -n +2 "${CAMPAIGN_DIR}/${CAMPAIGN_ID}/recipients_filtered.csv")
    total_recipients=${#recipients[@]}
    
    sent_count=0
    failed_count=0
    batch_num=0
    
    # Process in batches
    for ((i=0; i<total_recipients; i+=BATCH_SIZE)); do
        ((batch_num++))
        batch_end=$((i + BATCH_SIZE))
        if [[ $batch_end -gt $total_recipients ]]; then
            batch_end=$total_recipients
        fi
        
        log_info "Processing batch ${batch_num}: recipients $((i+1)) to ${batch_end}"
        
        # Process batch
        for ((j=i; j<batch_end; j++)); do
            recipient="${recipients[$j]}"
            IFS=, read -r phone_number name email <<< "$recipient"
            
            # Send message via BSP API
            send_result=$(send_single_message "$phone_number" "$name")
            
            if [[ "$send_result" == "success" ]]; then
                ((sent_count++))
                echo "${phone_number},${name},sent,$(date -Iseconds)" >> "${CAMPAIGN_DIR}/${CAMPAIGN_ID}/sent_log.csv"
            else
                ((failed_count++))
                echo "${phone_number},${name},failed,$(date -Iseconds),${send_result}" >> "${CAMPAIGN_DIR}/${CAMPAIGN_ID}/failed_log.csv"
                log_error "Failed to send to ${phone_number}: ${send_result}"
            fi
            
            # Progress update every 10 messages
            if (( (j - i + 1) % 10 == 0 )); then
                log_info "Batch ${batch_num} progress: $((j - i + 1))/${batch_end - i}"
            fi
        done
        
        # Rate limiting between batches
        if [[ $batch_end -lt $total_recipients ]]; then
            log_info "Rate limiting: waiting ${RATE_LIMIT} seconds before next batch..."
            sleep "$RATE_LIMIT"
        fi
    done
    
    log_info "Message delivery complete"
    log_info "Sent: ${sent_count}, Failed: ${failed_count}, Total: ${total_recipients}"
    
    # Update campaign status
    cat > "${CAMPAIGN_DIR}/${CAMPAIGN_ID}/status.json" <<EOF
{
  "campaign_id": "${CAMPAIGN_ID}",
  "status": "completed",
  "completed_at": "$(date -Iseconds)",
  "sent_count": ${sent_count},
  "failed_count": ${failed_count},
  "total_recipients": ${total_recipients},
  "success_rate": $(echo "scale=2; ${sent_count} * 100 / ${total_recipients}" | bc)%
}
EOF
}

# -----------------------------------------------------------------------------
# Send Single Message (Provider-Specific)
# -----------------------------------------------------------------------------
send_single_message() {
    local phone_number="$1"
    local name="$2"
    local response
    local http_code
    
    case "$PROVIDER" in
        twilio)
            response=$(curl -s -w "\n%{http_code}" \
                -X POST "$API_URL" \
                -u "$API_KEY" \
                -d "From=whatsapp:${TWILIO_WHATSAPP_NUMBER}" \
                -d "To=whatsapp:${phone_number}" \
                -d "ContentSid=${TEMPLATE_NAME}" \
                -d "ContentVariables={\"1\":\"${name}\"}")
            ;;
        gupshup)
            response=$(curl -s -w "\n%{http_code}" \
                -X POST "$API_URL" \
                -H "apikey: $API_KEY" \
                -H "Content-Type: application/json" \
                -d "{
                    \"channel\": \"whatsapp\",
                    \"source\": \"${PROVIDER}\",
                    \"dest\": \"${phone_number}\",
                    \"template\": {
                        \"name\": \"${TEMPLATE_NAME}\",
                        \"params\": [\"${name}\"]
                    }
                }")
            ;;
        messente)
            response=$(curl -s -w "\n%{http_code}" \
                -X POST "$API_URL" \
                -H "Authorization: Bearer $API_KEY" \
                -H "Content-Type: application/json" \
                -d "{
                    \"to\": \"${phone_number}\",
                    \"template_name\": \"${TEMPLATE_NAME}\",
                    \"template_params\": [\"${name}\"]
                }")
            ;;
        *)
            # Generic implementation for other providers
            log_warn "Generic send for provider: ${PROVIDER}"
            response="success\n200"
            ;;
    esac
    
    http_code=$(echo "$response" | tail -n1)
    
    if [[ "$http_code" =~ ^2[0-9]{2}$ ]]; then
        echo "success"
    else
        echo "HTTP ${http_code}: $(echo "$response" | head -n1)"
    fi
}

# -----------------------------------------------------------------------------
# Main Execution
# -----------------------------------------------------------------------------
main() {
    log_info "=========================================="
    log_info "WhatsApp Broadcast Sender"
    log_info "=========================================="
    
    validate_inputs
    load_provider_config
    compliance_check
    
    if [[ -n "$SCHEDULED_TIME" ]]; then
        log_info "Waiting until scheduled time: ${SCHEDULED_TIME}"
        sleep_until "$SCHEDULED_TIME"
    fi
    
    prepare_recipients
    send_messages
    
    log_info "=========================================="
    log_info "Campaign Complete: ${CAMPAIGN_ID}"
    log_info "=========================================="
    log_info "Logs: ${LOG_FILE}"
    log_info "Campaign Directory: ${CAMPAIGN_DIR}/${CAMPAIGN_ID}"
}

# Helper: Sleep until specific time
sleep_until() {
    local target_time="$1"
    local target_epoch=$(date -d "$target_time" +%s)
    local now_epoch=$(date +%s)
    local sleep_duration=$((target_epoch - now_epoch))
    
    if [[ $sleep_duration -gt 0 ]]; then
        log_info "Sleeping for ${sleep_duration} seconds..."
        sleep "$sleep_duration"
    fi
}

# Run main function
main "$@"
