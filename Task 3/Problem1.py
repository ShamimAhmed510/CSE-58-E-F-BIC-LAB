from itertools import product

def mismatch(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def count_d(pattern, text, d):
    k = len(pattern)
    count = 0
    
    for i in range(len(text) - k + 1):
        window = text[i:i+k]
        if mismatch(pattern, window) <= d:
            count += 1
    
    return count


def frequent_words_with_mismatches(text, k, d):
    letters = ['A', 'C', 'G', 'T']
    freq_map = {}
    max_count = 0

    for pattern_tuple in product(letters, repeat=k):
        pattern = ''.join(pattern_tuple)
        
        count = count_d(pattern, text, d)
        freq_map[pattern] = count
        
        if count > max_count:
            max_count = count

    result = [p for p in freq_map if freq_map[p] == max_count]

    return result


text = input().strip()
k, d = map(int, input().split())

result = frequent_words_with_mismatches(text, k, d)
print(*result)
