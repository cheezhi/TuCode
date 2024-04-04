'''
Project Name: TuCode
Author: Tutu (版权所有，请勿外传，否则后果自负)
QQ:2093142951
Blog: www.tutime.cn
'''

import string
import random
import webbrowser
import os
import base64

from io import BytesIO
import base64
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def image_to_base64(image: Image.Image, fmt='png') -> str:
    output_buffer = BytesIO()
    image.save(output_buffer, format=fmt)
    byte_data = output_buffer.getvalue()
    base64_str = base64.b64encode(byte_data).decode('utf-8')
    return f'data:image/{fmt};base64,{base64_str}'
    
def create_code():
    # try:
    #     from PIL import Image, ImageDraw, ImageFont, ImageFilter
    # except OSError:
    # 	os.system("pip3 install pillow")
    
    def rndLetter():
        list1 = list(string.ascii_letters+string.digits)
        return random.choice(list1)
    # 随机颜色1:
    def rndColor():
        return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
    
    # 随机颜色2:
    def rndColor2():
        return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
    
    width = 60 * 3+20
    height = 60
    image = Image.new('RGB', (width, height), (255,255,255))
    font = ImageFont.truetype(r'Arial.ttf', 36)
    # emonji_font = ImageFont.truetype(r'Apple Color Emoji.ttf', 1000)
    
    # draw = ImageDraw.Draw(image)
    


    
    nmsb_img = Image.open('nmsb.png')
    # draw = Image.open('bg.png')
    # draw = ImageDraw.Draw(nmsb_img)
    for i in range(15):
        ipnmsb_x, ipnmsb_y = random.randint((-5), 190), random.randint((-5), 5)
        r, g, b, a = nmsb_img.split()
        # nmsb_img = nmsb_img.rotate(random.randint((-90), 90))
        image.paste(nmsb_img,(ipnmsb_x,ipnmsb_y), mask=a)

    
    
    draw = ImageDraw.Draw(image)

    code = ""
    file_name = ""
    
    for t in range(6):
        rnd = rndLetter()
        draw.text((30 * t + 10, 10), rnd, font=font, fill=rndColor2())
        code += rnd
    for t in range(6):
        rnd = rndLetter()
        file_name += rnd
    # 模糊:
    image = image.filter(ImageFilter.SMOOTH)
    
    base64_img = image_to_base64(image)
    
    return base64_img,code,file_name
