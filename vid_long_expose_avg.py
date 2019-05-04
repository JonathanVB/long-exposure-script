# Long-exposure (avg) simulation from video. Usage: vid_long_expose_avg.py source_video target_image
import sys
import numpy as np
import imageio
filename = sys.argv[1]
vid = imageio.get_reader(filename)
#vidout = imageio.get_writer("test.mp4", format=None, mode='I', fps=60)
target = vid.get_data(0).astype('Float32')
total = 0
last_frame = len(vid)
for i, img in enumerate(vid):
    target += img
    total += 1
    #vidout.append_data(target)
    percent = int((i+1)/last_frame*100)
    sys.stdout.write("\r["+('#'*int(percent/4))+('.'*(25-int(percent/4)))+("] %d"%percent+"%"+" (%d"%i+"/%d"%last_frame+")"))
    sys.stdout.flush()
target = target/(total*255)
vid.close()
#vidout.close()
imageio.imwrite(sys.argv[2], target)
