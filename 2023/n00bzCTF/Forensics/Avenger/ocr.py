# extract text from all the images in a folder
# storing the text in a single file
from PIL import Image
import pytesseract as pt
import os
	
def main():
	# path for the folder for getting the raw images
	path ="./flag-opencv/"

	# link to the file in which output needs to be kept
	fullTempPath ="./output.txt"
	
	listFiles = sorted( filter(lambda x: os.path.isfile(os.path.join(path, x)), os.listdir(path)))

	# iterating the images inside the folder
	for imageName in listFiles:
		inputPath = os.path.join(path, imageName)
		img = Image.open(inputPath)

		# applying ocr using pytesseract for python
		text = pt.image_to_string(img, lang ="eng")

		# saving the text for appending it to the output.txt file
		# a + parameter used for creating the file if not present
		# and if present then append the text content
		file1 = open(fullTempPath, "a+")

		# providing the content in the image
		file1.write(text)
		file1.close()

	# for printing the output file
	file2 = open(fullTempPath, 'r')
	print(file2.read())
	file2.close()		


if __name__ == '__main__':
	main()
