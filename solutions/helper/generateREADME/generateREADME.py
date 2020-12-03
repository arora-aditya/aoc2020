import json
import datetime

import os 
data_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data.json'))
output_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../../README.md'))

with open(data_path, 'r') as f:
    datastore = json.load(f)

YEAR = 2020

headers = [
    f"# Advent of Code {YEAR}",
    "",
    "My solutions to this year's problems linked [here](https://adventofcode.com/2020)",
    "",
    "## Progress",
    "",
]

max_len_c1, max_len_c2, max_len_c3, max_len_c4 = 3,0,0,0
for day, info in datastore.items():
    name, rank1, rank2 = info['name'], str(info['part1']), str(info['part2'])
    name = f'[{name}](https://adventofcode.com/{YEAR}/day/{int(day)})'
    max_len_c1 = max(max_len_c1, len(day))
    max_len_c2 = max(max_len_c2, len(name))
    max_len_c3 = max(max_len_c3, len(rank1))
    max_len_c4 = max(max_len_c4, len(rank2))

max_len_c2 += 5
max_len_c3 += 4
max_len_c4 += 4

table = [
    ['Day', 'Problem', 'Part One', 'Part Two'],
    [':' + '-'*(x-2)+':' for x in [max_len_c1, max_len_c2, max_len_c3, max_len_c4]],
]

for day, info in datastore.items():
    day = day
    name = info['name']
    name = f'[{name}](https://adventofcode.com/{YEAR}/day/{int(day)})'
    rank1 = str(info['part1'])
    rank2 = str(info['part2'])
    if rank1 == "-1" or rank2 == "-1":
        rank1 = " "
        rank2 = " "
    table.append([day, name, rank1, rank2])

with open(output_path, 'w') as f:
    for header in headers:
        f.write(header + '\n')
    for row in table:
        row = ' | '.join([
            row[0].ljust(max_len_c1, ' '),
            row[1].ljust(max_len_c2, ' '),
            row[2].ljust(max_len_c3, ' '),
            row[3].ljust(max_len_c4, ' '),
            ""
        ])
        f.write(row + '\n')
    f.write(f'\n\nAuto-Generated at {datetime.datetime.now()}')