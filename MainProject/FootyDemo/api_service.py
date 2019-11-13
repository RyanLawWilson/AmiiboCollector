import json
import http.client
import requests

SECRET_TOKEN = 'b8680a82289c4d74ae06a1763bf6339a'

def GetAreas():
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = {'X-Auth-Token': SECRET_TOKEN}
    connection.request('GET', '/v2/areas/2267', None, headers)
    response = json.loads(connection.getresponse().read().decode())
    return response
