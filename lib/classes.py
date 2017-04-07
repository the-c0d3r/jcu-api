from datetime import datetime

class Classes:
    def __init__(self, clsname, clstype, clstime, clsroom):
        self.raw_time = clstime # clstime will be a list
        self.room = clsroom
        self.name = clsname
        self.type = clstype

    def getRoom(self):
        return self.room

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def formatTime(self):
        """
        Formats the time into nice string to return
        """
        start = self.raw_time[0]
        end = self.raw_time[1]

        return self.convertTime(start) + " - " + self.convertTime(end)

    def convertTime(self, data):
        d = datetime.strptime(data, "%H:%M")
        return d.strftime("%I:%M")


"""
from datetime import datetime
>>> d = datetime.strptime("10:30", "%H:%M")
>>> d.strftime("%I:%M %p")
'10:30 AM'
>>> d = datetime.strptime("22:30", "%H:%M")
>>> d.strftime("%I:%M %p")
'10:30 PM
"""
