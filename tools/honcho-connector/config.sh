#!/bin/bash
# Honcho Connector — Shared Configuration
# Source this from recall.sh, ingest.sh, query.sh

HONCHO_URL="${HONCHO_URL:-http://localhost:8000}"
WORKSPACE="${HONCHO_WORKSPACE:-cognitiveos}"
DEFAULT_TIMEOUT=5
LOG_DIR="$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")/logs"
mkdir -p "$LOG_DIR"

# Logging helper
log() {
    local script="$1"
    local status="$2"
    local message="$3"
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) | $script | $status | $message" >> "$LOG_DIR/$script.log"
}

# HTTP helper with timeout and fail-open
honcho_api() {
    local method="$1"
    local endpoint="$2"
    local data="$3"
    local timeout="${4:-$DEFAULT_TIMEOUT}"

    local url="${HONCHO_URL}${endpoint}"
    local response

    if [ -n "$data" ]; then
        response=$(curl -s -m "$timeout" -X "$method" "$url" \
            -H "Content-Type: application/json" \
            -d "$data" 2>/dev/null)
    else
        response=$(curl -s -m "$timeout" -X "$method" "$url" \
            -H "Content-Type: application/json" 2>/dev/null)
    fi

    local curl_exit=$?

    if [ $curl_exit -ne 0 ]; then
        echo "{\"error\": \"curl_exit=$curl_exit\", \"endpoint\": \"$endpoint\"}"
        return 1
    fi

    if [ -z "$response" ]; then
        echo "{\"error\": \"empty_response\", \"endpoint\": \"$endpoint\"}"
        return 1
    fi

    echo "$response"
    return 0
}
