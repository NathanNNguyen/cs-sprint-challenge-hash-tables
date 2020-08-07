# First we can add these item to our HT to keep track of them.
# Brute force strategy would probably be multiply to a -1 to get
# the value of each item in the list so we can compare again.
# This is a tricky solution since it could introduce a buggy program.
# However we can check for a value and if there is the same negative
# value in the cache. That way we can figure out the solution

def has_negatives(a):
    result = []
    cache = {}

    for i in a:
        if i not in cache:
            cache[i] = i

    for k, v in cache.items():
        if k and -k in cache and k > 0:
            result.append(k)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
    print(has_negatives([1, 2, -1, -2, -3, -4, 4]))
