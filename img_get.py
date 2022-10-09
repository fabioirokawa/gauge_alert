# import the opencv library
import cv2
import os.path

from datetime import datetime

count_img = {}
img_number = 0
file_name = "contador.txt"

def get_image():

	# define a video capture object
	vid = cv2.VideoCapture(0)

		
	# Capture the video frame
	# by frame
	ret, frame = vid.read()

	if ret:
		cv2.imshow('frame', frame)
	# Display the resulting frame
		today = datetime.now()
		time = today.strftime("%d%m%Y_%H%M%S")
		file_img = "gauge_%s.png" % time
		settings.file_img = file_img
		settings.update()
		print(settings.full_path + "AKSDKADSKAAK")
		cv2.imwrite(settings.full_path, frame)
		
	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
	# if cv2.waitKey(1) & 0xFF == ord('q'):

	# Destroy all the windows
		cv2.destroyAllWindows()

	else:
		print("Nada")

	return file_img

#le / guarda contador de fotos tiradas
def file_read():
	with open(file_name, "r") as f:
					try:
						contador = int(f.read())
						print(contador)
					finally:
						f.close()
		
if __name__ == "__main__":
	get_image()