import redis
def lambda_handler(event, context):
    endpoint = "<your redis endpoint>"
    r = redis.Redis(host=endpoint,port=6379,db=0)
    cleardown = r.flushall()
    print('Redis cleared ',cleardown)
    
