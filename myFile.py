import pickle
import streamlit as st

model1 = pickle.load(open('area.pkl','rb'))

def fn():
    st.title("Area Price Prediction")
    area = st.number_input("Enter the value of area : ")
    pred = st.button("Predict")
    if pred:
        res = model1.predict([[area]])
    # show the value 
    st.success("The price of the area is : {}".format(res))
fn()