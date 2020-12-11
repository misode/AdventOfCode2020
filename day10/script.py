with open('day10/in.txt') as f:
  nums = sorted([int(l) for l in f.readlines()])

  diffs = [0, 0, 1]
  last = 0
  for n in nums:
    diffs[n - last - 1] += 1
    last = n
  print("Part 1:", diffs[0] * diffs[2])

  ways = { 0: 1 }
  for n in nums:
    ways[n] = sum([ways.get(n - i, 0) for i in [1, 2, 3]])
  print("Part 2:", ways[nums[-1]])
