import os
import tekore as tk
import time
import csv


client_id = 'a34b4bf0f6c94c1e9a51259a4b1be93a'
client_secret = 'f4714d4912104496a36b4fd9e8039664'

app_token = tk.request_client_token(client_id, client_secret)

spotify = tk.Spotify(app_token)

#artists
playboiCarti = '699OTQXzgjhIYAHMy9RyPD'
jayChou = '2elBjNSdBE2Y3f0j1mjrql'
pheobeBridgers = '1r1uxoy19fzMxunt3ONAkG'
lilUzi = '4O15NlyKLIASxsJ0PrXPfz'
soFaygo = '2SJhf6rTOU53g8yBdAjPby'
poloPerks = '4f4Ee5QjHnoeSdlxTaK6rx'
kanyeWest = '5K4W6rqBFWDnAN6FQUkS6x'
trippieRedd = '6Xgp2XMz1fhVYe7i6yNAax'
macMiller = '4LLpKhyESsyAXpc4laK94U'
frankOcean = '2h93pZq0e7k5yf4dywlkpM'
juiceWrld = '4MCBfE4596Uoi2O4DtmEMz'
xxxTentacion = '15UsOTVnJzReFVN1VCnxy4'
JPEGMafia = '6yJ6QQ3Y5l0s0tn7b0arrO'
travisScott = '0Y5tJX1MQlPlqiwlOH1tJY'
BROCKHAMPTON = '1Bl6wpkWCQ4KVgnASpvzzA'
bernardJabs = '1EBoLDWzc0lpDDIVasJhAv'
youngThug = '50co4Is1HCEo8bhOyUWKpn'
youngNudy = '5yPzzu25VzEk8qrGTLIrE1'
poorStacy = '7vSY9HEreOqb1Llar3UC38'
tylerTheCreator = '4V8LLVI7PbaPR0K2TGSxFF'
jorjaSmith = '1CoZyIx7UvdxT5c8UkMzHd'
Dave = '6Ip8FS7vWT1uKkJSweANQK'
eightEightGLAM = '2I9SLklAOG0vdMiUUMNxRl'
NAV = '7rkW85dBwwrJtlHRDkJDAC'
yungBans = '6WkUZyqghQei2G809wMKuZ'
skiMaskTheSlumpGod = '2rhFzFmezpnW82MNqEKVry'
Future = '1RyvyyTE3xzB2ZywiAwp0i'
elliotSmith = '2ApaG60P4r0yhBoDCGD8YG'
IDK = '6aiFCgyKNwF9Rv5TOxnE8E'
Jaden = '0xOeVMOz2fVg5BJY3N6akT'
kevinAbstract = '07EcmJpfAday8xGkslfanE'
donToliver = '4Gso3d4CscCijv0lmajZWs'
Saba = '7Hjbimq43OgxaBRpFXic4x'
mobbDeep = '6O2zJ0tId7g07yzHtX0yap'
nebuKiniza = '5lCY3tqdQxbeg5igSlObaT'
Stormzy = '2SrSdSvpminqmStGELCSNd'
fumezTheEngineer = '0ksX396B3t2Gt8kwr0BJZk'
ArrDee = '7m0BsF0t3K9WQFgKoPejfk'
fivioForeign = '14CHVeJGrR5xgUGQFV5BVM'
teeGrizzley = '6AUl0ykLLpvTktob97x9hO'
chiefKeef = '15iVAtD3s3FsQR4w1v6M0P'
babyKeem = '5SXuuuRpukkTvsLuUknva1'
madeInTYO = '5SyGEPymt1G2uto47tVWvZ'
popSmoke = '0eDvMgVFoNV3TpwtrVCoTj'
TOBi = '0P54cVemq1DCHUfUMlWAoN'
lilBoom = '1mmlWsyPJvvxMdabcGJjRn'
Feist = '6CWTBjOJK75cTE8Xv8u1kj'
Masego = '3ycxRkcZ67ALN3GQJ57Vig'
Rav = '6oeSQ4qmDQ7n89Rdt6tLLn'
Killval = '1mNl9St7BvqjN0oj5ieIFZ'
lilPeep = '2kCcBybjl3SAtIcwdWpUe3'
lilTracy = '5g63iWaMJ2UrkZMkCC8dMi'
Gunna = '2hlmm7s2ICUX0LVIhVFlZQ'



