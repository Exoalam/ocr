import easyocr

# Create an EasyOCR reader object
reader = easyocr.Reader(['en'])  # specify the language(s) to recognize

# Load the image
image_path = "bottle_mark.png"

# Apply OCR
results = reader.readtext(image_path)

# Print the detected text
for result in results:
    print(result[1])