import streamlit as st
from PIL import Image
from tensorflow.keras.models import load_model

import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array

st.set_page_config(
    page_title="Crop Disease Detection",
    page_icon="",
    layout="centered"
)

st.title(" Crop Disease Detection")

st.write(
    "Upload a crop leaf image to identify the disease using a trained Deep Learning model."
)

st.info("""
 This application is trained to identify only the following 8 classes:

• Apple Scab
• Healthy Apple
• Corn Northern Leaf Blight
• Healthy Corn
• Potato Late Blight
• Healthy Potato
• Tomato Early Blight
• Healthy Tomato

 Images of crops or diseases outside these classes may produce incorrect predictions.
""")

st.write("Upload a leaf image to detect the disease.")

model = load_model("model/best_crop_model.keras")

uploaded_file = st.file_uploader(
    "Choose a leaf image...",
    type=["jpg", "jpeg", "png"]
)


    
class_names = [
    "Apple___Apple_scab",
    "Apple___healthy",
    "Corn_(maize)___Northern_Leaf_Blight",
    "Corn_(maize)___healthy",
    "Potato___Late_blight",
    "Potato___healthy",
    "Tomato___Early_blight",
    "Tomato___healthy"
]
disease_info = {
    "Apple___Apple_scab": " Apple Scab",
    "Apple___healthy": " Healthy Apple Leaf",
    "Corn_(maize)___Northern_Leaf_Blight": " Corn Northern Leaf Blight",
    "Corn_(maize)___healthy": " Healthy Corn Leaf",
    "Potato___Late_blight": " Potato Late Blight",
    "Potato___healthy": " Healthy Potato Leaf",
    "Tomato___Early_blight": " Tomato Early Blight",
    "Tomato___healthy": " Healthy Tomato Leaf"
}
disease_details = {
    "Apple___Apple_scab": {
        "description": "Apple scab is a fungal disease that causes dark spots on leaves and fruits.",
        "treatment": [
            "Remove infected leaves.",
            "Apply a recommended fungicide.",
            "Prune branches for better airflow."
        ]
    },

    "Apple___healthy": {
        "description": "The apple leaf appears healthy with no visible disease symptoms.",
        "treatment": [
            "Continue regular irrigation.",
            "Monitor for early disease signs.",
            "Maintain balanced fertilization."
        ]
    },

    "Corn_(maize)___Northern_Leaf_Blight": {
        "description": "A fungal disease causing long gray-green lesions on corn leaves.",
        "treatment": [
            "Use resistant hybrids.",
            "Apply fungicide if necessary.",
            "Rotate crops."
        ]
    },

    "Corn_(maize)___healthy": {
        "description": "Healthy corn leaf with no visible infection.",
        "treatment": [
            "Maintain proper nutrition.",
            "Inspect plants regularly."
        ]
    },

    "Potato___Late_blight": {
        "description": "Late blight is a serious fungal-like disease affecting potato leaves.",
        "treatment": [
            "Remove infected plants.",
            "Apply appropriate fungicide.",
            "Avoid excessive moisture."
        ]
    },

    "Potato___healthy": {
        "description": "Healthy potato leaf with no disease symptoms.",
        "treatment": [
            "Continue proper irrigation.",
            "Monitor crop health regularly."
        ]
    },

    "Tomato___Early_blight": {
        "description": "Early blight is a fungal disease that produces brown concentric spots on tomato leaves.",
        "treatment": [
            "Remove infected leaves.",
            "Spray a recommended fungicide.",
            "Avoid overhead watering.",
            "Improve air circulation."
        ]
    },

    "Tomato___healthy": {
        "description": "Healthy tomato leaf with no visible disease.",
        "treatment": [
            "Maintain balanced fertilization.",
            "Water consistently.",
            "Inspect plants regularly."
        ]
    }
}

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Leaf Image",
        use_container_width=True
    )
    image = image.resize((150, 150))
    image_array = img_to_array(image)
    image_array = np.expand_dims(image_array, axis=0)
    image_array = image_array / 255.0

    prediction = model.predict(image_array)

    predicted_class = class_names[np.argmax(prediction)]

    confidence = np.max(prediction) * 100

    st.success(f"Prediction: {disease_info[predicted_class]}")

    st.write(f"Confidence: {confidence:.2f}%")
    st.progress(float(confidence) / 100)

    st.subheader(" Disease Description")

    st.write(disease_details[predicted_class]["description"])

    st.subheader(" Recommended Treatment")

    for tip in disease_details[predicted_class]["treatment"]:
        st.write(f" {tip}")