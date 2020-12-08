import re

def testHeight(s):
  match = re.match(r'^(\d+)(cm|in)$', s)
  if not match:
    return False
  if match[2] == 'cm':
    return 150 <= int(match[1]) <= 193
  if match[2] == 'in':
    return 59 <= int(match[1]) <= 76

fieldTests = {
  'byr': lambda s: re.match(r'^\d{4}$', s) and 1920 <= int(s) <= 2002,
  'iyr': lambda s: re.match(r'^\d{4}$', s) and 2010 <= int(s) <= 2020,
  'eyr': lambda s: re.match(r'^\d{4}$', s) and 2020 <= int(s) <= 2030,
  'hgt': testHeight,
  'hcl': lambda s: re.match(r'^#[\da-f]{6}$', s),
  'ecl': lambda s: s in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
  'pid': lambda s: re.match(r'^\d{9}$', s)
}

def isValid(passport, validateFields = False):
  fields = dict([i.split(':') for i in passport.rstrip().split(' ')])
  for key in fieldTests:
    if key not in fields:
      return False
    if validateFields and not fieldTests[key](fields[key]):
      return False
  return True

with open('day4/in.txt') as f:
  validPart1 = 0
  validPart2 = 0
  passport = ''
  for line in [*f.readlines(), ""]:
    if line.rstrip():
      passport += line.rstrip() + ' '
    else:
      if isValid(passport):
        validPart1 += 1
      if isValid(passport, True):
        validPart2 += 1
      passport = ''
  print("Part 1:", validPart1)
  print("Part 2:", validPart2)
