from PIL import Image, ImageDraw, ImageFont
import pandas as pd

data = pd.read_csv("data.csv")
color = (0, 137, 209)
font_size = 85

# (width, height) 
name_location = (700, 790)
class_location = (450,870)
year_location = (1200,870)
font_used="./AlexBrush-Regular.ttf"

class_list = data["class"].tolist()
year_list = data["year"].tolist()

for i,name in enumerate(data["name"]):
    img = Image.open("cert.jpg")
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_used, font_size, encoding="unic")
    d.text(name_location, name, fill=color, font=font)
    d.text(class_location, class_list[i], fill=color, font=font)
    d.text(year_location, year_list[i], fill=color, font=font)
    img.convert("RGB").save(f"./certs/{name}.pdf")