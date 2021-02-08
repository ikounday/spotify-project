import requests
import base64
import json
import pandas as pd
from secret import *

# - Authorization
url = "https://accounts.spotify.com/api/token"
headers = {}
data = {}

# Encode as Base64
message = f"{clientId}:{clientSecret}"
messageBytes = message.encode('ascii')
base64Bytes = base64.b64encode(messageBytes)
base64Message = base64Bytes.decode('ascii')


headers['Authorization'] = f"Basic {base64Message}"
data['grant_type'] = "client_credentials"
r = requests.post(url, headers=headers, data=data)
token = r.json()['access_token']

# - Read tracks CSV file

csv_tracks_data = pd.read_csv('originalData/tracks-global-weekly.csv',usecols=[3,4])  # Read file
# print(csv_tracks_data)
N = 10 # top 10
csv_top_tracks_data = csv_tracks_data.head(N)
# print(csv_top_tracks_data)
csv_tracks_list = csv_top_tracks_data.values.tolist()
# print(csv_tracks_list[0][1])
trackStreams = []
trackId = []
for index in range(len(csv_tracks_list)):
    trackStreams.append(csv_tracks_list[index][0])
    trackId.append(csv_tracks_list[index][1][-22:])
# print(trackStreams)
# print(trackId)

# - Get Top Tracks
def get_top_tracks():
    tracksInf = []
    trackImg = []
    trackName = []
    for index in range(len(trackId)):
        atrackId = trackId[index]
        atrackUrl = f"https://api.spotify.com/v1/tracks/{atrackId}"
        headers = {
            "Authorization": "Bearer " + token
        }

        res = requests.get(url=atrackUrl, headers=headers)
        # print(json.dumps(res.json(), indent=2))
        jsonobj = json.loads(res.text)

        trackName.append(jsonobj['name'])
        trackImg.append(jsonobj['album']['images'][0]['url'])

    # print(trackName)
    # print(trackImg)
    tracksInf.append(trackName)
    tracksInf.append(trackImg)
    tracksInf.append(trackStreams)
    # print(tracksInf)

    return(tracksInf)

tracks_Inf = get_top_tracks()

# - Read artists CSV file

csv_artists_data = pd.read_csv('originalData/artists-global-weekly.csv',usecols=[2,3])  # Read file
# print(csv_artists_data)
csv_artists_list = csv_artists_data.values.tolist()
# print(csv_artists_list[0][1])
artistStreams = []
artist_trackId = []
for index in range(len(csv_artists_list)):
    artistStreams.append(csv_artists_list[index][0])
    artist_trackId.append(csv_artists_list[index][1][-22:])
# print(artistStreams)
# print(artist_trackId)

# - Get Artists Id

def get_artists_id():
    artistId = []
    for index in range(len(artist_trackId)):
        atrackId = artist_trackId[index]
        atrackUrl = f"https://api.spotify.com/v1/tracks/{atrackId}"
        headers = {
            "Authorization": "Bearer " + token
        }

        res = requests.get(url=atrackUrl, headers=headers)
            # print(json.dumps(res.json(), indent=2))
        jsonobj = json.loads(res.text)
        artistId.append(jsonobj['artists'][0]['id'])
    return(artistId)

artistsId = get_artists_id()
# print(artists_Id)

# - Get Top Artists

def get_top_artists():
    artistsInf = []
    artistkName = []
    artistImg = []
    for index in range(len(artistsId)):
        aartistId = artistsId[index]
        artistUrl = f"https://api.spotify.com/v1/artists/{aartistId}"
        headers = {
            "Authorization": "Bearer " + token
        }

        res = requests.get(url=artistUrl, headers=headers)
        jsonobj = json.loads(res.text)

        artistkName.append(jsonobj['name'])
        artistImg.append(jsonobj['images'][0]['url'])
    # print(artistkName)
    # print(artistImg)
    artistsInf.append(artistkName)
    artistsInf.append(artistImg)
    artistsInf.append(artistStreams)
    print(artistsInf)

    return(artistsInf)

artists_Inf = get_top_artists()

rank_Inf = ["Top 1","Top 2","Top 3","Top 4","Top 5","Top 6","Top 7","Top 8","Top 9","Top 10"]
value_Inf = [70,50,30,30,21,21,15,15,10,10]
color_Inf = ["#191414","#191414a1","#191414a2","#191414a3","#191414a4","#191414a5","#191414a6","#191414a7","#191414a8","#191414a9"]

d_artists = []
for i in range(10):
    d_artists.append({
    "color": color_Inf[i],
    "rank": rank_Inf[i],
    "id": artists_Inf[0][i],
    "value": value_Inf[i],
    "image": artists_Inf[1][i]
    })

# print(d_artists)

d_tracks = []

for i in range(10):
    d_tracks.append({
    "id": tracks_Inf[0][i],
    "group": tracks_Inf[0][i],
    "value": tracks_Inf[2][i]
    })


json.dump(d_artists, open("data/artists.json","w"),sort_keys=True, indent=4)
json.dump(d_tracks, open("data/tracks.json","w"),sort_keys=True, indent=4)
