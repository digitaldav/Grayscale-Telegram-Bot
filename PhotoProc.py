from PIL import Image, ImageOps

def Grayscale(imageName):
	col = Image.open(imageName)
	gray = col.convert('L')
	result = imageName+"GS.png"
	gray.save(result)
	return result

def Sepia(imageName):
	col = Image.open(imageName)
	gray = col.convert('L')
	sepia = make_linear_ramp((255, 240, 192))
	gray = ImageOps.autocontrast(gray)
	gray.putpalette(sepia)
	gray = gray.convert("RGB")
	result = imageName+"Sepia.png"
	gray.save(result)
	return result


def make_linear_ramp(white):
    ramp = []
    r, g, b = white
    for i in range(255):
        ramp.extend((r*i/255, g*i/255, b*i/255))
    return ramp