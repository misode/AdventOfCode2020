import re

def parseCommand(line: str):
  return list(re.match(r'([a-z]+) \+?(-?\d+)', line.rstrip()).groups())

def runProgram(commands):
  executed = set()
  ptr = 0
  acc = 0
  while ptr not in executed:
    if ptr >= len(commands):
      return (True, acc)
    executed.add(ptr)
    cmd = commands[ptr]
    if cmd[0] == 'nop':
      ptr += 1
    elif cmd[0] == 'acc':
      ptr += 1
      acc += int(cmd[1])
    elif cmd[0] == 'jmp':
      ptr += int(cmd[1])
  return (False, acc)

with open('day8/in.txt') as f:
  commands = [parseCommand(l) for l in f.readlines()]

  print("Part 1:", runProgram(commands)[1])

  for i in range(len(commands)):
    if commands[i][0] == 'acc':
      continue
    commands[i][0] = 'jmp' if commands[i][0] == 'nop' else 'nop'
    terminated, acc = runProgram(commands)
    if terminated:
      print("Part 2:", acc)
      break
    commands[i][0] = 'jmp' if commands[i][0] == 'nop' else 'nop'
