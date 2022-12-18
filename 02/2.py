#!/usr/bin/env python3
from collections import defaultdict
from enum import IntEnum
from functools import partial, reduce
from itertools import chain, cycle, takewhile
import math
from operator import mul
import os
import pprint
import re
from time import time
from typing import Dict, List, Set, Tuple, Union

from humanize import intcomma

# Fix path so we can do a relative import: https://stackoverflow.com/a/27876800
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

        # Relative imports here
        from util import *

INPUT_FILE='2-input.txt'
#INPUT_FILE='2a-example.txt'

input = [line.split(' ') for line in get_file_contents(INPUT_FILE)[0]]


class Choices(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


opponent_input_decoder = {
    'A': Choices.ROCK,
    'B': Choices.PAPER,
    'C': Choices.SCISSORS,
}

your_input_decoder = {
    'X': Choices.ROCK,
    'Y': Choices.PAPER,
    'Z': Choices.SCISSORS,
}


class RoundOutcome(IntEnum):
    LOSE = 0
    DRAW = 3
    WIN = 6




# Determine the round result
# key is opponent choice, inner-key is your choice
RESULTS_MAP_A = {
    Choices.ROCK: {
        Choices.ROCK: RoundOutcome.DRAW,
        Choices.PAPER: RoundOutcome.WIN,
        Choices.SCISSORS: RoundOutcome.LOSE,
    },
    Choices.PAPER: {
        Choices.ROCK: RoundOutcome.LOSE,
        Choices.PAPER: RoundOutcome.DRAW,
        Choices.SCISSORS: RoundOutcome.WIN,
    },
    Choices.SCISSORS: {
        Choices.ROCK: RoundOutcome.WIN,
        Choices.PAPER: RoundOutcome.LOSE,
        Choices.SCISSORS: RoundOutcome.DRAW,
    },
}

print(sum([RESULTS_MAP_A[opponent_input_decoder[opponent_choice]][your_input_decoder[your_choice]] + your_input_decoder[your_choice] for opponent_choice, your_choice in input]))

your_result_decoder = {
    'X': RoundOutcome.LOSE,
    'Y': RoundOutcome.DRAW,
    'Z': RoundOutcome.WIN,
}

RESULTS_MAP_B = {
    Choices.ROCK: {
        RoundOutcome.LOSE: Choices.SCISSORS,
        RoundOutcome.DRAW: Choices.ROCK,
        RoundOutcome.WIN: Choices.PAPER,
    },
    Choices.PAPER: {
        RoundOutcome.LOSE: Choices.ROCK,
        RoundOutcome.DRAW: Choices.PAPER,
        RoundOutcome.WIN: Choices.SCISSORS,
    },
    Choices.SCISSORS: {
        RoundOutcome.LOSE: Choices.PAPER,
        RoundOutcome.DRAW: Choices.SCISSORS,
        RoundOutcome.WIN: Choices.ROCK,
    },
}

print(sum([RESULTS_MAP_B[opponent_input_decoder[opponent_choice]][your_result_decoder[your_result]] + your_result_decoder[your_result] for opponent_choice, your_result in input]))
