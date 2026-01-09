#!/bin/bash

################################################################################
# PlantUML Diagram Renderer
# 
# This script renders all PlantUML diagrams in the doc/ directory to images.
# Supports multiple output formats: PNG, SVG, PDF
#
# Usage:
#   ./render_diagrams.sh [format]
#
# Arguments:
#   format - Output format: png (default), svg, pdf, all
#
# Examples:
#   ./render_diagrams.sh           # Renders to PNG
#   ./render_diagrams.sh svg       # Renders to SVG
#   ./render_diagrams.sh all       # Renders to all formats
#
################################################################################

# Don't exit on error - we want to render all diagrams even if some fail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Configuration
FORMAT="${1:-png}"
PUML_FILES=(
    "use_case_diagram.puml"
    "activity_diagram.puml"
    "sequence_diagram.puml"
    "component_diagram.puml"
    "class_diagram.puml"
)

################################################################################
# Functions
################################################################################

print_header() {
    echo -e "${BLUE}╔════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BLUE}║          PlantUML Diagram Renderer                             ║${NC}"
    echo -e "${BLUE}╚════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
}

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

check_plantuml() {
    if command -v plantuml &> /dev/null; then
        print_success "PlantUML found: $(plantuml -version | head -1)"
        return 0
    elif command -v java &> /dev/null && [ -f "plantuml.jar" ]; then
        print_success "Using plantuml.jar with Java"
        USE_JAR=true
        return 0
    else
        return 1
    fi
}

download_plantuml() {
    print_info "Downloading PlantUML JAR..."
    curl -L -o plantuml.jar "https://github.com/plantuml/plantuml/releases/download/v1.2024.0/plantuml-1.2024.0.jar"
    if [ $? -eq 0 ]; then
        print_success "PlantUML JAR downloaded successfully"
        USE_JAR=true
        return 0
    else
        print_error "Failed to download PlantUML JAR"
        return 1
    fi
}

render_diagram() {
    local file=$1
    local format=$2
    
    if [ ! -f "$file" ]; then
        print_warning "File not found: $file"
        return 1
    fi
    
    local output_flag=""
    case "$format" in
        png) output_flag="-tpng" ;;
        svg) output_flag="-tsvg" ;;
        pdf) output_flag="-tpdf" ;;
        *) 
            print_error "Unknown format: $format"
            return 1
            ;;
    esac
    
    local render_status=0
    if [ "$USE_JAR" = true ]; then
        java -jar plantuml.jar $output_flag "$file" 2>&1 || render_status=$?
    else
        plantuml $output_flag "$file" 2>&1 || render_status=$?
    fi
    
    if [ $render_status -eq 0 ]; then
        local output_file="${file%.puml}.$format"
        print_success "Rendered: $output_file"
        return 0
    else
        print_error "Failed to render: $file"
        return 1
    fi
}

render_all_formats() {
    local file=$1
    
    for fmt in png svg pdf; do
        render_diagram "$file" "$fmt"
    done
}

################################################################################
# Main Script
################################################################################

print_header

# Check for PlantUML
print_info "Checking for PlantUML..."
if ! check_plantuml; then
    print_warning "PlantUML not found"
    print_info "Attempting to download PlantUML JAR..."
    
    if ! command -v java &> /dev/null; then
        print_error "Java not found. Please install Java or PlantUML:"
        echo ""
        echo "  Ubuntu/Debian:  sudo apt-get install plantuml"
        echo "  macOS:          brew install plantuml"
        echo "  Or install Java and rerun this script"
        exit 1
    fi
    
    if ! download_plantuml; then
        print_error "Could not set up PlantUML"
        exit 1
    fi
fi

echo ""
print_info "Rendering diagrams to $FORMAT format(s)..."
echo ""

# Render diagrams
SUCCESS_COUNT=0
FAIL_COUNT=0

for file in "${PUML_FILES[@]}"; do
    if [ "$FORMAT" = "all" ]; then
        render_all_formats "$file" && ((SUCCESS_COUNT++)) || ((FAIL_COUNT++))
    else
        render_diagram "$file" "$FORMAT" && ((SUCCESS_COUNT++)) || ((FAIL_COUNT++))
    fi
done

# Summary
echo ""
echo -e "${BLUE}════════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}Rendered:${NC} $SUCCESS_COUNT diagram(s)"
if [ $FAIL_COUNT -gt 0 ]; then
    echo -e "${RED}Failed:${NC} $FAIL_COUNT diagram(s)"
fi
echo -e "${BLUE}════════════════════════════════════════════════════════════════${NC}"
echo ""

# List generated files
if [ $SUCCESS_COUNT -gt 0 ]; then
    print_info "Generated files:"
    case "$FORMAT" in
        all)
            ls -lh *.png *.svg *.pdf 2>/dev/null | awk '{print "  " $9 " (" $5 ")"}'
            ;;
        *)
            ls -lh *.$FORMAT 2>/dev/null | awk '{print "  " $9 " (" $5 ")"}'
            ;;
    esac
    echo ""
fi

print_success "Done!"

exit 0