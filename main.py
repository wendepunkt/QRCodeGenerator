import qrcode
import pandas as pd
from PIL import Image

# saved path
save_path = "/processed/"

# get background image
background_path = "images/background.png"
bg = Image.open(background_path)
bg_w, bg_h = bg.size

# setup vcard format
vcard0 = '''BEGIN:VCARD
VERSION:4.0
FN:'''
vcard1 = '''
TEL;TYPE=cell:'''
vcard2 = '''
END:VCARD'''

# initialise name and phone variables
name = ""
phone = ""

# read_excel export.xlsx
df = pd.read_excel('export.xlsx')
ids = df['id'].tolist()
names = df['first_name'].tolist()
numbers = df['phone'].tolist()

# generate qr code for each tuple in excel sheet
for (id, name, number) in zip(ids, names, numbers):
    # initialise qr code
    qr = qrcode.QRCode(version=1, box_size=8, border=2)
    # add name and number to qr code and convert to image
    qr.add_data((vcard0 + name + vcard1 + str(number) + vcard2))
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    # overlay generated qr code img on background
    img_w, img_h = img.size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    bg.paste(img, offset)
    # save generated image
    bg.save((str(id) + ".png"))