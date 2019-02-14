#!/usr/bin/env python
# coding:utf-8


from rediscluster import StrictRedisCluster
import sys


def redis_cluster():
    redis_nodes = [{'host': '172.20.4.91', 'port': 7000},
                   {'host': '172.20.4.91', 'port': 7001},
                   {'host': '172.20.4.92', 'port': 7002},
                   {'host': '172.20.4.92', 'port': 7003},
                   {'host': '172.20.4.95', 'port': 7004},
                   {'host': '172.20.4.95', 'port': 7005}]
    try:
        redisconn = StrictRedisCluster(startup_nodes=redis_nodes)
    except Exception:
        print("Connect Error!")
        sys.exit(1)

    keys = redisconn.keys("rc.item.ft.*");
    for key in keys:
        redisconn.delete(key)
    print(len(keys))

redis_cluster()