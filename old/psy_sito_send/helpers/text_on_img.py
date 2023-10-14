from PIL import Image, ImageDraw, ImageFont
import os

def text_on_image(img_back_folder_path, img_folder_path, new_file_name, title):
    item_path = os.path.join(img_back_folder_path, new_file_name)
    print(item_path)
    image = Image.open(item_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("comicz.ttf", size=40)

    text = title.split(' ')
    arr = [[]]
    count = 0

    print(len(arr))
    # x = 250
    # y = 20
    x = 250
    y = 30



    for f in text:
        if (count + len(f)) <= 10:
            arr[-1].append(f)
            count = count + len(f)
        else:
            count = 0
            arr.append([f'{f}\n'])

    text_out = ' '.join([j for i in arr for j in i])

    # if len(arr) == 3:
    #     x = 250
    #     y = 50
    # if len(arr) == 4:
    #     x = 250
    #     y = 40
    # if len(arr) == 5:
    #     x = 250
    #     y = 30
    # if len(arr) == 6:
    #     x = 200
    #     y = 20
    # if len(arr) == 7:
    #     x = 200
    #     y = 10

    draw.text((x, y), text_out.strip(), '#ffffff', font, align="left")
    image.save(f'{img_folder_path}/{new_file_name}.png', "PNG")



