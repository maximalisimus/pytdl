#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from pytdllib.basetube import *

def main():
	print(dir(sys.modules[__name__]))

if __name__ == '__main__':
	main()
