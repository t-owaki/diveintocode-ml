# -*- coding: utf-8 -*

import cv2

try:    
    src1 = cv2.imread('c:/temp/src1.jpg')
    src2 = cv2.imread('c:/temp/src2.jpg')
    
    if src1 is None or src2 is None:
        print ('ファイルを読み込めません。')
        import sys
        sys.exit()
    
    detector = cv2.AKAZE_create()
    keypoints1, descriptor1 = detector.detectAndCompute(src1, None)
    keypoints2, descriptor2 = detector.detectAndCompute(src2, None)

    matcher = cv2.BFMatcher(cv2.NORM_HAMMING)
    matches = matcher.match(descriptor1, descriptor2)
    dst = cv2.drawMatches(src1, keypoints1, src2, keypoints2, matches, None, flags=2)
    
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