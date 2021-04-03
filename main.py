import requests
import os
import json
import time
import sys
 

def checkIfLive(Client_ID, Client_Secret, channelName):
    # Getting the token from the new Twitch API.
    url = "https://id.twitch.tv/oauth2/token" + "?client_id=" + Client_ID + "&client_secret=" + Client_Secret + "&grant_type=client_credentials"
    r = requests.post(url)

    output = json.loads(r.text)
    
    # Checking if the client secret is correct and raising an error.
    try:
        token = output['access_token']
    except:
        print("Your client secret is incorrect, make sure you copy it correctly and try again.")
        sys.exit(1)


    # Sending a request with the token collected above, to receive the channel current statistics.
    channelUrl = "https://api.twitch.tv/helix/streams?user_login=" + str(channelName)
    auth = 'Bearer ' + token 

    # The headers to send with the get request to twitch's API server.
    headers = {
    'Authorization': auth,
    'client-id': Client_ID
    }

    r = requests.get(url = channelUrl, headers = headers) # Sending the request to Twitch's API server.
    
    # Formatting the JSON and checking if the data field is empty or not.
    output = json.loads(r.text)['data'] 
    return len(output) != 0             


# Enter your client ID and your client Secret in the variables here:
# *** The credintials requested below can be granted through the twitch API website, in this link: 
Client_ID = ''
Client_Secret = ''

channel_name = '' 
# Channel name refers the words after the last '/' in the URL of the channel.
# For example: https://www.twitch.tv/rocketleague channel name is - 'rocketleague'  
# So if you want to check for this channel just enter 'rocketleague' in the variable.

print(checkIfLive(Client_ID, Client_Secret, channel_name))
# True - currently in live.
# False - not living currently.


