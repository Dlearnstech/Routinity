import redis

# Connect to Redis Cloud
try:
    redis_client = redis.StrictRedis(
        host="redis-18029.c89.us-east-1-3.ec2.redns.redis-cloud.com",
        port=18029,
        password="ETzzKJ54aOZfZJGUITncMgJPqLxTlxDy",
        decode_responses=True
    )
    redis_client.ping()  # Test connection
    print("Successfully connected to Redis Cloud!")

except redis.ConnectionError as e:
    print(f"Error: {e}")