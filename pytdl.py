#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import pathlib
import pytube

class Files:
	
	@staticmethod
	def getRealPath(pathname):
		return str(pathlib.Path(pathname).resolve())

	@staticmethod
	def checkPath(onPath: str):
		downloadpath = Files.getRealPath(onPath)
		if not pathlib.Path(downloadpath).exists():
			pathlib.Path(downloadpath).mkdir(parents=True, exist_ok=True)
		return downloadpath
	
	@staticmethod
	def checkPathText(TextFile: str):
		path_parent = str(pathlib.Path(TextFile).parent.resolve())
		if not pathlib.Path(path_parent).exists():
			return False
		else:
			return True

class PyTDL(object):
	"""pytube control class"""
	fileLogs = str(pathlib.Path(pathlib.Path.cwd()).resolve().joinpath("logs.txt"))
	
	Quality = ''
	isVideoCount = ''
	onVideo = []
	video_url = []

	def __init__(self, link: str, loadDir: str = '', playListFile: str = '', 
				isPlayList: bool = False, isSaveInfo: bool = False, isSaveURL: bool = False, isSaveIndex: bool = False, isSaveName: bool = False):
		self.url = link
		self.isPlayList = isPlayList
		if loadDir == '':
			self.loadDir = str(pathlib.Path(pathlib.Path.cwd()).resolve())
		else:
			self.loadDir = Files.checkPath(loadDir)
		if playListFile == '':
			self.plFile = str(pathlib.Path(pathlib.Path.cwd()).resolve().joinpath("playlist.txt"))
		else:
			if Files.checkPathText(playListFile):
				self.plFile = playListFile
			else:
				self.plFile = str(pathlib.Path(pathlib.Path.cwd()).resolve().joinpath("playlist.txt"))
		self.isSaveInfo = isSaveInfo
		self.isSaveURL = isSaveURL
		self.isSaveIndex = isSaveIndex
		self.isSaveName = isSaveName

	

if __name__ == '__main__':
	pass
