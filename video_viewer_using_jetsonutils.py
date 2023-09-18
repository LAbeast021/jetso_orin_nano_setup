
import sys
import cv2
from jetson_utils import videoSource, videoOutput
from jetson_inference import imageNet

dispW = 1920
dispH = 1080

camSet = '/dev/video0'

input = videoSource(camSet, argv = ['--input-width='+str(dispW),'--input-height='+str(dispH)])

output = videoOutput('display://0')
while output.IsStreaming():
    image = input.Capture()
    output.Render(image)
    output.SetStatus( "Video Viewer | {:d}x{:d} | {:.1f} FPS" .format(image.width, image.height , input.GetFrameRate()) ) 