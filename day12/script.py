with open('day12/in.txt') as f:
  actions = [(l[0], int(l[1:])) for l in f.readlines()]

  dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)] 
  x = y = d = 0
  for a in actions:
    if a[0] == 'N':
      y -= a[1]
    elif a[0] == 'E':
      x += a[1]
    elif a[0] == 'S':
      y += a[1]
    elif a[0] == 'W':
      x -= a[1]
    elif a[0] == 'L':
      d = (d - (a[1] // 90)) % 4
    elif a[0] == 'R':
      d = (d + (a[1] // 90)) % 4
    elif a[0] == 'F':
      x += a[1] * dirs[d][0]
      y += a[1] * dirs[d][1]
  print("Part 1:", abs(x) + abs(y))

  x = y = 0
  wx = 10
  wy = -1
  for a in actions:
    if a[0] == 'N':
      wy -= a[1]
    elif a[0] == 'E':
      wx += a[1]
    elif a[0] == 'S':
      wy += a[1]
    elif a[0] == 'W':
      wx -= a[1]
    elif a[0] == 'L' and a[1] == 90 or a[0] == 'R' and a[1] == 270:
      wx, wy = wy, -wx
    elif a[0] == 'R' and a[1] == 90 or a[0] == 'L' and a[1] == 270:
      wx, wy = -wy, wx
    elif a[0] in 'LR' and a[1] == 180:
      wx, wy = -wx, -wy
    elif a[0] == 'F':
      x += a[1] * wx
      y += a[1] * wy
  print("Part 2:",  abs(x) + abs(y))
