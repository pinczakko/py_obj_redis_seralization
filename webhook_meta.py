import pickle
import redis_interface as redis_iface

# Returns WebhookMetadata object containing the target webhook metadata
def deserialize_webhook_metadata(redis_connection, webhook_id):
    p = "test-meta-webhook-" + webhook_id
    m_arr = redis_iface.get_objects_by_pattern(redis_connection, p)
    if len(m_arr) > 0:
        m = m_arr[0] # Get only the first match
        print ("Object with key [" + str(p) + "] is deserialized from Redis")
        print ("Type of returned object is: " + str(type(m)))
        return True, m 
    else:
        return False, None


class WebhookMetadata:
    def __init__(self, subs_id, user_id, expiration_time):
        self.subs_id = subs_id 
        self.user_id = user_id
        self.expiration_time = expiration_time 
    
    def serialize(self, redis_conn):
        key = "test-meta-webhook-" + self.subs_id 
        redis_iface.store_obj(redis_conn, key, self)
        print ("Object with key [" + str(key) + "] stored in Redis")

    def print_self(self):
        print("subs_id = " + self.subs_id)
        print("user_id = " + self.user_id)
        print("expiration_time = " + self.expiration_time)

