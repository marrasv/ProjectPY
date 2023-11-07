import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list,Loggable):
    def append(self, x):
        super().append(x)
        return self.log(x)


a = LoggableList()
a.append(23)
