from PIL import Image
from PIL import ImageFilter #濾波
import pytesseract #OCR光學套件
from matplotlib import pyplot as plt
def deal(path):
    pil_image = Image.open(path)

    #濾波 #深度平滑濾波,會使得影象變得更加平滑
    pil_image = pil_image.filter(ImageFilter.SMOOTH_MORE)
    # pil_image = pil_image.filter(ImageFilter.SMOOTH)
    # 灰度
    pil_image = pil_image.convert('L')
    #二值化
    threshhole = 129 #二值化
    table = []
    for i in range(256):
        if i < threshhole:
            table.append(0)
        else:
            table.append(1)
    pil_image = pil_image.point(table,'1')
    # plt.imshow(pil_image, cmap='gray')
    # plt.show()

    text = pytesseract.image_to_string(pil_image, lang='eng')
    return text

# deal('captcha.png')

