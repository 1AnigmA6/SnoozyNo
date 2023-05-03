import streamlit as st

st.title("Dataset")


st.markdown("""
The dataset used to train the model consists of images of eyes divided into two classes of open and closed.
The dataset used was split into two parts of training and validation.
Training was 80 percent of the dataset
Validation was 20 percent of the dataset

Model was trained on 84898 images which was divided into
Training - 64919 images
Validation - 16979 images

The images were trained in batch sizes of 32, which means 32 images were trained in a single batch together.
""")


datasetimg = ["images\s0001_01770_0_1_0_2_0_01.png","images\s0001_01782_0_1_0_0_0_01.png","images\s0001_01919_0_0_1_0_0_01.png","images\s0001_01924_0_0_1_0_0_01.png"]
st.write("The following are some images that are part of the dataset:")
st.image(datasetimg, width=100)

st.title("Model Training")
st.subheader("Algorithm used is Convolutional Neural Network")
st.image("images\\cnn.jpg")
st.markdown("""
Convolutional Neural Network(CNN) is a Deep Learning algorithm that can take in an input image, assign importance (learnable weights and biases) to various aspects/objects in the image, and be able to differentiate one from the other. The pre-processing required in a ConvNet is much lower as compared to other classification algorithms. While in primitive methods filters are hand-engineered, with enough training, ConvNets have the ability to learn these filters/characteristics.
""")


st.title("Accuracy over Epochs")
st.markdown("The below graph shows the accuracy and validation accuracy per epoch during training the model used for this project:")
st.image("images\LoE.jpg")

st.title("Loss over Epochs")
st.markdown("The below graph plots the loss and validation loss per epoch during training the model used for this project:")
st.image("images\AoE.jpg")