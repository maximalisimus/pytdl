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
		
		Quality = 240p, 360p, 480p, 720p, 1024p ....
		isVideoCount = "1/5 720p" к каждому видео
		onVideo - Информация о текущем видео в случае выведения в лог ошибок
		video_url - Получение всех ссылок плейлиста, в т.ч. из файла. 
	"""
	
	fileLogs = Files.getLogFile()
	
	Quality = ''
	isVideoCount = ''
	onVideo = []
	video_url = []

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
