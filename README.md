# LRUCache
## What is an LRU Cache?
Caches are a type of storage that store data in memory for fast retrieval.
Generally stored as a key-value
AKA you access the data via an identifying key of some sort
Example: RAM on your computer
OS stores data in RAM for faster access than the hard drive
Uses the address of the memory cell as the key
LRU caches are a specific type of cache w/ the unique feature of removing the least recently fetched value from the cache when it’s out of space
## Why are LRU Caches useful?
Problem: 
Slow-under performing websites ca result in lost revenue
Querying databases, especially when they contain a lot of data can be quite slow
Solution: 
Cache
Advantage: Since they keep data in memory, they are much more performant than traditional databases.
Caching can dramatically decrease the load on the databases
## How to Build an LRU Cache
Step 1: API (Which methods do we need to implement?)
get(key)
set(key, value)

Other requirements:
When LRU is max size, remove the LRU key
Whenever a key is fetched or updated, it becomes the most recently used key.
Both get and set operations must be O(1)
When fetching a key that doesn’t exist, return a null value

Step 2: Which data structure?

Since we need get and set operations to be O(1) → hashmap/ dictionary
But a dictionary does not allow for removal of the oldest key
We could use a timestamp as part of the dictionary to update it whenever the key is fetched. (gives us oldest key-value pair but O(n) :((  )
Answer: We need two data structures:
Fetching the values (dictionary/hashmap)
 Keeping the items sorted by recency of use
What data structure for the second data structure?
Array… hmm close
Each key in the dictionary would reference the index of a value in the array and whenever a key is referenced, we can move that value to the front of the array and push the rest back.
But, that inserting requires moving all the elements → O(n) 
Gets slower as the array increases in size
Data structure w/ same benefits w/ get, set, and delete in O(1) time
Doubly-Linked List 
Each key in the dictionary will reference a node in our linked list allowing us to easily fetch/update/delete data





