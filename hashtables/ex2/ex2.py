#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def __str__(self):
        return f"From {self.source} to {self.destination}"


# The tickets are messed up but we're still able to figure out a way
# to sort them. The very first ticket would be NONE -> 'something'.
# We can save the key:value as source:destination of tickets to a dict.
# We can add the very first destination to our arr. We should make a count
# for looping. Setting cur to value of the first k. Update our cur while
# we in the loop and append the cur everytime we updated it.

def reconstruct_trip(tickets, length):
    cache = {}
    route = []

    for i in tickets:
        k, v = i.source, i.destination
        cache[k] = v

    route.append(cache['NONE'])
    cur = cache[route[0]]
    count = 1

    while count < length:
        # while cur != 'NONE':
        route.append(cur)
        cur = cache[cur]
        count += 1

    return route


tickets = [
    Ticket("PIT", "ORD"),
    Ticket("XNA", "CID"),
    Ticket("SFO", "BHM"),
    Ticket("FLG", "XNA"),
    Ticket("NONE", "LAX"),
    Ticket("LAX", "SFO"),
    Ticket("CID", "SLC"),
    Ticket("ORD", "NONE"),
    Ticket("SLC", "PIT"),
    Ticket("BHM", "FLG")
]

length = 10

reconstruct_trip(tickets, length)
