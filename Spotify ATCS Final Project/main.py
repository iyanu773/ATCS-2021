import os
import random
import sys
import tekore
import tekore as tk
import time
import csv
from tqdm import tqdm
from random import uniform
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.cluster import KMeans


client_id = 'dcda589399b14d69a499ae046c464bee'
client_secret = '7daada75b6fd4847a5e80af33e0b7b59'
URI = 'http://localhost:8000'

#User Authorization Process
#Return and authentication token
def authenticateUser():
    conf = (client_id, client_secret, URI)
    scope = tk.scope.user_top_read
    token = tk.prompt_for_user_token(*conf, scope=tk.scope.every)
    return tk.Spotify(token)

#User Top Tracks
def getTop50Tracks(token):
    topTracksPagingList = token.current_user_top_tracks(time_range='medium_term', limit=100, offset=0)
    topTracksItemList = topTracksPagingList.items
    return topTracksItemList

#Return a pool of songs the user might enjoy
#Iterate through top 10 songs of artists that have collaborated with artists within user's top 50 songs
def generateSongPool(token, topTracks):
    songPool = []
    layer1TrackList = []
    layer2TrackList = []
    #Loop through each track in top 50 tracks
    x = 0
    for track in topTracks:
        if(len(track.artists) > 1):
            artistList = track.artists
            for artist in artistList[1:]:
                artistID = artist.id
                top10TrackList = token.artist_top_tracks(artistID, 'US')
                for track in top10TrackList:
                    if track not in songPool:
                        step = random.randrange(1, 3)
                        #Shortens Final Song List
                        if(x % step == 0):
                            songPool.append(track)
                            layer1TrackList.append(track)
                        x += 1

    #Loop through tracks in layer 1 tracks to find tracks of artist collaborators
    x = 0
    for track in layer1TrackList:
        time.sleep(.01)
        if(len(track.artists) > 1):
            artistList = track.artists
            for artist in artistList[1:]:
                artistID = artist.id
                top10TrackList = token.artist_top_tracks(artistID, 'US')
                for track in top10TrackList:
                    if track not in songPool:
                        step = random.randrange(1, 3)
                        #Shortens final song list
                        if(x % step == 0):
                            songPool.append(track)
                            layer2TrackList.append(track)
                        x += 1

  #Loop through tracks in layer 2 tracks to find tracks of artist collaborator's collaborators
    x = 0
    for track in layer2TrackList:
        time.sleep(.01)
        if(len(track.artists) > 1):
            artistList = track.artists
            for artist in artistList[1:]:
                artistID = artist.id
                top10TrackList = token.artist_top_tracks(artistID, 'US')
                for track in top10TrackList:
                    if track not in songPool:
                        step = random.randrange(1, 4)
                        #Shortens final song list
                        if(x % step == 0):
                            songPool.append(track)
                        x += 1
    loading = False
    return songPool

#Get the most defining audio features
def audioFeatureCompiler(token, songPool):
    audioFeaureArray = []

    index = 0
    print("here")
    for track in songPool:
        audioFeatures = (token.track_audio_features(track.id))

        acousticness = audioFeatures.acousticness
        danceability = audioFeatures.danceability
        energy = audioFeatures.energy
        liveliness = audioFeatures.liveness
        mode = audioFeatures.mode
        speechiness = audioFeatures.speechiness

        audioFeaureArray.append([acousticness, danceability, energy, liveliness, mode, speechiness])

        index += 1

    for x in audioFeaureArray:
        print(x)



#Main method
def main():
    print("Once terms are accepted, paste URL of localhost failure page into field requesting redirect URL")
    spotifyToken = authenticateUser()
    userCmd = input("what would you like a reccomendation for? (enter 'song' or 'artist'): ")
    if(userCmd == 'song'):
        topTracks = getTop50Tracks(spotifyToken)
        testPool = topTracks
        songPool = generateSongPool(spotifyToken, topTracks)
        audioFeatureCompiler(spotifyToken, songPool)



main()



