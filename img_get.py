# import the opencv library
import cv2
import os.path

from datetime import datetime

count_img = {}
img_number = 0
file_name = "contador.txt"

def get_image(path):


	# define a video capture object
	vid = cv2.VideoCapture(1)

		
	# Capture the video frame
	# by frame
	ret, frame = vid.read()

	if ret:
		cv2.imshow('frame', frame)
	# Display the resulting frame
		today = datetime.now()
		time = today.strftime("%d%m%Y_%H%M%S")
		file_img = "gauge_%s.png" % time
		fullPath = path + file_img
		#print(settings.full_path)
		cv2.imwrite(fullPath, frame)
		
	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
	# if cv2.waitKey(1) & 0xFF == ord('q'):

	# Destroy all the windows
		cv2.destroyAllWindows()

	else:
		print("Nada")

	return file_img
		
if __name__ == "__main__":
	get_image()