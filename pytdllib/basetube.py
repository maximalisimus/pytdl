import pathlib
from .filesdir import Files
from .vars import Stroka, Boolean

__all__ = ['BaseTube']

class BaseTube(object):
	"""	Base Tube control class 
	
		FileLogs - Error log.
			
		Each time you upload or receive information about one or more videos, the following parameters automatically change regardless of the user.
		Quality = 240p, 360p, 480p, 720p, 1024p. Getting the maximum resolution of each video when downloading or saving information.
		isVideoCount = "1/5 720p" Number/total number, resolution of each video.
		onVideo - Information about the current video in case of output to the error log.
		video_url - loading links from a file.
		onName - Names of one or all videos.
		
		url - The user's current link.
		isPlayList - Playlist flag.
		loadDir - The download directory. It is automatically checked for existence and, if absent, it is created.
		plFile - Playlist file. The existence of the parent directory is automatically checked.
						If there is no parent directory, the default value is set.
		isSaveInfo - Flag for saving all information about a playlist or a single video.
		isSaveURL - Flag for saving playlist or single video links.
		isSaveIndex - Flag for saving video indexing only when saving text information. 
		isIndexFile - File indexing flag.
		isSaveName - Flag for saving the names of a video playlist or a single video.
		isNameUses - Flag for using video names when uploading them.
		isSaveQuality - Flag for saving video resolution when naming playlist files or a single video.
		isCli - Flag for console message output.
	"""
	self.FileLogs = Stroka()
	self.url = Stroka()
	self.isPlayList = Boolean()
	self.loadDir = Stroka()
	self.plFile = Stroka()
	self.isSaveInfo = Boolean()
	self.isSaveURL = Boolean()
	self.isSaveIndex = Boolean()
	self.isIndexFile = Boolean()
	self.isSaveName = Boolean()
	self.isNameUses = Boolean()
	self.isSaveQuality = Boolean()
	self.isCli = Boolean()

	def __init__(self, *args, **kwargs):
		'''
			link : str = '', loadDir: str = '', playListFile: str = '', 
				isPlayList: bool = False, isSaveInfo: bool = False, isSaveURL: bool = False, 
				isSaveIndex: bool = False, isSaveName: bool = False, isNameUses: bool = False,
				isIndexFile: bool = True, isSaveQuality: bool = True, isCli: bool = True, FileLogs: str = ''
		'''
		self.Quality = ''
		self.isVideoCount = ''
		self.onVideo = []
		self.video_url = []
		self.OnName = []
		
		
		
		'''
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
		'''

