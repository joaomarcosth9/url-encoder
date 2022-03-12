#!/usr/bin/python3

import os


def encode_url(original_url):
    encoded = ''
    if 'http://' in original_url:
        original_url = original_url.replace('http://', '')
    elif 'https://' in original_url:
        original_url = original_url.replace('https://', '')
    for i in original_url:
        if i not in ['/', '+', '?', '&', '#', '=', '.']:
            encoded += hex(ord(i)).replace('0x', '%')
        else:
            encoded += i
    return encoded.upper()


def main():
    try:
        url = input('Insert a URL: ')
        encoded_url = encode_url(url)
        print(encoded_url)

        command = f"echo {encoded_url} | xclip -sel clip"
        if os.name in ('nt', 'dos'):
            command = f"echo {encoded_url} | clip.exe"
        os.system(command)
    except Exception as error:
        print('Error:', error)


if __name__ == '__main__':
    main()
