
import random
import tekore as tk
import time
from tqdm import tqdm
import numpy as np
from sklearn.cluster import KMeans

#Authentication Values
client_id = 'dcda589399b14d69a499ae046c464bee'
client_secret = '7daada75b6fd4847a5e80af33e0b7b59'
URI = 'http://localhost:8888/callback'

#User Authorization Process
#Return and authentication token
def authenticateUser():
    valid = False
    conf = (client_id, client_secret, URI)
    scope = tk.scope.user_top_read
    #token = tk.prompt_for_user_token(*conf, scope=tk.scope.every)

#Only accetp valid URI for authentication
    result = False
    while not result:
        try:
            token = tk.prompt_for_user_token(*conf, scope=tk.scope.every)
            result = True
        except KeyError as e:
            print("Please enter a valid URL")

    # other code that uses result but is not involved in getting it

    return tk.Spotify(token)

#User Top Tracks
def getTop50Tracks(token):
    topTracksPagingList = token.current_user_top_tracks(time_range='medium_term', limit=100, offset=0)
    topTracksItemList = topTracksPagingList.items
    return topTracksItemList

#Return a pool of songs the user might enjoy
#Iterate through top 10 songs of artists that have collaborated with artists within user's top 50 songs
def generateSongPool(token, topTracks):
    length1 = len(topTracks)
    songPool = []
    layer1TrackList = []
    layer2TrackList = []
    #Loop through each track in top 50 tracks
    x = 0
    loadCount = 0
    pbar = tqdm(total=length1, position=0, leave=True, desc="Generating song pool step 1")  #loading bar
    #Loop through top tracks and isolate top songs of collaborative artists in top tracks
    for track in topTracks:
        pbar.update(n=1)  # Increments counter for loading bar
        time.sleep(.005)
        if(len(track.artists) > 1):
            time.sleep(.005)
            artistList = track.artists
            for artist in artistList[1:]:
                artistID = artist.id
                top10TrackList = token.artist_top_tracks(artistID, 'US')
                for track in top10TrackList:
                    if track not in songPool:
                        step = random.randrange(1, 10)
                        #Shortens Final Song List
                        if(x % step == 0):
                            songPool.append(track)
                            layer1TrackList.append(track)
                            loadCount += 1
                        x += 1

    #Loop through tracks in layer 1 tracks to find tracks of artist collaborators
    x = 0
    loadCount = 0
    length2 = len(layer1TrackList)
    pbar = tqdm(total=length2, position=0, leave=True, desc="Generating song pool step 2")  # loading bar
    for track in layer1TrackList:
        pbar.update(n=1)  # Increments counter for loading bar
        time.sleep(.005)
        if(len(track.artists) > 1):
            time.sleep(.005)
            artistList = track.artists
            for artist in artistList[1:]:
                artistID = artist.id
                top10TrackList = token.artist_top_tracks(artistID, 'US')
                for track in top10TrackList:
                    if track not in songPool:
                        step = random.randrange(1, 10)
                        #Shortens final song list
                        if(x % step == 0):
                            songPool.append(track)
                            layer2TrackList.append(track)
                            loadCount += 1
                        x += 1

  #Loop through tracks in layer 2 tracks to find tracks of artist collaborator's collaborators
    x = 0
    loadCount = 0
    length3 = len(layer2TrackList)
    pbar = tqdm(total=length3, position=0, leave=True, desc="Generating song pool step 3")  # loading bar
    for track in layer2TrackList:
        pbar.update(n=1)  # Increments counter for loading bar
        time.sleep(.005)
        if(len(track.artists) > 1):
            time.sleep(.005)
            artistList = track.artists
            for artist in artistList[1:]:
                artistID = artist.id
                top10TrackList = token.artist_top_tracks(artistID, 'US')
                for track in top10TrackList:
                    if track not in songPool:
                        step = random.randrange(1, 10)
                        #Shortens final song list
                        if(x % step == 0):
                            songPool.append(track)
                            loadCount += 1
                        x += 1
    print("size of song reccomendation pool is " + str(len(songPool)))

    #Add top songs to end of song pool
    for track in topTracks:
        songPool.append(track)

    return songPool

#Break period to comply with API rate limit
def coolDown():
    for i in tqdm(range(0, 100), desc="Cooling down to comply with API rate limit"):
        time.sleep(.1)
    print("Continuing operations")

#Get an array of audio features for each song
def audioFeatureCompiler(token, songPool):
    print("Compiling audio features...")
    length = len(songPool)
    audioFeatureArray = []
    loadCount = 0
    index = 0
    pbar = tqdm(total=length, desc="Compiling audio features")  #loading bar
    for track in songPool:
        pbar.update(n=1)  # Increments counter for loading bar
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
        time.sleep(.05)

    audioFeatureArray = np.array(audioFeatureArray)
    return audioFeatureArray

