import random
import os
from PIL import Image, ImageFont, ImageDraw
import textwrap

out_image_path="./ready_images/"
finalsize=(600,600)
def draw(image, quote, filename):
    img = Image.open("./raw-images/"+image) 
    img.thumbnail(finalsize)
    draw = ImageDraw.Draw(img)
    para=textwrap.wrap(quote, width=40)
    font = ImageFont.truetype("./fonts/VeraBd.ttf", img.size[0]//30)
     
    current_h, pad = 10,10
    for line in para:
        w, h = draw.textsize(line, font=font)
        current_width=(finalsize[0]-w)/2
        for x in range(-3,4):
            for y in range(-3,4):
                draw_y=current_h+y
                draw.text((current_width+x, draw_y), line, font=font, fill="black")
        draw_y = current_h
        draw.text((current_width, draw_y), line ,font=font, fill="white")
        current_h += h+pad
    img.save(filename)


def draw_random_quote_on_random_image(filename):
    quote = random.choice(QUOTES)
    image = random.choice(IMAGES)
    return draw(image, quote, filename)

QUOTES=[]
i = open("./quotes1.csv", "r")
for lines in  i:
    QUOTES.append(lines.strip())

IMAGES=os.listdir("./raw-images")

filename_count=1
for I in IMAGES:
    for Q in QUOTES:
        draw(I,Q,out_image_path+str(filename_count)+".jpg")
        filename_count+=1
        
