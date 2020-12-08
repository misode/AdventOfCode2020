import re

with open('day2/in.txt') as f:
  validPart1 = 0
  validPart2 = 0

  for line in f.readlines():
    match = re.match('(\d+)-(\d+) ([a-z]): ([a-z]+)', line)

    countPart1 = 0
    for char in match[4]:
      if char is match[3]:
        countPart1 += 1
    if int(match[1]) <= countPart1 <= int(match[2]):
      validPart1 += 1

    countPart2 = 0
    for pos in [int(match[1]), int(match[2])]:
      if match[4][pos - 1] is match[3]:
        countPart2 += 1
    if countPart2 is 1:
      validPart2 += 1

  print('Part 1:', validPart1)
  print('Part 1:', validPart2)
