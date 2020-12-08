

with open('day3/in.txt') as f:
  trees = []
  for line in f.readlines():
    trees.append([c == '#' for c in line.strip()])
  
  w = len(trees[0])
  h = len(trees)

  def traverse(dx, dy):
    count = 0
    x = 0
    y = 0
    while y < h:
      if trees[y][x % w]:
        count += 1
      x += dx
      y += dy
    return count
  
  print('Part 1:', traverse(3, 1))

  slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
  product = 1
  for dx, dy in slopes:
    count = traverse(dx, dy)
    product *= count

  print('Part 2:', product)
