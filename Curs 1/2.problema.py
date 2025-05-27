letters=["l", "a", "v", "a", "g", "m", "n", "a"]
contor=0
# de cate ori se gaseste "a" in lista
for ch in letters:
    if ch=="a":
        contor+=1
print(contor)
       
print(letters.count("a"))

# 2. care este caracterul care se gaseste de cele mai multe ori


letters=["l", "a", "v", "a", "g", "m", "n", "a"]
contor=0

freq={

}
for ch in letters:
    freq[ch]=0
print(freq)

for ch in letters:
    freq[ch]+=1
print(freq)