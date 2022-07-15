import pathlib
from . import files

'''
class C:
	def __init__(self):
		self._x = None

	@property
	def x(self): # В декораторах 'setter' и 'deleter' нужно указывать имя метода-свойства
		"""I'm the 'x' property."""
		return self._x

	@x.setter
	def x(self, value):
		self._x = value

	@x.deleter
	def x(self):
		del self._x

'''


class Tube(object):
	"""	Tube control class """

	"""
		fileLogs - Лог ошибок
		
		_Quality = 240p, 360p, 480p, 720p, 1024p Получение максимального разрешения каждого видео
		_isVideoCount = "1/5 720p" Номер, общее число, разрешение каждого видео
		_onVideo - Информация о текущем видео в случае выведения в лог ошибок
		_video_url - Загрузка ссылок из файла. 
	"""
	
	fileLogs = Files.getLogFile()
	
	_Quality = ''
	_isVideoCount = ''
	_onVideo = []
	_video_url = []

	def __init__(self, link: str, loadDir: str = '', playListFile: str = '', 
				isPlayList: bool = False, isSaveInfo: bool = False, isSaveURL: bool = False, 
				isSaveIndex: bool = False, isSaveName: bool = False,
				isSaveQuality: bool = True, isCli: bool = True):
		'''
			self.url - текущая ссылка пользователя
			self.isPlayList - Флаг плейлиста
			self.loadDir - Директория для скачивания. При наличии, автоматически проверяется на существование и при отсутствии - создаётся
			self.plFile - Файл плейлиста. При наличии, проверяется директория, в которой он располагается на существование. 
							При отсутствии директории родителя задаётся значение по умолчанию.
			self.isSaveInfo - Флаг сохранении всей информации о плейлисте или одном видео.
			self.isSaveURL - Флаг сохранения ссылок плейлиста или одного видео.
			self.isSaveIndex - Флаг сохранения индексации видео только при сохранении текстовой информации. 
							Индексация файлов плейлиста автоматическая и не изменяется во избежание конфликтов имён.
			self.isSaveName - Флаг сохранения наименований видео плейлиста или одного видео.
			self.isSaveQuality - Флаг сохранения разрешения видео при наименовании файлов плейлиста или одного видео.
			self.isCli - Флаг вывода сообщений консоли.
		'''
		self._url = link
		self._isPlayList = isPlayList
		'''
		if (self._url != ''):
			if self._isPlayList:
				self._YouTube = pytube.Playlist(self._url)
			else:
				self._YouTube = pytube.YouTube(self._url)
		'''
		if loadDir == '':
			self._loadDir = Files.getCWDPath()
		else:
			self._loadDir = Files.checkPath(loadDir)
		if playListFile == '':
			self._plFile = Files.getCWDJoinPath("playlist.txt")
		else:
			if Files.checkPathText(playListFile):
				self._plFile = playListFile
			else:
				self._plFile = Files.getCWDJoinPath("playlist.txt")
		self._isSaveInfo = isSaveInfo
		self._isSaveURL = isSaveURL
		self._isSaveIndex = isSaveIndex
		self._isSaveName = isSaveName
		self._isSaveQuality = isSaveQuality
		self._isCli = isCli

	@property
	def url(self) -> str:
		return self._url

	@property
	def isPlayList(self) -> bool:
		return self._isPlayList

	@property
	def loadDir(self) -> str:
		return self._loadDir

	@property
	def plFile(self) -> str:
		return self._plFile

	@property
	def isSaveInfo(self) -> bool:
		return self._isSaveInfo

	@property
	def isSaveURL(self) -> bool:
		return self._isSaveURL

	@property
	def isSaveIndex(self) -> bool:
		return self._isSaveIndex

	@property
	def isSaveName(self) -> bool:
		return self._isSaveName

	@property
	def isSaveQuality(self) -> bool:
		return self._isSaveQuality

	@property
	def isCli(self) -> bool:
		return self._isCli

	@url.setter
	def url(self, value):
		if value != '':
			self._url = value
	
	@url.deleter
	def url(self):
		del self._url

	@isPlayList.setter
	def isPlayList(self, value: bool):
		self._isPlayList = value

	@isPlayList.deleter
	def isPlayList(self):
		del self._isPlayList
	
	@loadDirx.setter
	def loadDirx(self, value: str):
		self._loadDir = Files.checkPath(value)

	@loadDirx.deleter
	def loadDir(self):
		del self._loadDir

	@plFile.setter
	def plFile(self, value: str):
		if checkPathText(value):
			self._plFile = value

	@plFile.deleter
	def plFile(self):
		del self._plFile

	@isSaveInfo.setter
	def isSaveInfo(self, value: bool):
		self._isSaveInfo = value

	@isSaveInfo.deleter
	def isSaveInfo(self):
		del self._isSaveInfo

	@isSaveURL.setter
	def isSaveURL(self, value: bool):
		self._isSaveURL = value

	@isSaveURL.deleter
	def isSaveURL(self):
		del self._isSaveURL
	
	@isSaveIndex.setter
	def isSaveIndex(self, value: bool):
		self._isSaveIndex = value

	@isSaveIndex.deleter
	def isSaveIndex(self):
		del self._isSaveIndex
	
	@isSaveName.setter
	def isSaveName(self, value: bool):
		self._isSaveName = value

	@isSaveName.deleter
	def isSaveName(self):
		del self._isSaveName
	
	@isSaveQuality.setter
	def isSaveQuality(self, value: bool):
		self._isSaveQuality = value

	@isSaveQuality.deleter
	def isSaveQuality(self):
		del self._isSaveQuality
	
	@isCli.setter
	def isCli(self, value: bool):
		self._isCli = value

	@isCli.deleter
	def isCli(self):
		del self._isCli
