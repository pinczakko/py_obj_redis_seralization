import redis
import config as cfg
import pickle
import json

"""
 Connect to redis server
 Returns:
    Object representing Redis connection
"""
def connect(config_filename):
    # Init connection to the redis server
    redis_srv = {} 
    redis_cfg = cfg.get_redis_server_params(config_filename)
    redis_srv['host'] = redis_cfg['host']
    redis_srv['port'] = redis_cfg['port']
    redis_srv['db'] = redis_cfg['db']
    redis_obj = redis.StrictRedis(host=redis_srv['host'], port=redis_srv['port'], db=redis_srv['db'])
    if redis_obj == None:
        return False, None
    else:
        return True, redis_obj

def store_obj(redis_connection, key, py_obj):
    print ("redis key = " + key)
    #redis_connection.set(key, pickle.dumps(py_obj))
    obj_str = json.dumps(py_obj, default=lambda o: o.__dict__) 
    redis_connection.set(key, obj_str)

def get_objects_by_pattern(redis_connection, pattern):
    objs = []
    keys = redis_connection.scan_iter(match=pattern)
    for k in keys:
        """
        item = pickle.loads(redis_connection.get(k))
        if type(item) is str:
            obj_item = pickle.loads(item)
        else:
            obj_item = item
        """
        obj_item = json.loads(redis_connection.get(k)) 
        objs.append(obj_item)
    return objs 

