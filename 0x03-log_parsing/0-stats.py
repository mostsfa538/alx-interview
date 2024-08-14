#!/usr/bin/python3
""" Log parsing """
import re


def check_input(line):
    """ doc """
    regex = r'^[\S]+\s*-\s*\[\d{4}-\d\d-\d\d\s*\d\d:\d\d:\d\d\.\d{6}\]'
    regex2 = r'\s*"GET \/projects\/260 HTTP\/1\.1"\s*(\S+)\s*(\d+)$'
    match = re.match(regex + regex2, line)

    if match:
        status_code = match.group(1)
        file_size = int(match.group(2))

        return [status_code, file_size]
    return []


def print_data(file_size=0, data={}):
    """ doc """
    print(f'File size: {file_size}', flush=True)
    for key in sorted(data.keys()):
        if data[key] == 0:
            continue
        print(f'{key}: {data[key]}', flush=True)


def show_status():
    """ doc """
    status_code = {
        '200': 0, '301': 0,
        '400': 0, '401': 0,
        '403': 0, '404': 0,
        '405': 0, '500': 0,
    }
    file_size = 0
    counter = 0
    try:
        while True:
            line = input()
            data = check_input(line)
            if len(data) == 0:
                continue
            if data[0] in status_code.keys():
                status_code[data[0]] += 1
            file_size += data[1]
            counter += 1
            if counter == 10:
                print_data(file_size, status_code)
                counter = 0

    except (KeyboardInterrupt, EOFError):
        print_data(file_size, status_code)
        counter = 0


if __name__ == "__main__":
    """ main function """
    show_status()
