"""
Phone numbers founder module.
Opens .txt file named 'urls.txt' with list of
urls where module should find phone numbers in
format: 8KKKXXXXXX.

If there is any, numbers will be written
in 'founded_numbers.txt'
"""

import json
import logging
import re
import threading
import time
import urllib.request
from typing import List, Optional, Dict, Set

opener: urllib.request.FancyURLopener = urllib.request.FancyURLopener({})
FOUNDED_PHONES: Set[Optional[str]] = set()
WEBSITES: Dict[str, List[str]] = {}
logger: logging.Logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def get_data(file_path: str = 'urls.txt'):
    with open(file_path) as urls_fi:
        data: List[Optional[str]] = urls_fi.readlines()
    return None if not data else data


def find_phone_numbers(url: str) -> None:
    f: opener = opener.open(url)
    content: bytes = f.read()
    phone_numbers: List[bytes] = list(set(
        re.findall(rb'(8\s?-?\(?[4-9]\d{0,3}\)?-?\s?-?\d{3}\s?-?\d{2}\s?-?\d{2})', content)
    ))
    if phone_numbers:
        filtered_phone_numbers: List[Optional[str]] = [
            i_number.decode() for i_number in phone_numbers if len(
                re.sub(r'\W', '', i_number.decode())
            ) == 11
        ]
        WEBSITES[url.replace('\n', '')] = filtered_phone_numbers
        FOUNDED_PHONES.update(filtered_phone_numbers)


def main() -> None:
    start: float = time.time()
    logger.info('Start founding phone numbers from urls.')

    try:
        threads: List[threading.Thread] = [threading.Thread(target=find_phone_numbers, args=(i_url.replace('\n', ''),))
                                           for i_url in get_data()]
        list(map(lambda x: x.start(), threads))
    except Exception as e:
        logger.error(f'An exception: {str(e)} was raised')
        return

    for thread in threads: thread.join()

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

    logger.info('Stop founding phone numbers. Done in {:.4}'.format(time.time() - start))


if __name__ == '__main__':
    main()
