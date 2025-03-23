# README - Autocomplete Name Extraction

## Overview
This project aims to extract all possible names from an undocumented autocomplete API hosted at `http://35.200.185.69:8000/v1/autocomplete`. Since no official documentation is available, the approach involves exploration and systematic querying to discover all names.

## Approach

1. **Exploratory API Requests**  
   - The API was probed using different query prefixes to understand its response format and behavior.
   - The endpoint follows the format:  
     `GET /v1/autocomplete?query=<string>`
   - The response is assumed to be a JSON array containing autocomplete suggestions.

2. **Systematic Querying Using a BFS Approach**  
   - The script starts by querying single-letter prefixes (`a-z`).
   - For each retrieved suggestion, if a new name is discovered, it is added to a queue for further exploration.
   - This breadth-first search (BFS) ensures minimal redundant requests while efficiently discovering all possible names.

3. **Handling API Responses and Errors**  
   - The script includes exception handling for timeouts and request failures.
   - Duplicate names are avoided using a set.
   - Sorting ensures the extracted names are displayed in an ordered manner.

## Running the Script

Ensure you have Python installed, then run the script:

```bash
python extract_autocomplete_names.py
```

## Findings
- The API successfully returns names based on a given prefix.
- The BFS approach effectively discovers longer names by progressively appending new suggestions to the search queue.
- Some prefixes return no results, indicating gaps in the autocomplete dataset.

## Potential Enhancements
- Parallel requests for faster extraction.
- Adaptive querying to focus on high-yield prefixes.
- Logging to analyze query efficiency over time.

---
This project provides a structured approach to extracting names from an unknown autocomplete API while ensuring efficiency and reliability.

