import streamlit as st
import joblib

#Load the trained model
model = joblib.load("news-classification-model.pkl")

#Define sentiment labels
news_label ={'0':'Technical','1':'Business','2':'Sports','3':'Enterainment','4':'Politics'}

#create strealit app
st.title("News Classification")

#Input text area
user_input = st.text_area("Enter news here:")

#Prediction button
if st.button("Predict"):
    #Perform sentiment prediction
    predicted_label = model.predict([user_input])[0]
    #print("Predicted Label:" + str(predicted_label))
    predicted_news_label=news_label[str(predicted_label)]

    #Display predicted sentiment
    st.info(f"Predicted Label: {predicted_news_label}")
