# index.py

import algoliasearch_django as algoliasearch

from .models import AlgoliAppCLass

algoliasearch.register(AlgoliAppCLass)
