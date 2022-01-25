#!/usr/bin/python3

import os


def encode_url(original_url):
    encoded = ''
    for i in original_url:
        encoded += hex(ord(i)).replace('0x', '%')
    return encoded.upper()


try:
    url = input("Insert a URL: ")
    print(encode_url(url))

    command = 'echo {0} | xclip -sel clip'.format(encode_url(url))
    if os.name in ('nt', 'dos'):
        command = 'echo {0} | clip.exe'.format(encode_url(url))
    os.system(command)
except Exception as error:
    print("Error:", error)
