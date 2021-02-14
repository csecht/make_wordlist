#!/usr/bin/env python3
"""
Cut and paste text from a source text into the parse_this.txt file
before running this script. Output is overwritten to now_parsed.txt.

    Copyright (C) 2021 C.S. Echt

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see https://www.gnu.org/licenses/.
"""
from pathlib import Path

__version__ = 0.1

words2parse_path = Path('parse_this.txt')
parsed_words_path = Path('now_parsed.txt')

words2parse = Path(words2parse_path).read_text()
parse_list = words2parse.split()

parsed_words = [word for word in parse_list if word.isalpha()]
unique_parsed = set(parsed_words)
subset_parsed = [word for word in unique_parsed if len(word) >= 3]

print(f'{len(parsed_words)} words in {words2parse_path}\n'
      f'{len(unique_parsed)} unique words\n'
      f'{len(subset_parsed)} unique with 3 or more letters in {parsed_words_path}'
      )

with open(parsed_words_path, 'w', encoding='utf-8') as file:
    for word in sorted(subset_parsed):
        file.write(word)
        file.write('\n')
