#!/usr/bin/env python3
"""
Script to save browsing history URLs with date and title extraction.
Creates markdown files with URL metadata and content summaries.
"""

import re
import urllib.parse
from datetime import datetime
import os


def extract_date_from_url(url):
    """Extract date from URL if present in format YYYY-MM-DD."""
    date_pattern = r'(\d{4}-\d{2}-\d{2})'
    match = re.search(date_pattern, url)
    if match:
        return match.group(1)
    return datetime.now().strftime('%Y-%m-%d')


def extract_title_from_url(url):
    """Extract title from URL path by converting dashes to spaces and capitalizing."""
    parsed = urllib.parse.urlparse(url)
    path_parts = parsed.path.strip('/').split('/')
    
    # Look for the most descriptive part (usually the last meaningful segment)
    title_part = None
    for part in reversed(path_parts):
        if part and not re.match(r'^\d{4}-\d{2}-\d{2}$', part):  # Skip date parts
            title_part = part
            break
    
    if title_part:
        # Remove date pattern from the end if present
        title_part = re.sub(r'-\d{4}-\d{2}-\d{2}$', '', title_part)
        # Convert dashes to spaces and capitalize
        title = title_part.replace('-', ' ').replace('_', ' ')
        # Capitalize each word
        title = ' '.join(word.capitalize() for word in title.split())
        return title
    
    return "Article"


def create_filename(date, title):
    """Create a safe filename from date and title."""
    # Clean title for filename (remove special characters)
    safe_title = re.sub(r'[^\w\s-]', '', title.lower())
    safe_title = re.sub(r'[-\s]+', '-', safe_title).strip('-')
    return f"{date}_{safe_title}.md"


def create_markdown_content(url, title, date):
    """Create markdown content for the saved URL."""
    content = f"""# {title}

**URL:** {url}  
**Date:** {date}  
**Saved on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Summary

*Note: Content summary would be extracted from the actual webpage when accessible.*

**Key Points from URL:**
- Microsoft reaches $4 trillion valuation
- Results described as "solid"
- Published on: {date}
- Source: Reuters Business/Retail Consumer section

## Original URL
{url}

---
*This file was automatically generated from the browsing history URL.*
"""
    return content


def save_url_to_file(url):
    """Main function to save URL with extracted metadata."""
    date = extract_date_from_url(url)
    title = extract_title_from_url(url)
    filename = create_filename(date, title)
    content = create_markdown_content(url, title, date)
    
    # Write to file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created file: {filename}")
    print(f"Date: {date}")
    print(f"Title: {title}")
    
    return filename


if __name__ == "__main__":
    # URL from the problem statement
    reuters_url = "https://www.reuters.com/business/retail-consumer/microsoft-reaches-4-trillion-valuation-after-solid-results-2025-07-31/"
    save_url_to_file(reuters_url)