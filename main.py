import requests
from bs4 import BeautifulSoup
import sys
import re

def checkStatus(url):
    res = requests.get(url)
    if res.status_code != 200:
        return False
    return True

def turnToSoup(url):
    res = requests.get(url)
    content = res.text
    soup = BeautifulSoup(content,'lxml')
    return soup

def getUserInput():
    songTitle = input('Enter Song Title:\n').replace(' ', '-').replace('&','and')
    songTitle = re.sub(r'[^a-zA-Z-\d]',"",songTitle)
    artist = input("Enter Artist:\n").replace(' ', '-')
    artist = re.sub(r'[^a-zA-Z-\d]',"",artist)

    return artist, songTitle

def checkArtistExists(artist):
    if not checkStatus(f'https://genius.com/artists/{artist}'):
        print("Sorry we couldn't find that artist.")
        return False

    return True

def getLyrics(artist, songTitle):
    if not checkStatus(f'https://genius.com/{artist}-{songTitle}-lyrics'):
        print(f"\nSorry, we couldn't find any lyrics for - {songTitle}")
    else:
        soup = turnToSoup(f'https://genius.com/{artist}-{songTitle}-lyrics')
        lyrics = soup.find('p').text
        print(f"\nHere are your lyrics for {songTitle.title().replace('-',' ')} by {artist.replace('-',' ').title()}:\n\n{lyrics}")

def main():
    artist, songTitle = getUserInput()
    if not checkArtistExists(artist):
        sys.exit()
    getLyrics(artist, songTitle)
    
main()