#Cluster audio feature array by audio feature
def clusterSongs(token, audioFeatureArray, numCategories):
    print("Clustering songs...")
    audioFeatureArrayWithClusters = []
    k = numCategories
    km = KMeans(n_clusters=k).fit(audioFeatureArray)
    labels = km.labels_
    labels = np.array(labels)

    for x in range(len(audioFeatureArray)):
        cluster = int(labels[x])
        tempArray = audioFeatureArray[x]
        tempArray = np.append(tempArray, cluster)
        audioFeatureArrayWithClusters.append(tempArray)

    return audioFeatureArrayWithClusters


#Get the cluster that most of the user's top songs belong to
def getDominantCluster(audioFeatureArrayWithClusters, topTracks):
    print("Organizing song clusters...")
    counter = 0
    clusterArray = []

    for x in range(len(audioFeatureArrayWithClusters) - len(topTracks)):
        clusterArray.append(int(audioFeatureArrayWithClusters[x][5]))

    clusterArray = np.array(clusterArray)

    targetCluster = np.bincount(clusterArray).argmax()
    return targetCluster

#Return the songs in the cluster labeled as the dominant cluster
def returnRecommendedSongs(targetCluster, audioFeatureArrayWithClusters, songPool, topTracks):
    i = 0
    songPoolDictionary = {}
    recommendedSongNameList = []
    recommendedSongTrackList = []


    for x in range(len(audioFeatureArrayWithClusters)):
        songName = str(songPool[x].name)
        songPoolDictionary[songName] = audioFeatureArrayWithClusters[x]

    for x in songPoolDictionary:
        i += 1
        tempArray = songPoolDictionary[x]
        if(tempArray[5] == targetCluster):
            recommendedSongNameList.append(x)
            recommendedSongTrackList.append(songPool[i])

        if(x == len(songPool) - len(topTracks)):
            print(recommendedSongTrackList)
            return recommendedSongNameList, recommendedSongTrackList

    return recommendedSongNameList, recommendedSongTrackList

#Generate a playlist in the user's Spotify profile
def generatePlaylist(token, recommendedSongTrackList):
    #Max of 100 songs allowed to add to playlist
    songCap = 0
    user = token.current_user()
    userID = user.id
    uriList = []
    #Fill list of URIs
    for track in recommendedSongTrackList:
        if(songCap < 100):
            uriList.append(track.uri)
        songCap +=1

    playlistName = input("Enter the name of your new playlist:  ")
    newPlaylist = token.playlist_create(userID, playlistName, public=True, description="A playlist generated by a Spotify recommendation program for ATCS 2022. Program by Iyanu")
    playlistID = newPlaylist.id
    token.playlist_add(playlistID, uriList, position=None)
    print("Playlist generated! Open Spotify and enjoy your new music!")
    exit()



#Main method
def main():
    print("Once terms are accepted, paste URL of localhost failure page into field requesting redirect URL")
    spotifyToken = authenticateUser()
    userCmd = input("what would you like a reccomendation for? (enter 'song' or 'artist'): ")
    while(userCmd != 'song' and userCmd != 'artist'):
        userCmd = input("what would you like a reccomendation for? (enter 'song' or 'artist'): ")
    if(userCmd == 'song'):
        topTracks = getTop50Tracks(spotifyToken)
        testPool = topTracks + topTracks
        songPool = generateSongPool(spotifyToken, topTracks)
        coolDown()
        audioFeatureArray = audioFeatureCompiler(spotifyToken, songPool)
        audioFeatureArrayWithClusters = clusterSongs(spotifyToken, audioFeatureArray, 5)
        targetCluster = getDominantCluster(audioFeatureArrayWithClusters, topTracks)
        recommendedSongNameList, recommendedSongTrackList = returnRecommendedSongs(targetCluster, audioFeatureArrayWithClusters, songPool, topTracks)

        print("Would you like to print the names of the recommended songs or make a playlist out of them?  ")
        userCmd = input("Type 'list' for a printed list or 'playlist' to have a playlist added to your spotify account:  ")
        while (userCmd != 'list' and userCmd != 'playlist'):
            userCmd = input("Type 'list' for a printed list or 'playlist' to have a playlist added to your spotify account:  ")
        if(userCmd == 'list'):
            for track in recommendedSongNameList:
                print(track)
        elif(userCmd == "playlist"):
            for track in recommendedSongTrackList:
                generatePlaylist(spotifyToken, recommendedSongTrackList)

main()

