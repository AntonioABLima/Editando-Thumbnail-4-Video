from PIL import Image, ImageFilter 
import numpy as np

def buildThumbnail():
    bolinha = Image.open('images/subscribe/result.png')
    bolinha = bolinha.rotate(-3, resample=Image.BICUBIC, expand=False)
    pix = bolinha.load()
    color = pix[407, 411]

    buildContourLinesBlurBackground(color)
    buildBrushHead(color)
    
    background = Image.open('images/thumb/final_background.png')
    
    cavalete = Image.open('images/thumb/cavalete.png')

    eu = Image.open('images/thumb/eu2Pincel.png')

    pincelPonta = Image.open('images/thumb/final_ponta_pincel.png')

    clock = Image.open('images/clock/final_clock.png')
    clock.thumbnail((500, 500), Image.Resampling.LANCZOS)

    background.paste(cavalete, (0 ,0), cavalete)
    background.paste(bolinha, (1047 ,114), bolinha)
    background.paste(eu, (0,0), eu)
    background.paste(pincelPonta, (0,0), pincelPonta)
    background.paste(clock, (535,2), clock)
    
    size = 1280, 720
    background.thumbnail(size)
    background.show()
    background.save('images/thumb/final_thumbnail.png')

def buildContourLinesBlurBackground(color):
    r, g, b, alpha = color

    contuor_lines_img = Image.open('images/thumb/contour-line-rawGrey.png')
    contuor_lines_img.convert('RGBA')

    data = np.array(contuor_lines_img)   # "data" is a height x width x 4 numpy array
    red, green, blue, alpha = data.T # Temporarily unpack the bands for readability

    # Replace white with red... (leaves alpha values alone...)
    white_areas = (red == 255) & (blue == 255) & (green == 255)
    black_areas = (red == 0) & (blue == 0) & (green == 0)
    data[..., :-1][black_areas.T] = (r, g, b) # Transpose back needed

    im2 = Image.fromarray(data)
    im2 = im2.filter(ImageFilter.GaussianBlur(radius = 20))
    im2.save('images/thumb/final_background.png')


def buildBrushHead(color):
    r, g, b, alpha = color

    brushHead = Image.open('images/thumb/pontaPincel.png')
    brushHead.convert('RGBA')

    data = np.array(brushHead)   # "data" is a height x width x 4 numpy array
    red, green, blue, alpha = data.T # Temporarily unpack the bands for readability

    # Replace white with red... (leaves alpha values alone...)
    white_areas = (red == 255) & (blue == 255) & (green == 255)
    black_areas = (red == 0) & (blue == 0) & (green == 0)
    data[..., :-1][black_areas.T] = (r, g, b) # Transpose back needed

    im2 = Image.fromarray(data)
    im2.save('images/thumb/final_ponta_pincel.png')

