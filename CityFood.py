import streamlit as st
import helper




indian_states = (
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", 
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", 
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", 
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", 
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", 
    "Uttar Pradesh", "Uttarakhand", "West Bengal"
)



st.title('Popular Foods')

place = st.sidebar.selectbox('Pick a place',indian_states)



if place:
    response = helper.generate_city_food(place)
    st.write('**Famous City:**')
    st.header(response['city'])
    foods = response['city_itme'].split(',')
    st.write('**Top Foods**')
    for item in foods:
        st.write("-",item)
