#!/usr/bin/python

import serial
import io
import sys, getopt

def main(argv):
  source = 2
  room = 3
  query = 0

  try:
    opts, args = getopt.getopt(argv, "r:s:c:oij", ["room=", "source="])
  except getopt.GetoptError:
    print 'elan.py -s <source> -r <room>'
    sys.exit(2)

  source = -1
  open = -1
  for opt, arg in opts:
    if opt in ("-r", "--room"):
      room = int(arg)
    elif opt in ("-o", "--open"):
      open = 1
    elif opt in ("-s", "--source"):
      source = int(arg)
      print "In source %d\n" % source
 #     source = arg
    elif opt in ("-c", "--component"):
      component = arg
    elif opt in ("-i"):
      query = 1
    elif opt in ("-j"):
      query = 2
  
  ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=1)
  
  if (open == 1):
    while (1):
      line = sys.stdin.readline();
      print line;
      if (line == "quit\n"):
         sys.exit()
     
      ln = list(line)
      ln[len(line)-1]='\r'
 
      ser.write(unicode(''.join(ln)))
      line = ser.readline()
      print line



  if ((query == 1) or (query == 2)):
    for i in range(1, 17):
      if (query == 1):
         str = "&S12,VOR,1,%02d?\r" % i
      else:
         str = "&S12,CPN,%02d?\r" % i
      ser.write(unicode(str))
      line = ser.readline()
      print line
  else:
    if (source == -1):
      str = "&S12,CPN,%02d,%s\r" % (room, component)
    else:
      str = "&S12,SRC,%02d,%s\r" % (room, source)
    print str
    ser.write(unicode(str))
    ser.flush()

    line = ser.readline()
    print line
    print ""

    str = "&S12,SRC,%02d?\r" % room
    print str;
    ser.write(unicode(str))
    line = ser.readline()
    print line

#ser = io.TextIOWrapper(io.BufferedRWPair(srl, srl), newline='\r')

#def cr_readline(str) :
#    ct=0;
#    chr = str.read(1)
#    buf=""
#    while chr != '\r':
#        print chr
#        buf += chr
#        chr = str.read(1)
#        ct+=1
#        if ct==15:
#		break
#
#    buf += chr
#    return buf

#for i in range(1,9):
# 1 - Bedroom
# 2 - Bathroom
# 3 - Kitechn
# 4 - Living room
# 5 - Bonus 
# 6 - Office
# 7 - Back porch

# Sources
# 12 - Living room Tivo
# 2 - Sonos

if __name__ == "__main__":
    main(sys.argv[1:])
