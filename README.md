# Crop Disease Detection using Deep Learning

A deep learning-based web application that detects crop leaf diseases from images using TensorFlow and Keras. Users can upload a leaf image, and the application predicts the disease along with the confidence score, disease description, and recommended treatment.

---

## Live Demo

 https://crop-disease-detection-aman.streamlit.app/

---




## Features

- Upload crop leaf images
- Detect crop diseases using a Deep Learning model
- Display prediction confidence
- Show disease description
- Recommend treatment suggestions
- Clean and interactive Streamlit interface
- Supports 8 crop disease/healthy classes

---

##  Supported Classes

| Crop | Class |
|------|------|
|  Apple | Apple Scab |
|  Apple | Healthy Apple |
|  Corn | Northern Leaf Blight |
|  Corn | Healthy Corn |
|  Potato | Late Blight |
|  Potato | Healthy Potato |
|  Tomato | Early Blight |
|  Tomato | Healthy Tomato |

---

##  Tech Stack

- Python
- TensorFlow
- Keras
- NumPy
- Pillow
- Streamlit
- Google Colab
- Git
- GitHub

---

##  Project Structure

```text
Crop-Disease-Detection/
│
├── app/
│   └── app.py
│
├── model/
│   └── best_crop_model.keras
│
├── notebook/
│   └── Crop_Disease_Detection.ipynb
│
├── images/
│   └── app_demo.png
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/amankhan292002/Crop-Disease-Detection.git
```

Move into the project directory

```bash
cd Crop-Disease-Detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app/app.py
```

---

## Model Information

- Framework: TensorFlow / Keras
- Task: Image Classification
- Input Image Size: **150 * 150** * 3
- Output: Disease Class + Confidence Score

The model predicts the most probable disease class among the supported categories and displays the prediction confidence.

---

## How It Works
1.Pick a crop leaf and Resize the image to 150*150*3

2. Upload a crop leaf image.
 
3. The image is resized and preprocessed.
 
4. The trained deep learning model performs prediction.
 
5. The application displays:
   - Predicted disease
   - Confidence score
   - Disease description
   - Recommended treatment

---

## Current Limitations

- The application supports only the eight trained classes.
- Images from unsupported crops or diseases may produce incorrect predictions.
- Prediction confidence depends on image quality, lighting conditions, viewing angle, and disease severity.

---

## Future Improvements

- Support more crop species
- Add more plant diseases
- Disease severity estimation
- Multilingual support
- Mobile-friendly interface
- Better confidence calibration

---

## Contributing

Contributions are welcome.

If you would like to improve this project, feel free to fork the repository, make your changes, and submit a pull request.

---

## Author

**Aman Khan**

GitHub:
https://github.com/amankhan292002

---
