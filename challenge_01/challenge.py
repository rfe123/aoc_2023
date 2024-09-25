#Load the inputs
f = open("input.txt", "r")

#Instantiate the digit strings
words =  [None,'one','two','three','four','five','six','seven','eight','nine']

lines = []

#Loop through input lines
for x in f:
  print(x)
  #init first/last placeholders for each line
  first_idx = len(x) + 999
  first = None
  last_idx = -1
  last = None

  for i in range(1,10):
    # Search for digit or number from left
    dig_idx = x.find(str(i))
    wrd_idx = x.find(words[i])

    #Save if found to left of first_idx
    if dig_idx > -1:
      if dig_idx < first_idx:
        first_idx = dig_idx
        first = str(i)

    if wrd_idx > -1:
      if wrd_idx < first_idx:
        first_idx = wrd_idx
        first = i
  
    # Search for digit or number from right
    dig_idx = x.rfind(str(i))
    wrd_idx = x.rfind(words[i])

    #Save if found to right of first_idx
    if dig_idx > -1:
      if dig_idx > last_idx:
        last_idx = dig_idx
        last = str(i)

    if wrd_idx > -1:
      if wrd_idx > last_idx:
        last_idx = wrd_idx
        last = i
      
    print(f'{i}: first={first} last={last}')

  if first != None:
    line = int(f"{first}{last}")
    print(f"{x} : {line}")
    #Concat & Store Result
    lines.append(line)

  
  # break
  
#Sum lines
print(sum(lines))