try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract

# Ensure the tesseract_cmd path is properly formatted
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def recText(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text

#info = recText('text.jpg')
info = recText('D:/30 days master class/AI_30_DAYS/day 17/text.jpg')

print(info)

file = open("New.txt", "w")
file.write(info)
file.close()
print("Written Successfully")
