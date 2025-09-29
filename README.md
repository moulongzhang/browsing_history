# browsing_history

A repository for saving browsing history URLs with automatic date and title extraction.

## Features

- Automatically extracts date and title from URLs
- Creates markdown files with standardized naming: `YYYY-MM-DD_title.md`
- Generates structured content with URL metadata and summary placeholders
- Supports various URL formats with intelligent title parsing

## Usage

Run the script with a URL to save:

```bash
python3 save_url.py
```

The script will:
1. Extract the date from the URL (format: YYYY-MM-DD)
2. Parse the title from the URL path
3. Create a markdown file with the format: `YYYY-MM-DD_cleaned-title.md`
4. Generate structured content including URL, date, and summary placeholder

## Example

For the URL: `https://www.reuters.com/business/retail-consumer/microsoft-reaches-4-trillion-valuation-after-solid-results-2025-07-31/`

Creates file: `2025-07-31_microsoft-reaches-4-trillion-valuation-after-solid-results.md`

## File Structure

Each saved URL creates a markdown file containing:
- Title as main header
- Original URL
- Publication date
- Save timestamp
- Summary section (with placeholder for content extraction)
- Original URL reference

## Files

- `save_url.py` - Main script for URL processing and file creation
- `YYYY-MM-DD_title.md` - Generated markdown files for each saved URL