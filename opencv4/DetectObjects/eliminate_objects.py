# -*- coding: utf-8 -*

import cv2

try:    
    img = cv2.imread('c:/temp/input.jpg')
    msk = cv2.imread('c:/temp/mask.jpg', cv2.IMREAD_GRAYSCALE)
    
    if img is None or msk is None:
        print ('ファイルを読み込めません。')
        import sys
        sys.exit()

    dst = cv2.inpaint(img, msk, 1, cv2.INPAINT_TELEA)
    
    cv2.imwrite('c:/temp/dst.jpg', dst)
    cv2.imshow('dst', dst)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    import sys
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))