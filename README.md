# README

This program demonstrates how serialize/deserialize Python object as JSON to/from Redis 

## Prerequisites

This program requires:

- Python 2

- Redis


## How to run

- ```./write_py_obj_to_redis.py``` to write the python object to Redis.
- ```./read_py_obj_from_redis.py``` to the python object from Redis.

__NOTE__: You must write the python object to Redis before reading it.

## See Also

Read http://darmawan-salihun.blogspot.sg/2017/12/storing-python-object-in-redis-brute.html for the big picture explanation. _NOTE_: The article explains how to store the object via Python's pickle library. It has since been replaced by JSON serialization.

