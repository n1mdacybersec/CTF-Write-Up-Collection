from PIL import Image

im = Image.open("flag.png")

im1 = Image.new(mode="RGB", size=(400, 400))

def image_new(name, pixel, step):
	for x in range(400):
		for y in range(400):
			# Get the RGB color value for each step in pixel
			r, g, b = im.getpixel((pixel, y))
			# Modify image by putting the RGB color value from previous step
			im1.putpixel((x, y), (r, g, b))
		pixel += step

	im1.save(str(name)+".png")

image_new("image_new1", 0, 5)
image_new("image_new2", 1, 5)
