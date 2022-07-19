__all__ = ['Files']

import pathlib
import re

class Files:
	''' Help on class.

	Name: 
		Files - Files and folders.

	Note:
		A module for working with files and folders.

	File:
		filesdir.py

	Methods
	----------
		getRealPath(pathname: str) -> str:
			Getting the full directory.
		getCWDPath() -> str:
			Getting the current directory.
		getCWDJoinPath(onFiles: str) -> str:
			Attach a file to the current directory.
		getJoinPath(folder: str, value: str) -> str:
			Attach a folder or file to an 
			existing directory.
		getParentPath(folder: str) -> str:
			Find an existing directory, 
			possibly one of the parent.
		getFileName(fileORDir: str) -> str:
			Get the file name from the link.
		getLogFile(logFile: str = '') -> str:
			Error log file.
		checkPath(onPath: str) -> str:
			Checking the presence of the directory. 
			In its absence, a new directory 
			will be created.
		checkPathParent(fileORDir: str) -> str:
			Checking for the presence 
			of the parent directory.
		filterName(onNames: str) -> str:
			Filtering of invalid file name 
			characters for different OS.
	'''

	@staticmethod
	def getRealPath(pathname: str) -> str:
		''' Getting the full directory. '''
		return str(pathlib.Path(pathname).resolve())

	@staticmethod
	def getCWDPath() -> str:
		''' Getting the current directory. '''
		return str(pathlib.Path(pathlib.Path.cwd()).resolve())

	@staticmethod
	def getCWDJoinPath(onFiles: str) -> str:
		''' Attach a file to the current directory. '''
		return str(pathlib.Path(pathlib.Path.cwd()).resolve().joinpath(onFiles))

	@staticmethod
	def getJoinPath(folder: str, value: str) -> str:
		''' Attach a folder or file to an existing directory. '''
		real_path = Files.checkRealPath(folder)
		return str(pathlib.Path(real_path).resolve().joinpath(value))

	@staticmethod
	def getParentPath(folder: str) -> str:
		''' Find an existing directory, possibly one of the parent. '''
		real_path = Files.getRealPath(folder)
		if pathlib.Path(real_path).exists():
			return real_path
		else:
			real_path = str(pathlib.Path(folder).parent.resolve())
			return Files.checkRealPath(real_path)
	
	@staticmethod
	def getFileName(fileORDir: str) -> str:
		''' Get the file name from the link. '''
		return str(pathlib.Path(fileORDir).name)

	@staticmethod
	def getLogFile(logFile: str = '') -> str:
		''' Error log file. '''
		if logFile == '':
			return str(pathlib.Path(pathlib.Path.cwd()).resolve().joinpath("logs.txt"))
		else:
			if Files.checkPathText(logFile):
				return getRealPath(logFile)
			else:
				return str(pathlib.Path(pathlib.Path.cwd()).resolve().joinpath("logs.txt"))

	@staticmethod
	def checkPath(onPath: str) -> str:
		''' Checking the presence of the directory. 
		In its absence, a new directory will be created. '''
		yourPath = Files.getRealPath(onPath)
		if not pathlib.Path(yourPath).exists():
			pathlib.Path(yourPath).mkdir(parents=True, exist_ok=True)
		return yourPath

	@staticmethod
	def checkPathParent(fileORDir: str):
		''' Checking for the presence of the parent directory. '''
		path_parent = str(pathlib.Path(fileORDir).parent.resolve())
		if not pathlib.Path(path_parent).exists():
			return False
		else:
			return True

	@staticmethod
	def filterName(onNames: str) -> str:
		''' Filtering of invalid file name characters for different OS. '''
		outname = str(onNames).replace('|', '.').replace('%', '.').replace(':', '.').replace('"', '.').replace("'", ".").replace('<', '.').replace('>', '.')\
		.replace('[', '.').replace(']', '.').replace('{', '.').replace('}', '.').replace('#', '.').replace('$', '.').replace('?', '.')\
		.replace('`', '.').replace('~', '.').replace('@', '.').replace('!', '.').replace('&', '.').replace('^', '.').replace('*', '.')
		pattern = r'(.)\1+'
		repl = r'\1'
		return re.sub(pattern,repl,outname).strip()

'''

def clear_name(docname,
				slash_replace='-',  # слэш: заменять на минус; используется в идентификаторах документов: типа № 1/2
				quote_replace='',  # кавычки: замены нет - удаляем
				multispaces_replace='\x20', # множественные пробелы на один пробел
				quotes="""“”«»'\""""  # какие кавычки будут удаляться
				):
	docname = re.sub(r'[' + quotes + ']', quote_replace, docname)
	docname = re.sub(r'[/]', slash_replace, docname)
	docname = re.sub(r'[|*?<>:\\\n\r\t\v]', '', docname)  # запрещенные символы в windows
	docname = re.sub(r'\s{2,}', multispaces_replace, docname)
	docname = docname.strip()
	docname = docname.rstrip('-') # на всякий случай
	docname = docname.rstrip('.') # точка в конце не разрешена в windows
	docname = docname.strip()    # не разрешен пробел в конце в windows
	return docname

def slugify(value):
	import unicodedata
	value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
	value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
	value = unicode(re.sub('[-\s]+', '-', value))

def main():
	import re
	t = re.compile("[a-zA-Z0-9.,_-]")
	unsafe = "abc∂éåß®∆˚˙©¬ñ√ƒµ©∆∫ø"
	safe = [ch for ch in unsafe if t.match(ch)]
	# => 'abc'
	#
	s = "Hello$@ Python3&_"
	import re
	s1 = re.sub("[^A-Za-z0-9]", "", s)
	print(s1)
	# Результат: HelloPython3

'''
