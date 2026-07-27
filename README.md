# 🌱 Crop Disease Detection using Deep Learning

## About the Project

This is a Deep Learning project that I built to detect diseases in crop leaf images.

The user can upload a leaf image, and the model predicts the disease. The application also shows the confidence score, a short description of the disease, and some basic treatment suggestions.

I built this project using TensorFlow, Python, and Streamlit as part of my learning in Deep Learning and Computer Vision.

---

## Features

- Upload a crop leaf image
- Predict the disease using a trained Deep Learning model
- Show prediction confidence
- Display disease description
- Suggest basic treatment
- Simple and easy-to-use interface

---

## Technologies Used

- Python
- TensorFlow / Keras
- Streamlit
- NumPy
- Pillow

---

## Project Structure

```
Crop-Disease-Detection/
│
├── app/
│   └── app.py
│
├── model/
│   └── best_crop_model.keras
│
├── notebook/
│   └── 01_Crop_Disease_Detection.ipynb
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## How to Run

Clone the repository

```bash
git clone <repository-link>
```

Install the required libraries

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app/app.py
```

---

## Supported Classes

- Apple Scab
- Healthy Apple
- Corn Northern Leaf Blight
- Healthy Corn
- Potato Late Blight
- Healthy Potato
- Tomato Early Blight
- Healthy Tomato

---

## Future Improvements

- Add more crop diseases
- Improve the user interface
- Deploy the project online
- Add more disease information

---

## Author

**Aman Khan**
