with open('day11/in.txt') as f:
  original_layout = [list(l.rstrip()) for l in f.readlines()]
  n = len(original_layout)
  m = len(original_layout[0])

  dirs = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
  layout_a = [row.copy() for row in original_layout]
  layout_b = [row.copy() for row in original_layout]

  changed = True
  while changed:
    changed = False
    for i in range(n):
      for j in range(m):
        occupied = 0
        for k, l in dirs:
          if 0 <= i + k < n and 0 <= j + l < m:
            if layout_a[i + k][j + l] == '#':
              occupied += 1
        s = layout_a[i][j]
        if s == '.' or (s == 'L' and occupied > 0) or (s == '#' and occupied < 4):
          layout_b[i][j] = s
        else:
          changed = True
          layout_b[i][j] = '#' if s == 'L' else 'L'
    layout_a, layout_b = layout_b, layout_a
  count = "".join(["".join(row) for row in layout_a]).count('#')
  print("Part 1:", count)

  layout_a = [row.copy() for row in original_layout]
  changed = True
  while changed:
    changed = False
    for i in range(n):
      for j in range(m):
        occupied = 0
        for k, l in dirs:
          a, b = k, l
          while 0 <= i + a < n and 0 <= j + b < m:
            if layout_a[i + a][j + b] == '#':
              occupied += 1
              break
            if layout_a[i + a][j + b] == 'L':
              break
            a += k
            b += l
        s = layout_a[i][j]
        if s == '.' or (s == 'L' and occupied > 0) or (s == '#' and occupied < 5):
          layout_b[i][j] = s
        else:
          changed = True
          layout_b[i][j] = '#' if s == 'L' else 'L'
    layout_a, layout_b = layout_b, layout_a
  count = "".join(["".join(row) for row in layout_a]).count('#')
  print("Part 2:", count)
