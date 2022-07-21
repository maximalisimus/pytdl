__all__ = ['getDateTimeStr']

from datetime import datetime

def getDateTimeStr(strFormat = "%d.%m.%Y-%H:%M:%S") -> str:
	dateTime = datetime.now()
	outDateTime = dateTime.strftime(strFormat)
	return outDateTime
