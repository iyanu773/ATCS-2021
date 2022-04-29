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
    loadCount = 0
    for track in topTracks:
        time.sleep(.01)
        if(len(track.artists) > 1):
            time.sleep(.01)
            artistList = track.artists
            for artist in artistList[1:]:
                artistID = artist.id
                top10TrackList = token.artist_top_tracks(artistID, 'US')
                for track in top10TrackList:
                    if track not in songPool:
                        step = random.randrange(1, 6)
                        #Shortens Final Song List
                        if(x % step == 0):
                            #Simple loading screen process
                            if(loadCount % 2 == 0):
                                sys.stdout.write('\rloading / ')
                            else:
                                sys.stdout.write('\rloading \ ')
                            songPool.append(track)
                            layer1TrackList.append(track)
                            loadCount += 1
                        x += 1

    #Loop through tracks in layer 1 tracks to find tracks of artist collaborators
    x = 0
    loadCount = 0
    for track in layer1TrackList:
        time.sleep(.01)
        if(len(track.artists) > 1):
            time.sleep(.01)
            artistList = track.artists
            for artist in artistList[1:]:
                artistID = artist.id
                top10TrackList = token.artist_top_tracks(artistID, 'US')
                for track in top10TrackList:
                    if track not in songPool:
                        step = random.randrange(1, 6)
                        #Shortens final song list
                        if(x % step == 0):
                            # Simple loading screen process
                            if (loadCount % 2 == 0):
                                sys.stdout.write('\rloading / ')
                            else:
                                sys.stdout.write('\rloading \ ')
                            songPool.append(track)
                            layer2TrackList.append(track)
                            loadCount += 1
                        x += 1

  #Loop through tracks in layer 2 tracks to find tracks of artist collaborator's collaborators
    x = 0
    loadCount = 0
    for track in layer2TrackList:
        time.sleep(.01)
        if(len(track.artists) > 1):
            time.sleep(.01)
            artistList = track.artists
            for artist in artistList[1:]:
                artistID = artist.id
                top10TrackList = token.artist_top_tracks(artistID, 'US')
                for track in top10TrackList:
                    if track not in songPool:
                        step = random.randrange(1, 6)
                        #Shortens final song list
                        if(x % step == 0):
                            # Simple loading screen process
                            if (loadCount % 2 == 0):
                                sys.stdout.write('\rloading / ')
                            else:
                                sys.stdout.write('\rloading \ ')
                            songPool.append(track)
                            loadCount += 1
                        x += 1
    print("size of song reccomendation pool is " + str(len(songPool)))
    return songPool

#Break period to comply with API rate limit
def coolDown():
    for i in tqdm(range(0, 100), desc="Cooling down to comply with API rate limit"):
        time.sleep(.1)
    print("Continuing operations")

#Get the most defining audio features
def audioFeatureCompiler(token, songPool):
    audioFeatureArray = []
    loadCount = 0
    index = 0
    for track in songPool:
        # Simple loading screen process
        if (loadCount % 2 == 0):
            sys.stdout.write('\rloading / ')
        else:
            sys.stdout.write('\rloading \ ')

        audioFeatures = (token.track_audio_features(track.id))
        acousticness = float(audioFeatures.acousticness)
        danceability = float(audioFeatures.danceability)
        energy = float(audioFeatures.energy)
        liveliness = float(audioFeatures.liveness)
        speechiness = float(audioFeatures.speechiness)

        tempArray = [acousticness, danceability, energy, liveliness, speechiness]
        audioFeatureArray.append(tempArray)

        index += 1
        loadCount += 1
        time.sleep(.03)

    audioFeatureArray = np.array(audioFeatureArray)
    return audioFeatureArray

def clusterSongs(token, audioFeatureArray, numCategories):
    k = numCategories
    km = KMeans(n_clusters=k).fit(audioFeatureArray)
    labels = km.labels_
    labels = np.array(labels)
    for x in range(len(audioFeatureArray)):
        cluster = int(labels[x])
        np.append(audioFeatureArray[x], cluster)

    for x in audioFeatureArray:
        print(x)

#Main method
def main():
    print("Once terms are accepted, paste URL of localhost failure page into field requesting redirect URL")
    spotifyToken = authenticateUser()
    userCmd = input("what would you like a reccomendation for? (enter 'song' or 'artist'): ")
    if(userCmd == 'song'):
        topTracks = getTop50Tracks(spotifyToken)
        testPool = topTracks
        #songPool = generateSongPool(spotifyToken, topTracks)
        #coolDown()
        audioFeatureArray = audioFeatureCompiler(spotifyToken, testPool)
        clusterSongs(spotifyToken, audioFeatureArray, 5)

main()



