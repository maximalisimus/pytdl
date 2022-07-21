__all__ = ['BaseTube']

from .filesdir import *
from .variables import *
from .functions import *

class BaseTube(object):
	"""	Help on class.

	NAME:
		BaseTube - The base class of the "Pytube" class management.

	Note:
		This class is only a set of certain parameters, 
		i.e. strictly defined variables. 
		There is no control in this class.

	File:
		basetube.py

	Attributes
	----------
		FileLog : str
			Log file.

		Each time you upload or receive information 
		about one or more videos, the following parameters 
		automatically change regardless of the user.
		Quality : str 
			240p, 360p, 480p, 720p, 1024p. 
			Getting the maximum resolution of each video 
			when downloading or saving information.
		isVideoCount : str
			"1/5 720p" - Number/total number, 
			resolution of each video.
		onVideo : str
			Information about the current video in case 
			of output to the error log.
		video_url : str
			loading links from a file.
		onName : str
			Names of one or all videos.

		url : str
			The user's current link.
		isPlayList : bool
			Playlist flag.
		loadDir : str
			The download directory. 
			It is automatically checked for existence and, 
			if absent, it is created.
		plFile : str
			Playlist file. The existence of the parent directory 
			is automatically checked.
			If there is no parent directory, 
			the default value is set.
		isSaveInfo : bool
			Flag for saving all information about a playlist 
			or a single video.
		isSaveURL : bool
			Flag for saving playlist or single video links.
		isSaveIndex : bool
			Flag for saving video indexing only 
			when saving text information. 
		isIndexFile : bool
			File indexing flag.
		isSaveName : bool
			Flag for saving the names of a video playlist 
			or a single video.
		isNameUses : bool
			Flag for using video names when uploading them.
		isSaveQuality : bool
			Flag for saving video resolution 
			when naming playlist files or a single video.
		isCli : bool
			Flag for console message output.
	"""

	FileLog = Stroka()
	url = Stroka()
	isPlayList = Boolean()
	loadDir = Stroka()
	plFile = Stroka()
	isSaveInfo = Boolean()
	isSaveURL = Boolean()
	isSaveIndex = Boolean()
	isIndexFile = Boolean()
	isSaveName = Boolean()
	isNameUses = Boolean()
	isSaveQuality = Boolean()
	isCli = Boolean()

	def __init__(self, *args, **kwargs):
		''' Initialization.
		
		Note:
			The order of assigning values to variables 
			that you do not want to enter names ("*args") 
			or named arguments "**kwargs" with default values.
		
		Parameters
		----------
			link : str = ''
			loadDir: str = ''
			playListFile: str = '' 
			isPlayList: bool = False
			isSaveInfo: bool = False
			isSaveURL: bool = False
			isSaveIndex: bool = False
			isSaveName: bool = False
			isNameUses: bool = False,
			isIndexFile: bool = True
			isSaveQuality: bool = True
			isCli: bool = True
			FileLog: str = ''
		'''
		self.Quality = ''
		self.isVideoCount = ''
		self.onVideo = []
		self.video_url = []
		self.OnName = []
		
		self.url = args[0] if len(args) >= 1 else kwargs.get('link', '')
		self.loadDir = (Files.getCWDPath() if args[1] == '' \
						else Files.checkPath(args[1])) if len(args) >= 2 \
						else (Files.getCWDPath() if kwargs.get('loadDir', '') == '' \
						else Files.checkPath(kwargs.get('loadDir', '')))
		self.plFile = ( Files.getCWDJoinPath("playlist.txt") if args[2] == '' \
						else Files.getJoinPath(Files.getParentPath(args[2]), Files.getFileName(args[2])) ) if len(args) >= 3 \
						else Files.getJoinPath(Files.getParentPath(kwargs.get('playListFile', '')), Files.getFileName(kwargs.get('playListFile', '')))
		self.isPlayList = args[3] if len(args) >= 4 else kwargs.get('isPlayList', False)
		self.isSaveInfo = args[4] if len(args) >= 5 else kwargs.get('isSaveInfo', False)
		self.isSaveURL = args[5] if len(args) >= 6 else kwargs.get('isSaveURL', False)
		self.isSaveIndex = args[6] if len(args) >= 7 else kwargs.get('isSaveIndex', False)
		self.isSaveName = args[7] if len(args) >= 8 else kwargs.get('isSaveName', False)
		self.isNameUses = args[8] if len(args) >= 9 else kwargs.get('isNameUses', False)
		self.isIndexFile = args[9] if len(args) >= 10 else kwargs.get('isIndexFile', True)
		self.isSaveQuality = args[10] if len(args) >= 11 else kwargs.get('isSaveQuality', True)
		self.isCli = args[11] if len(args) >= 12 else kwargs.get('isCli', True)
		self.FileLog = Files.getLogFile(args[12]) if len(args) >= 13 else Files.getLogFile(kwargs.get('FileLog', ''))
		self.__onFinish = False

	def __setattr__(self, key, value):
		isValue = False
		if key == 'loadDir':
			onValue = Files.getCWDPath() if vaue == '' else Files.checkPath(value)
			isValue = True
		elif key == 'plFile':
			onValue = Files.getCWDJoinPath("playlist.txt") if vaue == '' else Files.getJoinPath(Files.getParentPath(value), Files.getFileName(value))
			isValue = True
		elif key == 'FileLog':
			onValue = Files.getLogFile(value)
			isValue = True
		object.__setattr__(self, key, onValue if isValue else value)
