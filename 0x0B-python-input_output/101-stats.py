#!/usr/bin/python3
"""Module containing a script that reads stdin line by line and computes,
metrics"""
import sys


def print_metrics(total_size, status_codes):
    """
    Prints the metrics computed from the input lines.

    Args:
        total_size (int): Total file size.
        status_codes (dict): Dictionary of status codes and their counts.

    Returns:
        None
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        count = status_codes[code]
        print("{}: {}".format(code, count))

def parse_line(line):
    """
    Parses a line and extracts the file size and status code.

    Args:
        line (str): Line of input.

    Returns:
        tuple: Tuple containing the file size (int) and status code (str).
    """
    line_parts = line.split()
    file_size = int(line_parts[-1])
    status_code = line_parts[-2]
    return file_size, status_code

def process_lines():
    """
    Processes input lines, computes metrics, and prints statistics.

    Returns:
        None
    """
    total_size = 0
    status_codes = {}

    try:
        line_count = 0
        for line in sys.stdin:
            file_size, status_code = parse_line(line)
            total_size += file_size
            status_codes[status_code] = status_codes.get(status_code, 0) + 1

            line_count += 1
            if line_count % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)

if __name__ == "__main__":
    process_lines()
