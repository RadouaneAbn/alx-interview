#!/usr/bin/python3
""" This script that reads stdin line by line and computes metrics """

import sys
import re

pattern = (
    r"^\d{,3}\.\d{,3}\.\d{,3}\.\d{,3}\s-\s"
    r"\[[^\[\]]*\]\s\"GET /projects/260 HTTP/1\.1\"\s(.+)\s(\d+)$"
)

status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
totale_size = 0
status_count = {}
i = 0


def print_log(totale_size, status_count):
    """ This function prints statistics of a log """
    print("File size: {}".format(totale_size))
    for key, value in sorted(status_count.items()):
        print("{}: {}".format(key, value))


try:
    for line in sys.stdin:
        result = re.match(pattern, line.strip())
        if not result:
            continue
        status_code, size = result.group(1, 2)
        if status_code.isnumeric() and status_code in status_codes:
            status_count[status_code] = status_count.get(
                status_code, 0
                ) + 1
        totale_size += int(size)
        i += 1
        if i == 10:
            print_log(totale_size, status_count)
            i = 0
except KeyboardInterrupt:
    pass
print_log(totale_size, status_count)
