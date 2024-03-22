import redis.asyncio as redis

from app.constants import REDIS_HOST, REDIS_PORT

DB_NAME = 10
redis_client = redis.Redis(
    host=REDIS_HOST, port=REDIS_PORT, db=DB_NAME, decode_responses=True)
