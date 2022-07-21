#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
import sys
from pytdllib.basetube import *
'''
#from pathlib import Path
import pathlib
import sys
#sys.path.insert(0, str(pathlib.Path('./pytdllib').resolve()))
#from functions import *
sys.path.insert(0, str(pathlib.Path('./').resolve()))
from pytdllib.functions import *

def main():
	'''
	for i in sys.path:
		print(i)
	'''
	#print(dir(sys.modules[__name__]))
	print(getDateTimeStr())

if __name__ == '__main__':
	main()
