# Project: 0x01. Caching

## Resources

#### Read or watch:

- [What is a caching system?](https://aws.amazon.com/caching/#:~:text=A%20cache's%20primary%20purpose%20is,is%20usually%20complete%20and%20durable.)
- [Cache replacement policies - FIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29)
- [Cache replacement policies - LIFO](https://www.youtube.com/watch?v=7lxAfszjy68)
- [Cache replacement policies - LRU](https://www.youtube.com/watch?v=_Hh-NcdbHCY)
- [Cache replacement policies - MRU](https://www.youtube.com/watch?v=_Hh-NcdbHCY)
- [Cache replacement policies - LFU](https://www.youtube.com/watch?v=_Hh-NcdbHCY)

## Learning Objectives

- What a caching system is
- What FIFO means
- What LIFO means
- What LRU means
- What MRU means
- What LFU means
- What the purpose of a caching system
- What limits a caching system have

## More Info

### Parent class `BaseCaching`

All your classes must inherit from `BaseCaching` defined below:

```
$ cat base_caching.py
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
""" BaseCaching defines: - constants of your caching system - where your data are stored (in a dictionary)
"""
MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
```

## Tasks

| Task                | File                                   |
| ------------------- | -------------------------------------- |
| 0. Basic dictionary | [0-basic_cache.py](./0-basic_cache.py) |
| 1. FIFO caching     | [1-fifo_cache.py](./1-fifo_cache.py)   |
| 2. LIFO Caching     | [2-lifo_cache.py](./2-lifo_cache.py)   |
| 3. LRU Caching      | [3-lru_cache.py](./3-lru_cache.py)     |
| 4. MRU Caching      | [4-mru_cache.py](./4-mru_cache.py)     |
| 5. LFU Caching      | [100-lfu_cache.py](./100-lfu_cache.py) |
