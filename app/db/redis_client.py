import redis.asyncio as redis

DB_NAME = 10
redis_client = redis.Redis(db=DB_NAME, decode_responses=True)
