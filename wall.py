import os
import requests
import wget
import subprocess
import time
import ctypes
SPI_SETDESKWALLPAPER = 20


def get_wallpaper(query):
    access_key = 'K7r6MdenUXTqJzFwiogTUWQqEi9Y_4brWKg41yYIr64' # add your unspash api key here
    url = 'https://api.unsplash.com/photos/random?client_id=' + access_key
    params = {
        'query': query,
        'orientation': 'landscape'
    }
    response = requests.get(url, params=params).json()
    image_source = response['urls']['full']

    image = wget.download(image_source, 'F:/Wallpapers/wallpaper.jpg') # add the path here
    return image

def change_wallpaper(query):
    print('This App is Made by Tushar Agrawal\n')
    wallpaper = get_wallpaper(query)
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, wallpaper , 0) # add the path  here as well

def main():
    print('Please wait your wallpaper will be downloaded and applied \n')
    try:
        query = input('what kind of wallpaper do you want ?\n')
        change_wallpaper(query)
    except e:
        print(e)
if __name__ == "__main__":
    main()
    input("Press enter to exit ;)")
