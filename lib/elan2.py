#!/usr/bin/python

import serial
import io
import sys, getopt

def main(argv):

  ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=1)
  
  while (1):
    line = sys.stdin.readline();
    print line;
    if (line == "quit\n"):
       sys.exit()

    line = '&S12,'+line
    print line
   
    ln = list(line)
    ln[len(line)-1]='\r'


 
    ser.write(unicode(''.join(ln)))
    print(unicode(''.join(ln)))
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
