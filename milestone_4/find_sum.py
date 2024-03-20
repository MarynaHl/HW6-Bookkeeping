def find_sum(target, li):
    n = len(li)
    for i in range(n):
        for j in range(i + 1, n):
            if li[i] + li[j] == target:
                return (li[i], li[j])

def find_sum_fast(target, li):
    num_index = {}
    for i, num in enumerate(li):
        complement = target - num
        if complement in num_index:
            return (complement, num)
        num_index[num] = i

# Test cases
assert find_sum(5, [1, 2, 3, 4, 5]) in {(1, 4), (2, 3)}
assert find_sum_fast(5, [1, 2, 3, 4, 5]) in {(1, 4), (2, 3)}