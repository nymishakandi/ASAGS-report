from ContSurv import ContinousSurv
if __name__ == '__main__':
	obj = ContinousSurv()
	# doing surveillance on a video file
	# obj.setVideoName('testV2.avi')
	# obj.doSurveillanceFromVideo()
	# doing surveillance with the camera
	obj.doSurveillanceFromCamera()
