f = open("input.txt", "r")

words =  [None,'one','two','three','four','five','six','seven','eight','nine']

lines = []

for x in f:
  print(x)
  first_idx = len(x) + 999
  first = None
  last_idx = -1
  last = None

  for i in range(1,10):
    dig_idx = x.find(str(i))
    wrd_idx = x.find(words[i])

    if dig_idx > -1:
      if dig_idx < first_idx:
        first_idx = dig_idx
        first = str(i)

    if wrd_idx > -1:
      if wrd_idx < first_idx:
        first_idx = wrd_idx
        first = i
  
    dig_idx = x.rfind(str(i))
    wrd_idx = x.rfind(words[i])

    if dig_idx > -1:
      if dig_idx > last_idx:
        last_idx = dig_idx
        last = str(i)

    if wrd_idx > -1:
      if wrd_idx > last_idx:
        last_idx = wrd_idx
        last = i
      
    print(f'first={first} last={last}')

  if first != None:
    line = int(f"{first}{last}")
    print(f"{x} : {line}")
    lines.append(line)

  
  # break
  

print(sum(lines))