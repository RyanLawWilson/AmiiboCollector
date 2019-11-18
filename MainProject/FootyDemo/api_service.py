import json
import http.client
import requests

#Separate the API Service into its own module, imported by the views

SECRET_TOKEN = 'b8680a82289c4d74ae06a1763bf6339a'   #API token from registering for access


#Gets all the main areas for the competitions to populate first dropdown
def get_areas():
    #Code pulled from the API documentation, connection with token
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = {'X-Auth-Token': SECRET_TOKEN}    #passes token with request as headers
    connection.request('GET', '/v2/areas/2267', None, headers)  #specific request, using the global area number
    response = json.loads(connection.getresponse().read().decode())
    return response


#Gets all the child areas for the competitions to populate second dropdown
def get_children(parent):       #parent passed in is the selection from the first dropdown
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = {'X-Auth-Token': SECRET_TOKEN}
    query = '/v2/areas/{}'.format(parent)       #use query string so it can be formatted with selection
    connection.request('GET', query, None, headers)     #pass dynamic query instead of a constant value
    response = json.loads(connection.getresponse().read().decode())
    return response


#Gets all the competitions (aka leagues) to populate third dropdown
def get_leagues(area):      #area is selection from 3rd dropdown (or second if third not used)
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = {'X-Auth-Token': SECRET_TOKEN}
    query = '/v2/competitions?areas={}'.format(area)    #using filtering, from documentation, to get leagues
    connection.request('GET', query, None, headers)
    response = json.loads(connection.getresponse().read().decode())
    return response


#Gets all of the matches for the selected league/competition
def get_matches(code):
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = {'X-Auth-Token': SECRET_TOKEN}
    query = '/v2/competitions/{}/matches?status=FINISHED'.format(code) #filter for completed games only
    connection.request('GET', query, None, headers)
    response = json.loads(connection.getresponse().read().decode())
    # coding = open("json.txt","w")             #Used these lines for printing out the json
    # coding.write(str(response['matches']))    # so I could run it through CodeBeautify
    # coding.close
    return response

