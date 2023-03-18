import streamlit as st
import pickle
import helper
from PIL import Image

model = pickle.load(open('model.pkl','rb'))

st.subheader(":red[Quora] Question Pairs") 
st.markdown('_To identify :blue[question pairs] that have the same intent_ ? :sunglasses:')
#put your own image here
image = Image.open('QuoraLogoForGreenhouse_3.png')
st.image(image, width=300)

#model = pickle.load(open('model.pkl','rb'))

st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    result = model.predict(query)[0]

    if result == 1:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')