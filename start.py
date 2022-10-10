import img_get as webcam
import analog_gauge_reader as gauge

path = './images/'
full_path = ""

#settings.init()
file_img = webcam.get_image(path)
#print(file_img)
gauge.main(file_img, path)