
def mismatch(s1 ,s2):
    return sum(c1 != c2 for c1, c2 in zip(s1,s2))

def approximate_pattern_matching(pattern, text , d):
    k = len(pattern)
    positions = []

    for i in range(len(text) - k + 1):
        window = text[i:i+k]
        if mismatch(pattern,  window) <= d:
            positions.append(i)
    
    return positions

pattern = input().strip()
text = input().strip()
d = int(input().strip())

result = approximate_pattern_matching(pattern, text, d)

print(*result)

