str1 = "B7A1R3"
alphabets = []
numbers = []

for ch in str1:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        numbers.append(ch)
        
print(sorted(alphabets) + sorted(numbers))
