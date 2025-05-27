letters=["l", "a", "v", "a", "g", "m", "n", "a"]

freq={}

for ch in letters:
    freq[ch]=letters.count(ch)

print(freq)
print(freq.values())
print(max(freq.values()))
max_value=max(freq.values())
print(freq.keys())



