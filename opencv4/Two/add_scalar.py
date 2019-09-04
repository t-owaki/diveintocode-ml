# -*- coding: utf-8 -*

import cv2
import numpy as np

try:
    img = cv2.imread('c:/temp/Parrots.jpg')
    
    if img is None:
        print ('ファイルを読み込めません。')
        import sys
        sys.exit()
    
    height = img.shape[0]
    width = img.shape[1]
    blue = np.zeros((height, width, 3), np.uint8)
    blue[:,:] = [128, 0, 0]
    
    dst = cv2.add(img, blue)
    cv2.imwrite('c:/temp/addScalar.jpg', dst)
    cv2.imshow('dst', dst)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))