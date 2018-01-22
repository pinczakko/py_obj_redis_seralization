#!/usr/bin/env python2

import redis_interface as redis_iface 
import json 
import pickle
from webhook_meta import WebhookMetadata, deserialize_webhook_metadata


def print_delimiter():
    print ("---------------------------------------------------------")

if __name__ == '__main__':
    status, redis_conn = redis_iface.connect('app_config.ini') 
    if status == False:
        print ("ERROR: Failed to connect to Redis server!")
    else: 
        print_delimiter()
        status, read_wm =  deserialize_webhook_metadata(redis_conn, "subs_id_aaaa")
        if status == False:
            print ("ERROR: Failed to get metadata from Redis server!")
        else:
            #read_wm.print_self()
            print("Object read from redis = " + json.dumps(read_wm, indent=2))
            print_delimiter()
