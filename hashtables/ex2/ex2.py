#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,
                        )
"""
Each ticket is represented as a Class with 
the following form:
"""

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

"""
Your function should output an array of strings with the entire route 
of your trip.
the `source` string represents the starting airport and the `destination` 
string represents the next airport along our trip. The ticket for your first 
flight has a destination with a `source` of `NONE`, and the ticket for your 
final flight has a `source` with a `destination` of `NONE`
## Hints
* The crux of this problem requires us to 'link' tickets together to reconstruct 
the entire trip. For example, if we have a ticket `('SJC', 'BOS')` that has us flying 
from San Jose to Boston, then there exists another ticket where Boston is the starting 
location: `('BOS', 'JFK')`. 
* We can hash each ticket such that the starting location is the key and the destination 
is the value. Then, when constructing the entire route, the `i`th location in the route 
can be found by checking the hash table for the `i-1`th location.
"""

def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    source = "NONE"

    for i in range(length):
        route[i] = hash_table_retrieve(hashtable, source)
        source = route[i]
    
    return route
