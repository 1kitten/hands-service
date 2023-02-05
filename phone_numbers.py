"""
Phone numbers founder module.
Opens .txt file named 'urls.txt' with list of
urls where module should find phone numbers in
format: 8KKKXXXXXX.

If there is any, numbers will be written
in 'founded_numbers.txt'
"""

import json
import re
import urllib.request

opener = urllib.request.FancyURLopener({})
FOUNDED_PHONES = set()
WEBSITES = {}

# regex = "(8(\s?|-?)(\(?|-?)[4-9]\d{0,3}(\)?|-?)(\s?|-?)\d{3}(-?|\s?)\d{2}(-?|\s?)\d{2})"
# regex_old = "(8\s?\(?[4-9]\d{0,3}\)?\s?\d{3}-?\d{2}-?\d{2})"


def find_phone_numbers(url: str) -> None:
    f = opener.open(url)
    content = f.read()
    phone_numbers = list(set(re.findall(rb'(8\s?-?\(?[4-9]\d{0,3}\)?-?\s?-?\d{3}\s?-?\d{2}\s?-?\d{2})', content)))
    if phone_numbers:
        filtered_phone_numbers = [
            i_number.decode() for i_number in phone_numbers if len(
                i_number.decode().replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
            ) == 11
        ]
        WEBSITES[url.replace('\n', '')] = filtered_phone_numbers
        FOUNDED_PHONES.update(filtered_phone_numbers)


def main() -> None:
    with open('urls.txt', 'r') as urls_fi:
        data = urls_fi.readlines()

    for i_url in data:
        find_phone_numbers(url=i_url.replace('\n', ''))

    with open('founded_numbers.txt', 'w') as fi:
        if FOUNDED_PHONES:
            for i_phone_number in FOUNDED_PHONES:
                fi.write(i_phone_number + '\n')
        else:
            fi.write('No phones founded.')

    if WEBSITES:
        with open('phone_numbers.json', 'w') as fi:
            json_data = json.dumps(WEBSITES, indent=4)
            fi.write(json_data)


if __name__ == '__main__':
    main()
