import random
from api_call import api_get


URL = 'https://reqres.in'
USERPAGE = '/api/users/'

class TestAPi:
	def test_api_smoke(self):
		response = api_get(url = URL, endpoint = (USERPAGE + str(random.randint(1, 12)))).send_get()
		assert response.status_code == 200
		assert sorted(list(response.response.keys())) == sorted(['data', 'support'])
		assert sorted(list(response.response['data'].keys())) == sorted(['id', 'email', 'first_name', 'last_name', 'avatar'])
		assert sorted(list(response.response['support'].keys())) == sorted(['url', 'text'])
