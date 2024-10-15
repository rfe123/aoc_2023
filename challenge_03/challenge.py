#Load the inputs
f = open("input.txt", "r")

# symbol_idxs = []
digit_ranges = []
row_strs = []

all_symbols = []
all_digits = []

def is_between(num, lower, upper):
  """Checks if a number is between two others (inclusive)."""
  return lower <= num <= upper

count = 5

numeric = [str(x) for x in range(10)]

def get_digit_range(i, digit):
    start = i-len(digit)-1
    if start < 0:
        start = 0

    return [start, i, int(digit)]

for x in f:
    digit = ''
    row_strs.append(x)
    unique_symbols = []
    # row_symbol_idxs = []
    row_digit_ranges = []

    for i in range(len(x)-1):
        c = x[i]
        
        if c != '.':
            if c in numeric:
                digit += c
                if i == (len(x) - 2):
                    row_digit_ranges.append(get_digit_range(i, digit))
                    digit = ''
            else:
                if digit != '':
                    row_digit_ranges.append(get_digit_range(i, digit))
                    digit = ''
        else:
            if digit != '':
                row_digit_ranges.append(get_digit_range(i, digit))
                digit = ''
    
    # symbol_idxs.append(row_symbol_idxs)
    digit_ranges.append(row_digit_ranges) 
    
part_numbers = []

def check_symbol_row(s, ranges, printRows=False):
    # print(row_symbols)
    for d in ranges:
        if printRows: print(f'find: {s[0]} start: {d[0]} end: {d[1]} str: {d[2]}')
        if is_between(s[0], d[0], d[1]):
            if printRows: print(f'match: {s}')
            part_numbers.append(int(d[2]))
            
def check_digit_row(symbols, d, printRows=False):
    # print(row_symbols)
    for s in symbols:
        # if printRows: print(f'find: {s[0]} start: {d[0]} end: {d[1]} str: {d[2]}')
        if is_between(s[0], d[0]-1, d[1]+1):
            if printRows: print(f'match: {s}')
            part_numbers.append(int(d[2]))
            return True

loopNum = len(digit_ranges)
printRows = True

def is_symbol(c):
    return c not in numeric and c != '.'

for i in range(loopNum): 
    start_idx = i-1 if i>0 else 0
    end_idx = i+1 if i < (loopNum -1) else loopNum - 1
    if printRows: print(start_idx, i, end_idx)
    for d in digit_ranges[i]:
        if printRows: print(f'Check {d[2]}')
        for j in range(start_idx, end_idx+1):
            slice_str = row_strs[j][d[0]:d[1]+1]
            if printRows: print(slice_str)
            if any(c not in numeric and c != '.' for c in slice_str):
                if printRows: print('match')
                part_numbers.append(d[2])
                break
    
print(sum(part_numbers))
    
