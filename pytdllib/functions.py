__all__ = ['dateTimeToStrNow']

from datetime import datetime

def dateTimeToStrNow(strFormat = "%d.%m.%Y-%H:%M:%S") -> str:
	dateTime = datetime.now()
	outDateTime = dateTime.strftime(strFormat)
	return outDateTime