artistList = [playboiCarti, jayChou, pheobeBridgers, lilUzi, soFaygo, poloPerks, kanyeWest, trippieRedd, macMiller, frankOcean, juiceWrld, xxxTentacion, JPEGMafia, travisScott, BROCKHAMPTON, bernardJabs, youngThug, youngNudy, poorStacy, tylerTheCreator, jorjaSmith, Dave, eightEightGLAM, NAV, yungBans, skiMaskTheSlumpGod, Future, elliotSmith, IDK, Jaden, kevinAbstract, donToliver, Saba, mobbDeep, nebuKiniza, Stormzy, fumezTheEngineer, ArrDee, fivioForeign, teeGrizzley, chiefKeef, babyKeem, madeInTYO, popSmoke, TOBi, lilBoom, Feist, Masego, Rav, Killval, lilPeep, lilTracy, Gunna]


artistName = "Kanye West"
artistListIndex = 6
albums = spotify.artist_albums(artistList[artistListIndex])
numSongs = 0
arrayAlbums = []

#total values
totalTempo = 0
totalAcousticness = 0
totalDanceability = 0
totalDuration = 0
totalEnergy = 0
totalLiveliness = 0
totalLoudness = 0
totalMode = 0
totalSpeechiness = 0
totalPopularity = 0
totalExplicit = 0

#average values
averageTempo = 0
averageAcousticness = 0
averageDanceability = 0
averageDuration = 0
averageEnergy = 0
averageLiveliness = 0
averageLoudness = 0
averageMode = 0
averageSpeechiness = 0
averagePopularity = 0
percentExplicit = 0
for albums in albums.items:
    tempAlbumID = albums.id
    tempAlbum = album = spotify.album(tempAlbumID)


    if (album.artists[0].name == artistName and album.album_type == 'album'):
        arrayAlbums.append(album)


for x in range(0, len(arrayAlbums)):
    loopAlbum = arrayAlbums[x]
    loopTracksList = loopAlbum.tracks.items
    for y in range(0, len(loopTracksList)):
        tempTrack = loopTracksList[y]
        tempTrackID = tempTrack.id
        fullTrack = spotify.track(tempTrackID)
        #value additions
        audioFeatures = (spotify.track_audio_features(tempTrackID))
        totalTempo += audioFeatures.tempo
        totalAcousticness += audioFeatures.acousticness
        totalDanceability += audioFeatures.danceability
        totalDuration += audioFeatures.duration_ms
        totalEnergy += audioFeatures.energy
        totalLiveliness += audioFeatures.liveness
        totalLoudness += audioFeatures.loudness
        totalMode += audioFeatures.mode
        totalSpeechiness += audioFeatures.speechiness
        totalPopularity += fullTrack.popularity
        if(fullTrack.explicit == True):
            totalExplicit += 1
        numSongs = numSongs + 1

    time.sleep(3)

print(artistName + " has " + str(numSongs) + " songs in total")

artist = spotify.artist(artistList[artistListIndex])
numFollowers = artist.followers.total
print(artistName + " has " + str(numFollowers) + " spotify followers")

averageTempo = round(totalTempo/numSongs, 3)
print(artistName + " average tempo is " + str(averageTempo))

averageAcousticness = round(totalAcousticness/numSongs, 3)
print(artistName + " average acousticness is " + str(averageAcousticness))

averageDanceability = round(totalDanceability/numSongs, 3)
print(artistName + " average danceability is " + str(averageDanceability))

averageDuration = round(totalDuration/numSongs, 3)
print(artistName + " average duration is " + str(averageDuration) + " ms")

averageEnergy = round(totalEnergy/numSongs, 3)
print(artistName + " average energy is " + str(averageEnergy))

averageLiveliness = round(totalLiveliness/numSongs, 3)
print(artistName + " average liveliness is " + str(averageLiveliness))

averageLoudness = round(totalLoudness/numSongs, 3)
print(artistName + " average loudness is " + str(averageLoudness) + " db")

averageMode = round(totalMode/numSongs, 3)
print(artistName + " average mode is " + str(averageMode))

averageSpeechiness = round(totalSpeechiness/numSongs, 3)
print(artistName + " average speechiness is " + str(averageSpeechiness))

averagePopularity = round(totalPopularity/numSongs, 3)
print(artistName + " average popularity is " + str(averagePopularity))

percentExplicit = round(totalExplicit/numSongs, 4)
print(artistName + " percent explicit songs is " + str(percentExplicit*100) + "%")


valueList = [numSongs, numFollowers, averageTempo, averageAcousticness, averageDanceability, averageDuration, averageEnergy, averageLiveliness, averageLoudness, averageMode, averageSpeechiness, averagePopularity, percentExplicit]
with open('../Code/' + artistName + '.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(valueList)








