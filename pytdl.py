#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import pathlib
import pytube

class PyTDL(object):
	"""pytube control class"""
	fileLogs = str(pathlib.Path(pathlib.Path.cwd()).resolve().joinpath("logs.txt"))
	
	Quality = ''
	isVideoCount = ''
	onVideo = []
	video_url = []

	def __init__(self, link: str, loadDir: str = '', playListFile: str = '', 
				isPlayList: bool = False, SaveInfo: bool = False, SaveURL: bool = False, SaveIndex: bool = False, SaveName: bool = False):
		self.url = link
		self.isPlayList = isPlayList
		if loadDir == '':
			self.loadDir = str(pathlib.Path(pathlib.Path.cwd()).resolve())
		else:
			self.loadDir = 	loadDir
		if playListFile == '':
			self.plFile = str(pathlib.Path(pathlib.Path.cwd()).resolve().joinpath("playlist.txt"))
		else:
			self.plFile = playListFile
		self.isSaveInfo = SaveInfo
		self.isSaveURL = SaveURL
		self.isSaveIndex = SaveIndex
		self.isSaveName = SaveName

	

if __name__ == '__main__':
	pass
