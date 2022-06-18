import os
from PIL import Image

mac = Image.open(os.getcwd() + "/jose_portilla/images/example.jpg")
# mac.show()
# print(mac.filename)
# print("mac.format_description", mac.format_description)

print("mac.size", mac.size)  # 1993, 1257
halfway = 1993 / 2
x = halfway - 200
width = halfway + 200

y = 800
height = 1257

# https://pillow.readthedocs.io/en/stable/reference/Image.html
computer = mac.crop((x, y, width, height))
mac.paste(im=computer, box=(0, 0))
# mac.show()
# mac.resize((500, 400)).show()
# mac.rotate(180).show()


###################################################################################################################################################


red = Image.open(os.getcwd() + "/jose_portilla/images/red_color.jpg")
blue = Image.open(os.getcwd() + "/jose_portilla/images/blue_color.png")

newblue = blue.convert("RGB")
newblue.save(os.getcwd() + "/jose_portilla/images/blue_color.jpg")  # new file
blue = Image.open(os.getcwd() + "/jose_portilla/images/blue_color.jpg")

red.putalpha(128)  # does not work on png images
blue.paste(im=red, box=(0, 0), mask=red)
blue.save(os.getcwd() + "/jose_portilla/images/purple.jpg")
# blue.show()


###################################################################################################################################################


word_matrix = Image.open(os.getcwd() + "/jose_portilla/images/word_matrix.png")
mask = Image.open(os.getcwd() + "/jose_portilla/images/mask.png")

mask = mask.resize((1015, 559))
mask.putalpha(200)
word_matrix.paste(mask, (0, 0), mask)
# word_matrix.show()


###################################################################################################################################################
