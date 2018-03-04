""" Kipoi website configuration file.
"""
DEBUG = True
EXPLAIN_TEMPLATE_LOADING = False

# Cache config
CACHE_TYPE = 'simple'  # 'memcached'
MEMCACHED_SERVERS = ['127.0.0.1:11211']
# Cache duration - set in seconds
CACHE_TIMEOUT = 600


SOURCE = "kipoi"
