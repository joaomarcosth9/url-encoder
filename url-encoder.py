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


try:
    url = input("Insert a URL: ")
    print(encode_url(url))

    command = 'echo "{0}" | xclip -sel clip'.format(encode_url(url))
    if os.name in ('nt', 'dos'):
        command = 'echo "{0}" | clip.exe'.format(encode_url(url))
    os.system(command)
except Exception as error:
    print("Error:", error)
