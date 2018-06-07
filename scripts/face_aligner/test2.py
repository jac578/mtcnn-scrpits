import os
import sys
import os.path as osp
import time
import json

import struct
import numpy as np

def get_gt_rect(rect_fn):
    fp = open(rect_fn, 'r')
    facex_det_resp=json.load(fp)
    rects=[]
    js_str = json.dumps(facex_det_resp, indent=4)
    print facex_det_resp
    if(not facex_det_resp
        or facex_det_resp['code']
        or 'result' not in facex_det_resp
        or 'detections' not in facex_det_resp['result']
        or len(facex_det_resp['result']['detections']) < 1
        ):
            print '--->facex-det failed or no face detected '
            return [] 
    faces = facex_det_resp['result']['detections']
    print '\n--->%d faces detected' % len(faces)
    # facex-det request data
    for face_idx, face in enumerate(faces):
        print '\n--->process face #%d' % face_idx
        # facex-[age, gender, feature] request data
        bbox=face['pts']
        t_array = np.array(bbox) 
        # if t_array.shape == (4, 2):
        #     t_array = t_array[(0,2), ...]
        # elif t_array.size == 4:
        #     t_array = t_array.reshape((2, 2))
        if t_array.shape == (4, 2):
            xmin,ymin=t_array[0]
            xmax,ymax=t_array[2]
            rect = [xmin, ymin, xmax, ymax]
            print 'rect--->',rect
            rects.append(rect)
           
    print 'rects====>\n',rects 
    return rects


if __name__ == "__main__":
      rect_fn="/Users/jackie/Desktop/test.json"
      gt_rect = get_gt_rect(rect_fn)