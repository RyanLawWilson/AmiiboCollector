import json
import http.client
import requests

SECRET_TOKEN = 'b8680a82289c4d74ae06a1763bf6339a'


def get_areas():
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = {'X-Auth-Token': SECRET_TOKEN}
    connection.request('GET', '/v2/areas/2267', None, headers)
    response = json.loads(connection.getresponse().read().decode())
    return response


def get_children(parent):
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = {'X-Auth-Token': SECRET_TOKEN}
    query = '/v2/areas/{}'.format(parent)
    connection.request('GET', query, None, headers)
    response = json.loads(connection.getresponse().read().decode())
    return response


def get_leagues(area):
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = {'X-Auth-Token': SECRET_TOKEN}
    query = '/v2/competitions?areas={}'.format(area)
    connection.request('GET', query, None, headers)
    response = json.loads(connection.getresponse().read().decode())
    return response


def get_matches(code):
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = {'X-Auth-Token': SECRET_TOKEN}
    query = '/v2/competitions/{}/matches?status=FINISHED'.format(code)
    connection.request('GET', query, None, headers)
    response = json.loads(connection.getresponse().read().decode())
    # coding = open("json.txt","w")             #Used these lines for printing out the json
    # coding.write(str(response['matches']))    # so I could run it through CodeBeautify
    # coding.close
    return response

