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
