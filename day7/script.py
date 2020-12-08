import re

def parseRule(rule: str):
  m = re.match(r'([a-z ]+) bags contain (.+)\.', rule)
  if m[2] == 'no other bags':
    return (m[1], [])
  def parseBagContent(content: str):
    n = re.match(r'(\d+) ([a-z ]+) bags?', content)
    return (int(n[1]), n[2])
  return (m[1], [parseBagContent(b.strip()) for b in m[2].split(',')])


with open('day7/in.txt') as f:
  rules = dict([parseRule(l.rstrip()) for l in f.readlines()])

  def canContainShinyGold(bag: str):
    for b in rules[bag]:
      if b[1] == 'shiny gold' or canContainShinyGold(b[1]):
        return True
    return False

  def numOfBagsInside(bag: str):
    return sum([b[0] * (1 + numOfBagsInside(b[1])) for b in rules[bag]])

  countPart1 = 0
  for b in rules.keys():
    if canContainShinyGold(b):
      countPart1 += 1
  print('Part 1:', countPart1)
  print('Part 2:', numOfBagsInside('shiny gold'))
