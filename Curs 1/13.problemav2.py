letters=["l", "a", "v", "a", "g", "m", "n", "a"]
contor=0

freq={

}

for ch in letters:
    freq[ch]= freq.get(ch,0)+1

print(freq)
max_freq=0
for key in freq:
    print(freq[key])
    if freq[key]>max_freq:
        max_freq=freq[key]
        max_key=key

print("valoarea maxima:", max_freq)
print("litera care se intalneste cel mai des", max_key)        