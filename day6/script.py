
with open('day6/in.txt') as f:
  lines = ''.join(f.readlines()).rstrip()
  groups = lines.split('\n\n')

  countPart1 = 0
  countPart2 = 0
  for g in groups:
    persons = [set(p) for p in g.split('\n')]
    union = set().union(*persons)
    intersection = persons[0].intersection(*persons)
    countPart1 += len(union)
    countPart2 += len(intersection)
  
  print("Part 1:", countPart1)
  print("Part 2:", countPart2)
