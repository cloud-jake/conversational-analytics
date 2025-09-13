#!/bin/bash

#
# PDF to Markdown Batch Converter
#
# This script converts all .pdf files in the current directory to .md files
# using the 'pdftotext' and 'pandoc' command-line tools.
#
# Prerequisites:
# You must have 'poppler' (which provides pdftotext) and 'pandoc' installed.
# On macOS with Homebrew, you can install them with:
# brew install poppler pandoc
#

# --- Script Start ---

# Check if required commands are available in the system's PATH
if ! command -v pdftotext &> /dev/null || ! command -v pandoc &> /dev/null; then
    echo "Error: Required command not found." >&2
    echo "Please ensure 'poppler' (for pdftotext) and 'pandoc' are installed and in your PATH." >&2
    exit 1
fi

echo "Starting batch PDF to Markdown conversion..."

# Loop through every file ending with a .pdf extension in the current directory.
# The loop is case-insensitive for the extension (e.g., it will match .pdf, .PDF, .pDf).
shopt -s nullglob nocaseglob
for pdf_file in *.pdf; do
    # Get the filename without the .pdf extension.
    # This will be used for the output file.
    base_name="${pdf_file%.*}"
    output_file="${base_name}.md"

    echo "Converting '${pdf_file}' -> '${output_file}'"

    # Execute the conversion pipeline.
    # - 'pdftotext' extracts the text and layout from the PDF and pipes it to stdout.
    # - 'pandoc' reads the plain text from stdin and converts it to Markdown, saving the result.
    pdftotext -layout "${pdf_file}" - | pandoc -f markdown_strict --wrap=none -t markdown -o "${output_file}"
done

shopt -u nullglob nocaseglob
echo "-----------------------------------"
echo "Batch conversion complete."

