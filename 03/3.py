#!/usr/bin/env python3

# Fix path so we can do a relative import: https://stackoverflow.com/a/27876800
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

        # Relative imports here
        from util import *

INPUT_FILE='3-input.txt'
#INPUT_FILE='3a-example.txt'

inputA = [(line[:split_idx], line[split_idx:]) for line in get_file_contents(INPUT_FILE)[0]
         if (split_idx := int(len(line)/2))]


def get_priority(char: str):
    if 97 <= (my_ord := ord(char)) <= 122:
        return my_ord - 97 + 1
    elif 65 <= (my_ord := ord(char)) <= 90:
        return my_ord - 65 + 27


print('Priority Sum', sum([get_priority(list(set(rucksack1).intersection(rucksack2))[0])
                           for rucksack1, rucksack2 in inputA]))

def inputB():
    buffer: List[str] = []
    iter = get_file_contents(INPUT_FILE)[0].__iter__()

    try:
        while True:
            buffer.append(next(iter))
            buffer.append(next(iter))
            buffer.append(next(iter))
            yield buffer
            buffer = []
    except StopIteration:
        return

print('Priority sum Part B:', sum([get_priority(list(set(rucksack1).intersection(set(rucksack2)).intersection(set(rucksack3)))[0]) for rucksack1, rucksack2, rucksack3 in inputB()]))
