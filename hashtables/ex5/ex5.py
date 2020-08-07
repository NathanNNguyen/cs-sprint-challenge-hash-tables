# First we figure out what the name of the files are, then
# let's set it into our cache with the key being the name and
# value being the whole path. Once we done that, we can now
# compare between the key in our cache and the name of the queries.
# If match, we found our solution, just append them to the result []

def finder(files, queries):
    cache = {}
    result = []

    for path in files:
        name = path.split('/')[-1]

        if name not in cache:
            cache[name] = path

    for i in queries:
        if i in cache:
            result.append(cache[i])

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
