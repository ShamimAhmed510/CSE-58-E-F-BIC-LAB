p = input().strip()
g = input().strip()

print(*[i for i in range(len(g)-len(p)+1) if g[i:i+len(p)] == p])
