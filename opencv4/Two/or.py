# -*- coding: utf-8 -*

import cv2

try:
    img1 = cv2.imread('c:/temp/Lenna.jpg')
    img2 = cv2.imread('c:/temp/Parrots.jpg')
    
    if img1 is None or img2 is None:
        print ('ファイルを読み込めません。')
        import sys
        sys.exit()
    
    dst = cv2.bitwise_or(img1, img2)
    cv2.imwrite('c:/temp/or.jpg', dst)
    cv2.imshow('dst1', dst)
    
    img_mask = cv2.imread('c:/temp/mask.bmp', cv2.IMREAD_GRAYSCALE)
    dst = cv2.bitwise_or(img1, img2, img1, img_mask)
    cv2.imwrite('c:/temp/orMask.jpg', dst)
    cv2.imshow('dst2', dst)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))