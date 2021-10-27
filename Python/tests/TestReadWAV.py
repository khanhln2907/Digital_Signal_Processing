import sys
import logging
sys.path.append('C:\\Users\\khanh\\Desktop\\Workspace\\DSP\\')

logging.basicConfig(encoding='utf-8', level=logging.INFO)

from src.Parser import Parser


filepath = ".\\dataset\\IRMAS-Sample\\Training\\sax\\118__[sax][nod][jaz_blu]1702__3.wav"
myParser = Parser(filepath)
myParser.visualize()
myParser.splitChannels()
