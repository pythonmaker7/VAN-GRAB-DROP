from script import *
import sys

# print.py      -> s2s.txt (path relative)
sys.stdout = open('../STATIONTOSTATION.txt', 'w')
sys.stdout.close()

# print.command -> print.py (path absolute)
# print.command -> s2s.txt (path absolute)