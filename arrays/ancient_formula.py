
def solve():
    '''
    Given n integers and an integer k, returns the absolute difference between k and a combination of sums and
    products of the n integers. Do by brute force.
    '''
    n, k = map(int, raw_input().split())
    arr = map(int, raw_input().split())
    permutations = permute(arr)
    result = []
    print permutations
    for perm in permutations:
        results = generate_results(perm)
        result.extend(results)
def generate_results(perm):
    results = []


def permute(LIST):
    length=len(LIST)
    if length <= 1:
        return [LIST]
    else:
        result = []
        for n in range(0,length):
             for end in permute( LIST[:n] + LIST[n+1:] ):
                 result.append([ LIST[n] ] + end)
        return result

solve()

# for x in permute(["3","3","4"]):
#     print x
