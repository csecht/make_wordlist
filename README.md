# make_wordlist
Make a wordlist file of unique words from any input text file

A simple python script to create a wordlist from any text file, such as the custom wordlists used in the csecht/passphrase-generate repository.

Before running parser.py, the user cuts-and-pastes any source text into the default file, `parse_this.txt`.
Running the script provides terminal standout for numbers of words and writes unique words to a default, newline-delimited, utf-8 encoded, text file, `now_parsed.txt`. The folder SourceTexts contains examples of text file sources to cut-and-paste into `parse_this.txt`

Source files used for the csecht/passphrase-generate repository are provided in the SourceTexts directory as examples of source texts; they are not required to run the script.

parser.py was written with PyCharm using a Python 3.8 interpreter.

### Notes
- Hyphenated words in the source text will be split into component words. 
- Roman numerals, e.g. VIII, DXXIII, will be included as words if present in the source text.
- Only words 3 letters or longer are included in the results file, `now_parsed.txt`.
- The file `now_parsed.txt` is overwritten each time `parser.py` is run.

### License
Copyright (C) 2021 C.S. Echt, GNU General Public License, see https://www.gnu.org/licenses/

