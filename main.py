#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pip install pytube
# pip install nuitka
# Windows
# pip install pyinstaller pywin32 pywin32-ctypes
# Linux
# pip install altgraph pyinstaller pyinstaller-hooks-contrib
#
# Linux: PyQT5 PyQT5-sip PyQT5-QT PyQT5-QT5 PyQT6 PyQT6-sip PyQT6-QT
# Windows: PyQT5 PyQT5-sip PyQT6 PyQT6-sip
#
# nuitka3 hello.py
# pyinstaller hello.py
# --onefile — сборка в один файл, т.е. файлы .dll не пишутся.
# --windowed -при запуске приложения, будет появляться консоль.
# --noconsole — при запуске приложения, консоль появляться не будет.
# --icon=app.ico — добавляем иконку в окно.
# --paths — возможность вручную прописать путь к необходимым файлам, если pyinstaller
# не может их найти(например: --paths D:\python35\Lib\site-packages\PyQt5\Qt\bin)
# pyinstaller --onefile --icon=name.ico --noconsole myscript.py
# 

import re
import pathlib
import pytube

Quality = ''
isVideoCount = ''
onVideo = []
fileLogs = str(pathlib.Path(pathlib.Path.cwd()).resolve().joinpath("logs.txt"))

def on_progress(stream, chunk, bytes_remaining):
	global isVideoCount
	global onVideo
	global fileLogs
	total_size = stream.filesize
	bytes_downloaded = total_size - bytes_remaining
	percentage_of_completion = round(bytes_downloaded / total_size * 100)
	if percentage_of_completion == 100:
		print(f"{percentage_of_completion}%\t{isVideoCount}\t[OK]")
	elif percentage_of_completion < 100 and percentage_of_completion > 0:
		print(f"{percentage_of_completion}%\t{isVideoCount}")
	else:
		print(f"Download video {onVideo[0]} ERROR!")
		with open(fileLogs, 'a') as f:
			f.write(onVideo[0])
			f.write(onVideo[1])
			f.write(onVideo[2])

def filterName(innames: str) -> str:
	outname = str(innames).replace('|', '.').replace('%', '.').replace(':', '.').replace('"', '.').replace("'", ".").replace('<', '.').replace('>', '.')\
	.replace('[', '.').replace(']', '.').replace('{', '.').replace('}', '.').replace('#', '.').replace('$', '.').replace('?', '.')\
	.replace('`', '.').replace('~', '.').replace('@', '.').replace('!', '.').replace('&', '.').replace('^', '.').replace('*', '.')
	pattern = r'(.)\1+'
	repl = r'\1'
	return re.sub(pattern,repl,outname).strip()

def getTitle(urlFile: str) -> str:
	global Quality
	yt = pytube.YouTube(urlFile)
	Quality = yt.streams.get_highest_resolution().resolution
	outname = filterName(yt.title) + '_' + Quality + '.mp4'
	return outname

def downloadYouTube(urlFile: str, onPath: str = None, FName: str = None):
	yt = pytube.YouTube(urlFile, on_progress_callback=on_progress)
	yt = yt.streams.get_highest_resolution()
	yt.download(output_path=onPath, filename=FName)

def downloadPlayList(link: str, inPath: str):
	global isVideoCount
	global onVideo
	global Quality
	playlist = pytube.Playlist(link)
	all_count = str(len(playlist.video_urls))
	#all_count = len(playlist.video_urls)
	print('Number of videos in playlist: %s' % all_count)
	download_path = str(pathlib.Path(inPath).resolve())
	if not pathlib.Path(download_path).exists():
		pathlib.Path(download_path).mkdir(parents=True, exist_ok=True)
	video_url = []
	for url in playlist.video_urls:
		video_url.append(url)
	index = 1
	for onURL in video_url:
		fname = str(index) + '.' + getTitle(onURL)
		isVideoCount = f"{index}/{all_count}\t{Quality}"
		onVideo.clear()
		onVideo+=[fname]
		onVideo+=[link]
		onVideo.append(isVideoCount)
		print(f"{fname}\n{isVideoCount}")
		downloadYouTube(onURL, download_path, fname)
		index+=1

def downloadVideo(link: str, inPath: str):
	global onVideo
	download_path = str(pathlib.Path(inPath).resolve())
	if not pathlib.Path(download_path).exists():
		pathlib.Path(download_path).mkdir(parents=True, exist_ok=True)
	fname = getTitle(link)
	onVideo.clear()
	onVideo+=[fname]
	onVideo+=[link]
	onVideo.append(f"1/1\t{Quality}")
	print(fname)
	downloadYouTube(link, download_path, fname)

def main():
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
	# test
	#url = 'https://www.youtube.com/watch?v=V3h2iq2mylI&list=PLlWXhlUMyoobAlP3mZ0_uuJagsDSg_5YT&index=2'
	#url = 'https://www.youtube.com/playlist?list=PLlWXhlUMyoobAlP3mZ0_uuJagsDSg_5YT'
	#folder = '/home/mikl/003/'
	# print(getTitle(url))
	#downloadVideo(url, folder)
	#downloadPlayList(url, folder)

if __name__ == '__main__':
    main()
