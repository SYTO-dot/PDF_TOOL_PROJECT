from PIL import Image

img = Image.open("soltech_temp.png")
img.save("soltech_pdf_tool.ico", format="ICO", sizes=[(256, 256)])
