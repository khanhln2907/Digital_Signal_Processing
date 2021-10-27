import time

#from src.Tools import ElapsedTimer

def millis():
    return round(time.time() * 1000)

class ElapsedTimer_Millis:
    _initMillis = 0

    def __init__(self) -> None:
        self._initMillis = millis()

    def __str__(self):
         # Return the time passed since the initalization
         return f'{millis() - self._initMillis}' 