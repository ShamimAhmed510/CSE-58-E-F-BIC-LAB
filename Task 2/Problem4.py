
pattern = input().strip()
genome = input().strip()

k = len(pattern)
res = []

for i in range(len(genome) - k + 1):
    if genome[i:i+k] == pattern:
        res.append(str(i))

print(" ".join(res))
