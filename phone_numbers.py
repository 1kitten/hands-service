"""
Phone numbers founder module.
Opens .txt file named 'urls.txt' with list of
urls where module should find phone numbers in
format: 8KKKXXXXXX.

If there is any, numbers will be written
in 'founded_numbers.txt'
"""

import re
import urllib.request

opener = urllib.request.FancyURLopener({})
FOUNDED_PHONES = set()

with open('urls.txt', 'r') as urls_fi:
    data = urls_fi.readlines()

for i_url in data:
    f = opener.open(i_url.replace('\n', ''))
    content = f.read()
    phone_numbers = set(re.findall(rb'(8\s?\(?[4-9]\d{0,3}\)?\s?\d{3}-?\d{2}-?\d{2})', content))
    if phone_numbers:
        FOUNDED_PHONES.update(phone_numbers)

with open('founded_numbers.txt', 'w') as fi:
    if FOUNDED_PHONES:
        for i_phone_number in FOUNDED_PHONES:
            fi.write(i_phone_number.decode() + '\n')
    else:
        fi.write('No phones founded.')
