IN = (0,20,7,16,1,18,15)

def play(t):
  nums = dict([(n, i + 1) for i, n in enumerate(IN[:-1])])
  p = IN[-1]

  for i in range(len(IN), t):
    n = i - nums[p] if p in nums else 0
    nums[p] = i
    p = n

  return p

print('Part 1:', play(2020))
print('Part 2:', play(30000000))
