import pathlib
from filesdir import Files

class BaseTube(object):
	"""	Tube control class """
	
	def __init__(self, link, loadDir = '', playListFile = '', 
				isPlayList = False, isSaveInfo = False, isSaveURL = False, 
				isSaveIndex = False, isSaveName = False,
				isSaveQuality = True, isCli = True):
		'''
			__fileLogs - Лог ошибок
		
			Quality = 240p, 360p, 480p, 720p, 1024p Получение максимального разрешения каждого видео при скачивании или сохранении информации
			isVideoCount = "1/5 720p" Номер, общее число, разрешение каждого видео
			onVideo - Информация о текущем видео в случае выведения в лог ошибок
			video_url - Загрузка ссылок из файла. 
			
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
			__isSaveQuality - Флаг сохранения разрешения видео при наименовании файлов плейлиста или одного видео.
			__isCli - Флаг вывода сообщений консоли.
		'''
		self.__fileLogs = Files.getLogFile()
		
		self.Quality = ''
		self.isVideoCount = ''
		self.onVideo = []
		self.video_url = []
		
		if type(link) == str:
			self.__url = link
		else:
			raise TypeError('Не верный тип данных! Введите строку!')
		if type(isPlayList) == bool:
			self.__isPlayList = isPlayList
		else:
			raise TypeError('Не верный тип данных! Введите "True" или "False"!')
		if type(loadDir) == str:	
			if loadDir == '':
				self.__loadDir = Files.getCWDPath()
			else:
				self.__loadDir = Files.checkPath(loadDir)
		else:
			raise TypeError('Не верный тип данных! Введите строку!')
		if type(playListFile) == str:
			if playListFile == '':
				self.__plFile = Files.getCWDJoinPath("playlist.txt")
			else:
				if Files.checkPathParent(playListFile):
					self.__plFile = playListFile
				else:
					self.__plFile = Files.getCWDJoinPath("playlist.txt")
		else:
			raise TypeError('Не верный тип данных! Введите строку!')
		if type(isSaveInfo) == bool:
			self.__isSaveInfo = isSaveInfo
		else:
			raise TypeError('Не верный тип данных! Введите "True" или "False"!')
		if type(isSaveURL) == bool:
			self.__isSaveURL = isSaveURL
		else:
			raise TypeError('Не верный тип данных! Введите "True" или "False"!')
		if type(isSaveIndex) == bool:
			self.__isSaveIndex = isSaveIndex
		else:
			raise TypeError('Не верный тип данных! Введите "True" или "False"!')
		if type(isSaveIndex) == bool:
			self.__isSaveName = isSaveIndex
		else:
			raise TypeError('Не верный тип данных! Введите "True" или "False"!')
		if type(isSaveQuality) == bool:
			self.__isSaveQuality = isSaveQuality
		else:
			raise TypeError('Не верный тип данных! Введите "True" или "False"!')
		if type(isCli) == bool:
			self.__isCli = isCli
		else:
			raise TypeError('Не верный тип данных! Введите "True" или "False"!')

	@property
	def fileLogs(self):
		return self.__fileLogs

	@property
	def url(self):
		return self.__url

	@property
	def isPlayList(self):
		return self.__isPlayList

	@property
	def loadDir(self):
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
	def isSaveQuality(self):
		return self.__isSaveQuality

	@property
	def isCli(self):
		return self.__isCli

	@fileLogs.setter
	def fileLogs(self, value):
		if type(value) == str:
			self.__fileLogs = Files.getLogFile(value)
		else:
			raise TypeError('Не верный тип данных! Введите строку!')
	
	@fileLogs.deleter
	def fileLogs(self):
		del self.__fileLogs

	@url.setter
	def url(self, value):
		if type(value) == str:
			self.__url = value
		else:
			raise TypeError('Не верный тип данных! Введите строку!')
	
	@url.deleter
	def url(self):
		del self.__url

	@isPlayList.setter
	def isPlayList(self, value):
		if type(value) == bool:
			self.__isPlayList = value
		else:
			raise TypeError('Не верный тип данных! Введите "True" или "False"!')

	@isPlayList.deleter
	def isPlayList(self):
		del self.__isPlayList
	
	@loadDirx.setter
	def loadDirx(self, value):
		if type(value) == str:
			self.__loadDir = Files.checkPath(value)
		else:
			raise TypeError('Не верный тип данных! Введите строку!')

	@loadDirx.deleter
	def loadDir(self):
		del self.__loadDir

	@plFile.setter
	def plFile(self, value):
		if type(value) == str:
			if checkPathParent(value):
				self.__plFile = value
		else:
			raise TypeError('Не верный тип данных! Введите строку!')

	@plFile.deleter
	def plFile(self):
		del self.__plFile

	@isSaveInfo.setter
	def isSaveInfo(self, value):
		if type(value) == bool:
			self.__isSaveInfo = value
		else:
			raise TypeError('Не верный тип данных! Введите "True" или "False"!')

	@isSaveInfo.deleter
	def isSaveInfo(self):
		del self.__isSaveInfo

	@isSaveURL.setter
	def isSaveURL(self, value):
		if type(value) == bool:
			self.__isSaveURL = value
		else:
			raise TypeError('Не верный тип данных! Введите "True" или "False"!')

	@isSaveURL.deleter
	def isSaveURL(self):
		del self.__isSaveURL
	
	@isSaveIndex.setter
	def isSaveIndex(self, value):
		if type(value) == bool:
			self.__isSaveIndex = value
		else:
			raise TypeError('Не верный тип данных! Введите "True" или "False"!')

	@isSaveIndex.deleter
	def isSaveIndex(self):
		del self.__isSaveIndex
	
	@isSaveName.setter
	def isSaveName(self, value):
		if type(value) == bool:
			self.__isSaveName = value
		else:
			raise TypeError('Не верный тип данных! Введите "True" или "False"!')

	@isSaveName.deleter
	def isSaveName(self):
		del self.__isSaveName
	
	@isSaveQuality.setter
	def isSaveQuality(self, value):
		if type(value) == bool:
			self.__isSaveQuality = value
		else:
			raise TypeError('Не верный тип данных! Введите "True" или "False"!')

	@isSaveQuality.deleter
	def isSaveQuality(self):
		del self.__isSaveQuality
	
	@isCli.setter
	def isCli(self, value):
		if type(value) == bool:
			self.__isCli = value
		else:
			raise TypeError('Не верный тип данных! Введите "True" или "False"!')

	@isCli.deleter
	def isCli(self):
		del self.__isCli
