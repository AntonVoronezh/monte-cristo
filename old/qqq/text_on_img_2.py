from PIL import Image, ImageDraw, ImageFont

# image = Image.open("2222222.jpg")
# image = Image.new('RGB', (400, 400), color=('#FAACAC'))
#
# font = ImageFont.truetype("badscript.ttf", 25)
# drawer = ImageDraw.Draw(image)
# drawer.text_for_msg((50, 100), "Псилоцибин - природное \nпсиходелическое вещество, \nсодержащееся в \"волшебных грибах\"", font=font, fill='black')
#
# image.save('new_img2.jpg')
# image.show()

# unicode_text = '''Псилоцибин - природное психоделическое вещество'''
# font = ImageFont.truetype("arial.ttf", 28, encoding="unic")
# text_width, text_height = font.getsize(unicode_text)
# canvas = Image.new('RGB', (text_width + 10, text_height + 10), "orange")
# draw = ImageDraw.Draw(canvas)
# # draw.text_for_msg((5, 5), u'Псилоцибин - природное психоделическое вещество', 'blue', font)
# canvas.save("unicode-text_for_msg.png", "PNG")
# canvas.show()


def text_color(output_path):
    image = Image.open(output_path)
    draw = ImageDraw.Draw(image)
    colors = ["green", "blue", "red", "yellow", "purple"]
    font = ImageFont.truetype("comicz.ttf", size=40)
    # y = 100
    # text_for_msg = '''
    # Как смириться
    # с тем, что навсегда
    # потеряла шанс
    # исполнить свою мечту?
    # '''
    # text_for_msg = ['Как смириться с тем,', 'что навсегда потеряла шанс','исполнить свою мечту?']
    # text_for_msg = ['Как смириться с тем,', 'что навсегда потеряла шанс', 'исполнить свою мечту?']
    # text_out = '\n'.join(text_for_msg)

    text = 'Как жить дольше и процветать, делая противоположное'.split(' ')
    arr = [[]]
    count = 0

    for f in text:
        if (count + len(f)) <= 10:
            arr[-1].append(f)
            count = count + len(f)
        else:
            count = 0
            arr.append([f'\n {f}'])

    text_out = ' '.join([j for i in arr for j in i])
    print(text_out)

    draw.text((300, 20), text_out, '#ffffff', font, align ="center")
    image.save(f'{output_path}.png', "PNG")


text_color("back_1.jpg")