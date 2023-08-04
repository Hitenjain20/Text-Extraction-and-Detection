import os
import cv2
import pytesseract
import streamlit as st
import numpy as np
from PIL import Image
from pytesseract import Output
#from layoutparser import LayoutParser

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def main():
    st.title("Text Extraction and Detection")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
        text = pytesseract.image_to_string(image)
        st.write("Extracted Text:")
        st.write(text)

        st.write("Text Detection with Bounding Boxes:")
        d = pytesseract.image_to_data(image, output_type=Output.DICT)
        n_boxes = len(d['level'])
        for i in range(n_boxes):
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        st.image(image, channels="BGR")

if __name__ == "__main__":
    main()