import pytesseract
from PIL import Image
import os

class OCR:
    def __init__(self):
        self.lang = "eng"
        self.path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        pytesseract.pytesseract.tesseract_cmd = self.path  # Set Tesseract path in init

    def extract(self, filename):
        try:
            # Ensure file exists
            if not os.path.exists(filename):
                return "Error: File not found"

            # Open the image using PIL
            image = Image.open(filename)

            # Extract text from image
            text = pytesseract.image_to_string(image, lang=self.lang)
            return text
        except Exception as e:
            print("Error:", e)
            return "Error"

# Usage
ocr = OCR()
text = ocr.extract("abc.jpg")  # Ensure this file is in the script's directory
print(text)
