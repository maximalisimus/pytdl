import pathlib
from filesdir import Files

class BaseTube(object):
	"""	Base Tube control class """

	def __init__(self, link : str = '', loadDir: str = '', playListFile: str = '', 
				isPlayList: bool = False, isSaveInfo: bool = False, isSaveURL: bool = False, 
				isSaveIndex: bool = False, isSaveName: bool = False, isNameUses: bool = False,
				isSaveQuality: bool = True, isCli: bool = True, fileLogs: str = ''):
		'''
			__FileLogs - Лог ошибок
			
			При каждой загрузке или получения информации об одном или нескольких видео автоматически меняются независимо от пользователя.
			Quality = 240p, 360p, 480p, 720p, 1024p Получение максимального разрешения каждого видео при скачивании или сохранении информации
			isVideoCount = "1/5 720p" Номер, общее число, разрешение каждого видео
			onVideo - Информация о текущем видео в случае выведения в лог ошибок
			video_url - Загрузка ссылок из файла. 
			onName - Наименования одного или всех видео.
			
			__url - текущая ссылка пользователя
			__isPlayList - Флаг плейлиста
			__loadDir - Директория для скачивания. При наличии, автоматически проверяется на существование и при отсутствии - создаётся
			__plFile - Файл плейлиста. При наличии, проверяется директория, в которой он располагается на существование. 
							При отсутствии директории родителя задаётся значение по умолчанию.
			__isSaveInfo - Флаг сохранении всей информации о плейлисте или одном видео.
			__isSaveURL - Флаг сохранения ссылок плейлиста или одного видео.
			__isSaveIndex - Флаг сохранения индексации видео только при сохранении текстовой информации. 
							Индексация файлов плейлиста автоматическая и не изменяется во избежание конфликтов имён.
			__isSaveName - Флаг сохранения наименований видео плейлиста или одного видео.
			__isNameUses - Флаг использования имен видео при их загрузке.
			__isSaveQuality - Флаг сохранения разрешения видео при наименовании файлов плейлиста или одного видео.
			__isCli - Флаг вывода сообщений консоли.
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
