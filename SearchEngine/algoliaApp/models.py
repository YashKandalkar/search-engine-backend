from django.db import models

# Create your models here.

class AlgoliAppCLass(models.Model):
    url = models.TextField()
    text = models.TextField()

from algoliasearch.search_client import SearchClient

client = SearchClient.create('2P65DVMJ1J', '69cf5ae95ffbed6f5eca1520d7de0562')
index = client.init_index('index1')

# index = client.init_index('contacts')

res = index.search('malloc')
# res = index.search('query string', {
#     'attributesToRetrieve': [
#         'firstname',
#         'lastname'
#     ],
#     'hitsPerPage': 20
# })