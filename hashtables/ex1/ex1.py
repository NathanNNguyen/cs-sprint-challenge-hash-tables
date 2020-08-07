def get_indices_of_item_weights(weights, length, limit):

    # for i in range(len(weights)):
    #     for k in range(len(weights)):
    #         if weights[i] + weights[k] == limit:
    #             return i, k

    # Traverse through the arr only once. Each time let's get the diff
    # of its value and the limit. Save the diff as key and value as index
    # into our cache. At some point if our item appear to be in the cache,
    # which means we found the 2 item that add up to the limit. Now we can
    # get the index of the first item in the list by accessing the cache with
    # that key. Now [i] would be the index at given time in the loop, we can
    # just return the values of both

    cache = {}
    for i in range(length):
        if weights[i] not in cache:
            diff = limit - weights[i]
            cache[diff] = i
        else:
            value = cache[weights[i]]
            return (i, value)

    return None


weights = [4, 6, 10, 15, 16]
length = 5
limit = 21

get_indices_of_item_weights(weights, length, limit)
