import cv2
import os
import time
import shutil
import sys

#camera connection
#'rstp://username:password@ip:port/live/ch00_0'
url = 'rtsp://username:password@ip:port/live/chanal'
camera = cv2.VideoCapture(url)
k = 0 #flag to end

def main():

  #start rec loop
  while True:
    #record file
    timestart = time.time()
    date = time.localtime(timestart)
    save_path = 'd:\\path\\to\\record\\directory\\{y:04}-{m:02}-{d:02}'.format(y=date.tm_year,m=date.tm_mon,d=date.tm_mday) #name path
    name = '{h:02}-{m:02}.avi'.format(h=date.tm_hour,m=date.tm_min) #name file
    frames_per_second = 24.0 
    fourcc = cv2.VideoWriter_fourcc(*'XVID') #video decode xvid for avi file
    resolution = (int(camera.get(3)),int(camera.get(4))) #auto resolution from camera

    #create new directory and delete old record
    if not os.path.isdir(save_path): #isn't path exists
      os.makedirs(save_path) #create path

      #del record from 16 day ago
      timestart -= 1382400 #16 day = 1382400 sec
      date = time.localtime(timestart)
      old_path = 'd:\\IPCAMERA\\{y:04}-{m:02}-{d:02}'.format(y=date.tm_year,m=date.tm_mon,d=date.tm_mday)
      if os.path.isdir(old_path):
        del_dir(old_path)

    #create record
    rec_out = cv2.VideoWriter(os.path.join(save_path,name),fourcc,frames_per_second,resolution)

    #record frame
    while True:
      #capture frame by frame 
      ret, frame = camera.read()

      #result
      cv2.imshow('Output', frame) #display result
      rec_out.write(frame) #result record

      #stop record loop when press ESC or 10 min
      k = cv2.waitKey(20) &0xFF
      if k == 27 or time.time()-timestart>=600:#ESC to exit or 600 sec to create new record
        rec_out.release() #release record
        break

    #terminate program
    if k == 27:#if exit by ESC terminate
      print('...ending...')
      camera.release()
      cv2.destroyAllWindows()
      sys.exit()
    

#delete directory
def del_dir(path):
  try:
    shutil.rmtree(path)
  except OSError as e:
    print('Error: %s - %s.' % (e.filename, e.strerror))

#running and error handleing
while k != 27:
  try:
    main()
  except Exception as error:
    print (str(error))
    timestart = time.time()
    date = time.localtime(timestart)
    print ('{y:04}-{m:02}-{d:02}'.format(y=date.tm_year,m=date.tm_mon,d=date.tm_mday))
    print ('{h:02}-{m:02}'.format(h=date.tm_hour,m=date.tm_min))
    print ('...restarting...')
    try: #try to release cam for error before cam release
      camera.release()
      cv2.destroyAllWindows()
    except Exception as error:
      print (str(error))
      print('...release cam fail...')
      continue
    try: #try to connect camera
      camera = cv2.VideoCapture(url)
    except Exception as error:
      print (str(error))
      print('...connection fail...')
      time.sleep(60) #wait 60 sec if connection fail
      continue
    continue
import cv2
import os
import time
import shutil
import sys

#camera connection
#'rstp://username:password@ip:port/live/ch00_0'
url = 'rtsp://admin:pP123456pP@192.168.1.116:554/live/ch00_1'
camera = cv2.VideoCapture(url)
k = 0 #flag to end

def main():

  #start rec loop
  while True:
    #record file
    timestart = time.time()
    date = time.localtime(timestart)
    save_path = 'd:\\IPCAMERA\\{y:04}-{m:02}-{d:02}'.format(y=date.tm_year,m=date.tm_mon,d=date.tm_mday) #name path
    name = '{h:02}-{m:02}.avi'.format(h=date.tm_hour,m=date.tm_min) #name file
    frames_per_second = 24.0 
    fourcc = cv2.VideoWriter_fourcc(*'XVID') #video decode xvid for avi file
    resolution = (int(camera.get(3)),int(camera.get(4))) #auto resolution from camera

    #create new directory and delete old record
    if not os.path.isdir(save_path): #isn't path exists
      os.makedirs(save_path) #create path

      #del record from 16 day ago
      timestart -= 1382400 #16 day = 1382400 sec
      date = time.localtime(timestart)
      old_path = 'd:\\IPCAMERA\\{y:04}-{m:02}-{d:02}'.format(y=date.tm_year,m=date.tm_mon,d=date.tm_mday)
      if os.path.isdir(old_path):
        del_dir(old_path)

    #create record
    rec_out = cv2.VideoWriter(os.path.join(save_path,name),fourcc,frames_per_second,resolution)

    #record frame
    while True:
      #capture frame by frame 
      ret, frame = camera.read()

      #result
      cv2.imshow('Output', frame) #display result
      rec_out.write(frame) #result record

      #stop record loop when press ESC or 10 min
      k = cv2.waitKey(20) &0xFF
      if k == 27 or time.time()-timestart>=600:#ESC to exit or 600 sec to create new record
        rec_out.release() #release record
        break

    #terminate program
    if k == 27:#if exit by ESC terminate
      print('...ending...')
      camera.release()
      cv2.destroyAllWindows()
      sys.exit()
    

#delete directory
def del_dir(path):
  try:
    shutil.rmtree(path)
  except OSError as e:
    print('Error: %s - %s.' % (e.filename, e.strerror))

#running and error handleing
while k != 27:
  try:
    main()
  except Exception as error:
    print (str(error))
    timestart = time.time()
    date = time.localtime(timestart)
    print ('{y:04}-{m:02}-{d:02}'.format(y=date.tm_year,m=date.tm_mon,d=date.tm_mday))
    print ('{h:02}-{m:02}'.format(h=date.tm_hour,m=date.tm_min))
    print ('...restarting...')
    try: #try to release cam for error before cam release
      camera.release()
      cv2.destroyAllWindows()
    except Exception as error:
      print (str(error))
      print('...release cam fail...')
      continue
    try: #try to connect camera
      camera = cv2.VideoCapture(url)
    except Exception as error:
      print (str(error))
      print('...connection fail...')
      time.sleep(60) #wait 60 sec if connection fail
      continue
    continue
