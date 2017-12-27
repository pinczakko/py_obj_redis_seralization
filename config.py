# Module to parse configuration file

import ConfigParser

def get_redis_server_params(cfg_file_path):
    cfg = ConfigParser.RawConfigParser()
    cfg.read(cfg_file_path)
    params = {'host': cfg.get('RedisServer','host'),
              'port': cfg.get('RedisServer','port'), 
              'db': cfg.get('RedisServer','db')} 
    ## Dump the result to screen
    print "Redis Server Parameters: "
    for key, val in params.iteritems():
        print key + " : " + val
    return params

