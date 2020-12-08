def getID(p: str):
  return sum((c in 'BR') * 2**(9 - i) for i, c in enumerate(p))

with open('day5/in.txt') as f:
  ids = sorted(getID(p.rstrip()) for p in f.readlines())
  print('Part 1:', ids[-1])

  for i in range(ids[0], ids[-1] + 1):
    if ids[i - ids[0]] != i:
      print("Part 2:", i)
      break
