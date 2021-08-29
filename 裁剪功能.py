from PIL import Image
img = Image.open("./2c.jpg")
print(img.size)
cropped = img.crop((8, 205, 1061,1613))  # (left, top, width, height)
cropped.save("./t/pil_cut_thor.jpg")