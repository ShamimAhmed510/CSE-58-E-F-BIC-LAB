
text = input().strip()
k = int(input())

freq = {}

for i in range(len(text) - k + 1):
    pat = text[i:i+k]
    freq[pat] = freq.get(pat, 0) + 1

mx = max(freq.values())

for key in freq:
    if freq[key] == mx:
        print(key, end=" ")
