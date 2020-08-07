# Worst case we have to do a double forloop. Setting our item
# in the cache first so we can keep track of the duplicates.
# Increase its counts if already exists, other wise just set it
# to 1. Once we already have that in our cache, we can loop through
# it to check if there is any value that appears more than once.
# Once that's figured out we now know the values that are duplicates

def intersection(arrays):
    result = []
    cache = {}

    for array in arrays:

        for item in array:

            if item in cache:
                cache[item] += 1

            else:
                cache[item] = 1

    for k, v in cache.items():
        if v > 1:
            result.append(k)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(10, 20)) + [1, 2, 3])
    arrays.append(list(range(20, 30)) + [1, 2, 3])
    arrays.append(list(range(30, 40)) + [1, 2, 3])

    print(intersection(arrays))
