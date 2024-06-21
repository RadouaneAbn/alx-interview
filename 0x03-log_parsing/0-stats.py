#!/usr/bin/python3
""" This script that reads stdin line by line and computes metrics """

import sys
import re

pattern = (
    r"^\d{,3}\.\d{,3}\.\d{,3}\.\d{,3}\s-\s"
    r"\[[^\[\]]*\]\s\"GET /projects/260 HTTP/1\.1\"\s(.+)\s(\d+)$"
)

totale_size = 0
status_count = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
i = 0


def print_log(totale_size, status_count):
    """ This function prints statistics of a log """
    print("File size: {}".format(totale_size))
    for key, value in sorted(status_count.items()):
        if value:
            print("{}: {}".format(key, value))


try:
    for line in sys.stdin:
        result = re.match(pattern, line.strip())
        if not result and not size.isnumeric():
            continue
        status_code, size = result.group(1, 2)
        if status_code in status_count:
            status_count[status_code] += 1
        totale_size += int(size)
        i += 1
        if i == 10:
            print_log(totale_size, status_count)
            i = 0
except KeyboardInterrupt:
    pass
print_log(totale_size, status_count)
