# pillow和pytesseract
from PIL import Image
import pytesseract

# pillow来打开图像
img = Image.open("test2.png")
# 查看这张图像
# img.show()
# 手动指定tesseract的位置
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
text = pytesseract.image_to_string(img)
print(text.strip())