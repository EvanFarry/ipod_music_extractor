# python 3.4
#-------------------------------------------------------------------------------
# author : evan farry
# date   : july 2018
# what?  : simple script to move music files into appropriatly named folders.
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# Thanks!
# Tom Wallroth for the TinyTag Library - https://github.com/devsnd/tinytag
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

from tinytag import TinyTag
import os
import shutil

def main(music_folder):

    #key : 'lake-street-dive'
    #val : 'Lake Street Dive'
    artistDictionary = {}
    targetDirectory = '/Users/evan/Music/ipod_copy/_artists/'

    for subdir, dirs, files in os.walk(music_folder):
        for filename in files:
            if filename.endswith('.mp3') or filename.endswith('.m4a'):

                #get tag for files
                tag = TinyTag.get(os.path.join(subdir, filename))

                #clean artist name for use as directory and dictionary name
                artistFolder = str(tag.artist).lower().replace(' ', '-').replace('.', '').replace('/', '-')

                if artistFolder in artistDictionary:
                    pass #Ive already seen this artist already. carry on.
                else:
                    #this is a new artist! -> add to dictionary -> make new folder.
                    artistDictionary[artistFolder] = str(tag.artist)

                    #make a new empty folder named after this artist.
                    newFolder = targetDirectory + artistFolder
                    if os.path.exists(newFolder):
                        pass #I've already made an empty folder
                    else:
                        os.mkdir(newFolder)

                #move mp3 or m4a file into new folder
                moveFrom = os.path.join(subdir, filename)
                moveTo = targetDirectory + artistFolder

                #move
                shutil.move(moveFrom, moveTo)
#-------------------------------------------------------------------------------

#ipod_dir = '/Users/evan/Music/ipod_copy/Music'
#main(ipod_dir)
