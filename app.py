import torch
from prediction import predict
import streamlit as st
import urllib.request

st.title("Face Image Classifier")
st.subheader("Load Images")
st.text("Upload an image")

image_url = st.text_input('Enter Face Image URL to classify.. ',
                         'http://cdn.shopify.com/s/files/1/0094/0716/8559/products/1_0ae8a2c4-99a3-4f8e-afa8-fd621903f534.jpg?v=1618893103 ')

# if not image_url:
#     return None

urllib.request.urlretrieve(image_url, "image.png")

model = torch.load("model.pt")
result = predict(model, 'image.png')

st.image(result[0])
st.write(result[1])