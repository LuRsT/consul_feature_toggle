import json
import logging
import os
import time

import consul


class ConsulKeyNotFound(Exception):
    pass


def get(key):
    kv_client = _get_kv_client()
    _, value = kv_client.get(key, index=None)
    if not value:
        raise ConsulKeyNotFound()
    else:
        value = json.loads(value['Value'].decode('utf-8'))
    return value


def put(key, value):
    kv_client = _get_kv_client()
    value = json.dumps(value)
    kv_client.put(key, value)


def _get_kv_client():
    client = consul.Consul(host='consul')
    return client.kv


def main():
    while True:
        time.sleep(5)
        try:
            logging.warning('Hello {}!'.format(get('name')))
        except ConsulKeyNotFound:
            logging.warning('Hello World!')
        except JSONDecodeError:
            logging.warning('JSON value pls!')


if __name__ == '__main__':
    main()
