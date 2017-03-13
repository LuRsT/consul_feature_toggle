import json
import logging
import os
import time

import consul


class ConsulKeyNotFound(Exception):
    pass


def get(key):
    client = consul.Consul(host='consul')
    _, value = client.kv.get(key, index=None)
    if not value:
        raise ConsulKeyNotFound()
    else:
        value = json.loads(value['Value'].decode('utf-8'))
    return value


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
