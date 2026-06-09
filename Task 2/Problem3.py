s = input().strip()

comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

ans = []

for ch in reversed(s):
    ans.append(comp[ch])

print("".join(ans))
