import pathlib
from filesdir import Files

class BaseTube(object):
	"""	Base Tube control class """

	def __init__(self, link : str = '', loadDir: str = '', playListFile: str = '', 
				isPlayList: bool = False, isSaveInfo: bool = False, isSaveURL: bool = False, 
				isSaveIndex: bool = False, isSaveName: bool = False, isNameUses: bool = False,
				isIndexFile: bool = True, isSaveQuality: bool = True, isCli: bool = True, fileLogs: str = ''):
		'''
			__FileLogs - Error log.
			
			Each time you upload or receive information about one or more videos, the following parameters automatically change regardless of the user.
			Quality = 240p, 360p, 480p, 720p, 1024p. Getting the maximum resolution of each video when downloading or saving information.
			isVideoCount = "1/5 720p" Number/total number, resolution of each video.
			onVideo - Information about the current video in case of output to the error log.
			video_url - loading links from a file.
			onName - Names of one or all videos.
			
			__url - The user's current link.
			__isPlayList - Playlist flag.
			__loadDir - The download directory. It is automatically checked for existence and, if absent, it is created.
			__plFile - Playlist file. The existence of the parent directory is automatically checked.
							If there is no parent directory, the default value is set.
			__isSaveInfo - Flag for saving all information about a playlist or a single video.
			__isSaveURL - Flag for saving playlist or single video links.
			__isSaveIndex - Flag for saving video indexing only when saving text information. 
			__isIndexFile - File indexing flag.
			__isSaveName - Flag for saving the names of a video playlist or a single video.
			__isNameUses - Flag for using video names when uploading them.
			__isSaveQuality - Flag for saving video resolution when naming playlist files or a single video.
			__isCli - Flag for console message output.
		'''
		self.__FileLogs = Files.getLogFile(fileLogs)
		
		self.Quality = ''
		self.isVideoCount = ''
		self.onVideo = []
		self.video_url = []
		self.OnName = []
		
		self.__url = link
		self.__isPlayList = isPlayList
		if loadDir == '':
			self.__loadDir = Files.getCWDPath()
		else:
			self.__loadDir = Files.checkPath(loadDir)
		if playListFile == '':
			self.__plFile = Files.getCWDJoinPath("playlist.txt")
		else:
			if Files.checkPathParent(playListFile):
				self.__plFile = playListFile
			else:
				self.__plFile = Files.getCWDJoinPath("playlist.txt")
		self.__isSaveInfo = isSaveInfo
		self.__isSaveURL = isSaveURL
		self.__isSaveIndex = isSaveIndex
		self.__isIndexFile = isIndexFile
		self.__isSaveName = isSaveIndex
		self.__isNameUses = isNameUses
		self.__isSaveQuality = isSaveQuality
		self.__isCli = isCli

	@property
	def FileLogs(self):
		return self.__FileLogs

	@property
	def url(self):
		return self.__url

	@property
	def isPlayList(self):
		return self.__isPlayList

	@property
	def LoadDir(self):
		return self.__loadDir

	@property
	def plFile(self):
		return self.__plFile

	@property
	def isSaveInfo(self):
		return self.__isSaveInfo

	@property
	def isSaveURL(self):
		return self.__isSaveURL

	@property
	def isSaveIndex(self):
		return self.__isSaveIndex

	@property
	def isIndexFile(self):
		return self.__isIndexFile

	@property
	def isSaveName(self):
		return self.__isSaveName

	@property
	def isNameUses(self):
		return self.__isNameUses

	@property
	def isSaveQuality(self):
		return self.__isSaveQuality

	@property
	def isCli(self):
		return self.__isCli

	@FileLogs.setter
	def FileLogs(self, value: str):
		self.__FileLogs = Files.getLogFile(value)

	@FileLogs.deleter
	def FileLogs(self):
		del self.__FileLogs

	@url.setter
	def url(self, value: str):
		self.__url = value

	@url.deleter
	def url(self):
		del self.__url

	@isPlayList.setter
	def isPlayList(self, value: bool):
		self.__isPlayList = value

	@isPlayList.deleter
	def isPlayList(self):
		del self.__isPlayList

	@LoadDir.setter
	def LoadDir(self, value: str):
		self.__loadDir = Files.checkPath(value)

	@LoadDir.deleter
	def LoadDir(self):
		del self.__loadDir

	@plFile.setter
	def plFile(self, value: str):
		if checkPathParent(value):
			self.__plFile = value
		else:
			self.__plFile = Files.getCWDJoinPath("playlist.txt")

	@plFile.deleter
	def plFile(self):
		del self.__plFile

	@isSaveInfo.setter
	def isSaveInfo(self, value: str):
		self.__isSaveInfo = value

	@isSaveInfo.deleter
	def isSaveInfo(self):
		del self.__isSaveInfo

	@isSaveURL.setter
	def isSaveURL(self, value: bool):
		self.__isSaveURL = value

	@isSaveURL.deleter
	def isSaveURL(self):
		del self.__isSaveURL

	@isSaveIndex.setter
	def isSaveIndex(self, value: bool):
		self.__isSaveIndex = value

	@isSaveIndex.deleter
	def isSaveIndex(self):
		del self.__isSaveIndex

	@isIndexFile.setter
	def isIndexFile(self, value: bool):
		self.__isIndexFile = value

	@isIndexFile.deleter
	def isIndexFile(self):
		del self.__isIndexFile

	@isSaveName.setter
	def isSaveName(self, value: bool):
		self.__isSaveName = value

	@isSaveName.deleter
	def isSaveName(self):
		del self.__isSaveName

	@isNameUses.setter
	def isNameUses(self, value: bool):
		self.__isNameUses = value

	@isNameUses.deleter
	def isNameUses(self):
		del self.__isNameUses

	@isSaveQuality.setter
	def isSaveQuality(self, value: bool):
		self.__isSaveQuality = value

	@isSaveQuality.deleter
	def isSaveQuality(self):
		del self.__isSaveQuality

	@isCli.setter
	def isCli(self, value: bool):
		self.__isCli = value

	@isCli.deleter
	def isCli(self):
		del self.__isCli
