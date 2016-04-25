from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import serial
import io
import sys


# Create your views here.

def index(request):
    rooms = {1: 3, 2: 4}
    return render(request, 'webtool/index.html', {'rooms': rooms})

def list(request, source):
    return HttpResponse("Hello list. Source is " + source)

def set(request, source, room):
    setRoom(int(source), int(room))
    return HttpResponseRedirect("/webtool/")

def setRoom(source, room):
    ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=1)
    str = "&S12,SRC,%02d,%d\r" % (room, source)
    print str
    ser.write(unicode(str))
    ser.flush()

    line = ser.readline()
    print line
    print ""

def roomStatus():
    ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=1)
    for i in range(1, 9):
      str = "&S12,SRC,%02d?\r" % i
      ser.write(unicode(str))
      line = ser.readline()
      print line[12:]

