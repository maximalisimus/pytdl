#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pip install pytube
# pip install nuitka
# nuitka3 hello.py

import pathlib
import pytube

video_size = {1: '240p',
			2: '360p',
			3: '480p',
			4: '720p',
			5: '1024p'}

def on_progress(stream, chunk, bytes_remaining):
	total_size = stream.filesize
	bytes_downloaded = total_size - bytes_remaining
	percentage_of_completion = round(bytes_downloaded / total_size * 100)
	if percentage_of_completion == 100:
		print(f"{percentage_of_completion}%\t\t[OK]")
	elif percentage_of_completion < 100 and percentage_of_completion > 0:
		print(f"{percentage_of_completion}% ...")
	else:
		print(f"{percentage_of_completion}%\t\t[ERROR]")

def filterName(innames: str) -> str:
	outname = str(innames).replace('|', '.').replace('%', '.').replace(':', '.').replace('"', '.').replace("'", ".").replace('<', '.').replace('>', '.')\
	.replace('[', '.').replace(']', '.').replace('{', '.').replace('}', '.').replace('#', '.').replace('$', '.').replace('?', '.')\
	.replace('`', '.').replace('~', '.').replace('@', '.').replace('!', '.').replace('&', '.').replace('^', '.').replace('*', '.')
	return outname

def getTitle(urlFile: str) -> str:
	yt = pytube.YouTube(urlFile)
	outname = filterName(yt.title) + '.mp4'
	return outname

def downloadYouTube(urlFile: str, yourPath: str = None, FName: str = None, quality: str = '720p'):
	yt = pytube.YouTube(urlFile, on_progress_callback=on_progress)
	if quality != 'Undefened':
		yt = yt.streams.filter(progressive=True, mime_type="video/mp4", res=quality).first()
	else:
		yt = yt.streams.filter(progressive=True, mime_type="video/mp4", res='720p').first()
	yt.download(output_path=yourPath, filename=FName)

def downloadPlayList(link: str, fullPath: str, size_count: str):
	global video_size
	playlist = pytube.Playlist(link)
	all_count = str(len(playlist.video_urls))
	#all_count = len(playlist.video_urls)
	print('Number of videos in playlist: %s' % all_count)
	download_path = str(pathlib.Path(fullPath).resolve())
	if not pathlib.Path(download_path).exists():
		pathlib.Path(download_path).mkdir(parents=True, exist_ok=True)
	video_url = []
	for url in playlist.video_urls:
		video_url.append(url)
	index = 1
	for onURL in video_url:
		fname = str(index) + '.' + getTitle(onURL)
		print(f"{fname}\n{index}/{all_count}")
		downloadYouTube(onURL, download_path, fname, size_count)
		index+=1

def downloadVideo(link: str, fullPath: str, size_count: str):
	global video_size
	download_path = str(pathlib.Path(fullPath).resolve())
	if not pathlib.Path(download_path).exists():
		pathlib.Path(download_path).mkdir(parents=True, exist_ok=True)
	fname = getTitle(link)
	print(fname)
	downloadYouTube(link, download_path, fname, size_count)

def main():
	'''
	playlist = pytube.Playlist('playlist-url')
	all_count = str(len(playlist.video_urls))
	print('Number of videos in playlist: %s' % len(playlist.video_urls))
	'''
	'''
	with open('selfedu.txt', 'w') as the_file:
		index=1
		for url in playlist.video_urls:
			the_file.write(str(index))
			the_file.write(' ')
			the_file.write(url)
			the_file.write('\n')
			index+=1
	'''
	'''
	download_path = str(pathlib.Path(pathlib.Path.cwd()).resolve().joinpath("download-folder-1024p"))
	if not pathlib.Path(download_path).exists():
		pathlib.Path(download_path).mkdir(parents=True, exist_ok=True)
	video_url = [] 
	for url in playlist.video_urls:
		video_url.append(url)
	#video_link = 'video-url'
	#index = 1
	#fname = str(index) + '.' + getTitle(video_link)
	#downloadYouTube(video_link, download_path, fname)
	#yt = pytube.YouTube(video_link, on_progress_callback=on_progress)
	#yt = yt.streams.filter(progressive=True, mime_type="video/mp4", res="720p").order_by('resolution').desc().first()
	#yt = yt.streams.filter(progressive=True, mime_type="video/mp4", res="720p").first() # fps="24fps"
	#yt.download(download_path)
	#print(yt.streams)
	#titles = filterName(yt.title)
	#print(titles)
	index = 1
	for onURL in video_url:
		fname = str(index) + '.' + getTitle(onURL)
		print(fname, all_count)
		downloadYouTube(onURL, download_path, fname, '1024p')
		index+=1
	'''

if __name__ == '__main__':
    main()

'''
In this method you can download the available highest resolution video.
С помощью этого метода вы можете загрузить доступное видео с самым высоким разрешением.

video = YouTube('mylink')
highresvid = video.streams.get_highest_resolution()
highresvid.download('location')




def downloadYouTube(URLLink: str, yourPath: str, fName: str, quality: str):
	global video_size
	yt = pytube.YouTube(URLLink, on_progress_callback=on_progress)

	if switch(quality) == 1: yt.streams.filter(progressive=True, mime_type="video/mp4", res="240p").first()
	if switch(quality) == 2: yt.streams.filter(progressive=True, mime_type="video/mp4", res="360p").first()
	if switch(quality) == 3: yt.streams.filter(progressive=True, mime_type="video/mp4", res="480p").first()
	if switch(quality) == 4: yt.streams.filter(progressive=True, mime_type="video/mp4", res="720p").first()
	if switch(quality) == 5: yt.streams.filter(progressive=True, mime_type="video/mp4", res="1024p").first()
	if switch(quality) == None: yt.streams.filter(progressive=True, mime_type="video/mp4", res="720p").first()

	yt.streams.filter(progressive=True, mime_type="video/mp4", res="720p").first()
	yt.download(output_path=yourPath, filename=fName)

def switch(case):
	return {
		"240p": 1,
		"360p": 2,
		"480p": 3,
		"720p": 4,
		"1024p": 5
	}.get(case, None)
'''
