#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""
import sys
from collections import defaultdict
import re

def parse_line(line):
    """
    Parses a line of log and extracts the status code and
    file size if the format is correct.
    """
    try:
        # Regular expression to match the log format
        match = re.match(
            r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] \"GET /projects/260 HTTP/1.1\" (\d{3}) (\d+)",
            line
        )
        if match:
            status_code = int(match.group(3))
            file_size = int(match.group(4))
            if status_code in {200, 301, 400, 401, 403, 404, 405, 500}:
                return status_code, file_size
    except (IndexError, ValueError):
        pass
    return None, None

def print_stats(status_codes, total_file_size):
    """
    Prints the current statistics.
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

def main():
    """ Log parsing"""
    status_codes = defaultdict(int)
    total_file_size = 0
    line_count = 0

    try:
        for line in sys.stdin:
            status_code, file_size = parse_line(line)
            if status_code is not None and file_size is not None:
                status_codes[status_code] += 1
                total_file_size += file_size
                line_count += 1

                if line_count % 10 == 0:
                    print_stats(status_codes, total_file_size)
    except KeyboardInterrupt:
        # Print statistics on keyboard interruption
        print_stats(status_codes, total_file_size)

if __name__ == "__main__":
    main()
