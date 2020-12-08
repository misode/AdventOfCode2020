import re

with open('day1/in.txt') as f:
  nums = [int(l) for l in f.readlines()]
  for i in range(len(nums)):
    for j in range(i):
      if nums[i] + nums[j] == 2020:
        print('Part 1:', nums[i] * nums[j])
      for k in range(j):
        if nums[i] + nums[j] + nums[k] == 2020:
          print('Part 2:', nums[i] * nums[j] * nums[k])
