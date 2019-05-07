import sys
import redis


def check_big_key(r, k):
    bigKey = False
    length = 0
    try:
        type = r.type(k)
        if type == "string":
            length = r.strlen(k)
        elif type == "hash":
            length = r.hlen(k)
        elif type == "list":
            length = r.llen(k)
        elif type == "set":
            length = r.scard(k)
        elif type == "zset":
            length = r.zcard(k)
    except:
        return
    if length > 10240:
        bigKey = True
    if bigKey:
        print (db, k, type, length)


def find_big_key_normal(db_host, db_port, db_password, db_num):
    r = redis.StrictRedis(host=db_host, port=db_port, password=db_password, db=db_num)
    for k in r.scan_iter(count=1000):
        check_big_key(r, k)


def find_big_key_sharding(db_host, db_port, db_password, db_num, nodecount):
    r = redis.StrictRedis(host=db_host, port=db_port, password=db_password, db=db_num)
    cursor = 0
    for node in range(0, nodecount):
        while True:
            iscan = r.execute_command("iscan", str(node), str(cursor), "count", "1000")
            for k in iscan[1]:
                check_big_key(r, k)
            cursor = iscan[0]
            print (cursor, db, node, len(iscan[1]))
            if cursor == "0":
                break;


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print ('Usage: python ', sys.argv[0], ' host port password ')
        exit(1)
    db_host = sys.argv[1]
    db_port = sys.argv[2]
    db_password = sys.argv[3]
    r = redis.StrictRedis(host=db_host, port=int(db_port), password=db_password)
    nodecount = r.info()['nodecount']
    keyspace_info = r.info("keyspace")
    for db in keyspace_info:
        print ('check ', db, ' ', keyspace_info[db])
        if nodecount > 1:
            find_big_key_sharding(db_host, db_port, db_password, db.replace("db", ""), nodecount)
        else:
            find_big_key_normal(db_host, db_port, db_password, db.replace("db", ""))
