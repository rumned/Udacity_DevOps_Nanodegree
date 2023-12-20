roman = {'i': 1, 'v': 5, 'x': 10}
roman['m'] = 1000
letters = list(roman.keys())
letters.sort()
print(" ".join(letters))