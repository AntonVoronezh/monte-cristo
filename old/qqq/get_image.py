import PIL
import httplib2
from PIL import Image, ImageEnhance, ImageDraw, ImageFont


# for fn in iglob("c:/Windows/Fonts/*.*"):
#     print(fn)

def get_image(url):
    h = httplib2.Http('.cache')
    response, content = h.request(url)
    out = open('121212.jpg', 'wb')
    out.write(content)
    out.close()

    im = Image.open('121212.jpg')
    im_crop = im.crop((0, 50, 750, 400))
    im_crop.save('121212-2.jpg', quality=95)

    im_contrast = Image.open('121212-2.jpg')
    im_contrast_rotate =im_contrast.transpose(PIL.Image.FLIP_LEFT_RIGHT)
    enhancer = ImageEnhance.Contrast(im_contrast_rotate)
    factor = 1.35
    im_contrast_output = enhancer.enhance(factor)
    enhancer_2 = ImageEnhance.Sharpness(im_contrast_output)
    factor_2 = 1.35
    im_contrast_output_2 = enhancer_2.enhance(factor_2)

    draw = ImageDraw.Draw(im_contrast_output_2)
    font = ImageFont.truetype("trebuc.ttf", size=30)
    # draw.rectangle((0, 310, 750, 350), fill='#ffffff')
    # draw.text((20, 310), 'Я в домике!', '#c49843', font)
    # draw.text((540, 310), '@humans_psy', '#c49843', font)
    # draw.rectangle((0, 0, 750, 35), fill='#ffffff')
    # draw.rectangle((0, 0, 750, 1), fill='#697c42')
    # draw.text((20, 0), 'Я в домике!', '#697c42', font)
    # draw.text((540, 0), '@humans_psy', '#697c42', font)
    draw.ellipse((530, 300, 570, 340), fill='#ffffff')
    draw.ellipse((690, 300, 730, 340), fill='#ffffff')
    draw.rectangle((550, 300, 710, 340), fill='#ffffff')
    draw.text((540, 300), '@humans_psy', '#c49843', font)

    im_contrast_output_2.save('121212-3.jpg')


get_image('https://neurosciencenews.com/files/2016/09/addiction-aging-cognition-neurosciencenews-public.jpg')