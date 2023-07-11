#!/usr/bin/python3
"""
Script to compute metrics from input lines read from stdin.
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C), the script prints the accumulated statistics.
"""
import sys


def compute_metrics():
    """
    Function to compute metrics from input lines read from stdin.

    Returns:
        None
    """
    total_size = 0
    status_counts = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            line = line.strip()
            _, _, _, _, _, status_code, file_size = line.split(" ")
            total_size += int(file_size)

            if status_code in status_counts:
                status_counts[status_code] += 1
            else:
                status_counts[status_code] = 1

            if i % 10 == 0:
                print("File size: {:d}".format(total_size))
                for code in sorted(status_counts.keys()):
                    print("{:s}: {:d}".format(code, status_counts[code]))

    except KeyboardInterrupt:
        print("File size: {:d}".format(total_size))
        for code in sorted(status_counts.keys()):
            print("{:s}: {:d}".format(code, status_counts[code]))


if __name__ == "__main__":
    compute_metrics()
