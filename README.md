# Text-Extraction-and-Detection

![image 30-03-2022 20_00_49](https://github.com/Hitenjain20/Text-Extraction-and-Detection/assets/84326121/b210f502-4a83-4b41-ad41-dc6fe52dd1c8)


# Overview #


Text Extraction from Images is an efficient application that allows users to extract text from images using the powerful combination of Pytesseract, OpenCV, Pillow, NumPy, and Streamlit. The application utilizes Pytesseract for text recognition, and it leverages the capabilities of NumPy, OpenCV, and Pillow to detect and draw bounding boxes around the recognized text regions.


# Features #


* Extract text from images using Pytesseract.
* Detect and draw bounding boxes around text regions using NumPy, OpenCV, and Pillow.
* User-friendly interface powered by Streamlit.


# Installations #


* `pip install pytesseract`
* `pip install opencv-python`
* `pip install pillow`
* `pip install numpy`
* `pip install streamlit`


Install Tesseract OCR (https://github.com/tesseract-ocr/tesseract) for text recognition:

# For Ubuntu
* 'sudo apt-get install tesseract-ocr'
# For Mac
* 'brew install tesseract'
# For Windows
### Download installer from: https://github.com/tesseract-ocr/tesseract ###



# Usage #


Run the Streamlit application:

* 'streamlit run app.py'

* Access the application at http://localhost:8501 in your web browser.
* Upload an image to the application and click on the "Extract Text" button.
* View the extracted text and the image with bounding boxes around the detected text regions.


