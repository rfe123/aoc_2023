f = open("input.txt", "r")

lines = []

for x in f:
  first = None
  last = None

  for c in x:
    if c.isnumeric():
        if first == None:
           first = c
        last = c

  if first != None:
    line = int(f"{first}{last}")
    print(line)
    lines.append(line)

print(sum(lines))