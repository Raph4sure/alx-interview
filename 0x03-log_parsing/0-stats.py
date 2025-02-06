#!/usr/bin/python3
import sys
import re

def print_stats(total_size, status_codes):
    """Print the statistics for file size and status codes."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

# Initialize variables
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        # Match the specific log format
        match = re.match(
            r'^(\d+\.\d+\.\d+\.\d+) - \[.*?\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$', 
            line.strip()
        )
        
        if match:
            # Extract status code and file size
            status_code = int(match.group(2))
            file_size = int(match.group(3))
            
            # Update totals
            if status_code in status_codes:
                status_codes[status_code] += 1
            total_size += file_size
            
            # Increment line count
            line_count += 1
            
            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
    
    # Print final stats if not already printed
    if line_count % 10 != 0:
        print_stats(total_size, status_codes)

except KeyboardInterrupt:
    # Print stats on keyboard interrupt
    print_stats(total_size, status_codes)