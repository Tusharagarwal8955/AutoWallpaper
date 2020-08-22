import os
import requests
import wget
import subprocess
import time
import ctypes
SPI_SETDESKWALLPAPER = 20


def get_wallpaper():
	access_key = 'K7r6MdenUXTqJzFwiogTUWQqEi9Y_4brWKg41yYIr64' # add your unspash api key here
	url = 'https://api.unsplash.com/photos/random?client_id=' + access_key
	params = {
		'query': 'HD wallpapers',
		'orientation': 'landscape'
	}

	response = requests.get(url, params=params).json()
	image_source = response['urls']['full']

	image = wget.download(image_source, 'F:/Wallpapers/wallpaper.jpg') # add the path here
	return image

def change_wallpaper():
	wallpaper = get_wallpaper()
	ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, wallpaper , 0) # add the path  here as well

def main():
	print('Your wallpaper will be downloaded and applied ')
	try:
		change_wallpaper()
		print('Made by Tushar Agrawal')
	except e:
		print(e)
if __name__ == "__main__":
	main()
