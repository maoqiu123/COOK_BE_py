# _*_ coding: utf-8 _*_
import memcache
from django.core.cache import cache

host_port = '127.0.0.1:11211'

mc = memcache.Client([host_port], debug=True)


def test():
    print(cache.set('name', 'maoqiu', 30))
    print(cache.get('name'))



