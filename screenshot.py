# -*- coding: utf-8 -*-
import numpy as np
import cv2
import time
from PIL import ImageGrab

last_time = time.time()
while(True):
    printscreen_pil =  ImageGrab.grab(bbox = (0, 40, 600, 340))
   
    print('loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
    cv2.imshow('window',np.array(printscreen_pil))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
