try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\ASUS\anaconda3\Library\bin\tesseract.exe"

def main():
    text_from_image = pytesseract.image_to_string(Image.open('test_image.png'))
    arr = text_from_image.split('\n')[0:-1]
    text_from_image = '\n'.join(arr)
    print(text_from_image)
    return text_from_image

if __name__ == '__main__':
    main()