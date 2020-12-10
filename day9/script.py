with open('day9/in.txt') as f:
  nums = [int(l) for l in f.readlines()]

  def findSum(i):
    for j in range(i - 25, i):
      for k in range(i - 25, i):
        if nums[j] == nums[k]:
          continue
        if nums[i] == nums[j] + nums[k]:
          return True
    return False

  x = 0
  for i in range(25, len(nums)):
    if not findSum(i):
      x = nums[i]
      break
  print("Part 1:", x)

  i = j = s = 0
  while True:
    if s < x:
      s += nums[j]
      j += 1
    elif s > x:
      s -= nums[i]
      i += 1
    if s == x:
      break
  range = nums[i:j+1]
  print("Part 2:", min(range) + max(range))
