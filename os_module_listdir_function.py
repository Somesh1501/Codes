#! python3
# os module
import os
#listdir function gives us list of element containing in a folder
MusicPath = (r"F:\Music")
MusicSongs = (os.listdir(MusicPath))

Music2Path = (r"E:\some")
Music2Songs = (os.listdir(Music2Path))

for song in MusicSongs:
    if song in Music2Songs:
        commonSong = os.path.join(Music2Path , song)#join folder path & songs path
        os.remove(commonSong)#remove common element
