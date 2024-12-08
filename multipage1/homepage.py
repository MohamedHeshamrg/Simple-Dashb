import streamlit as st
import plotly.express as px 



st.set_page_config(
    layout="wide",
    page_title='Tips HomePage',
    page_icon='🪙'
)

df = px.data.tips()

## side bar 
st.sidebar.success('Select Page Above')
x = st.sidebar.checkbox('Show Data', True, key=1)
st.markdown('<h1 style="text-align: center; color : cyan;">Home Page For Dash Board</h1>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([3,4, 3])
with col2:
    if x:
        st.markdown('<h3 style="text-align: center; color : MediumAquaMarine;">Dataset</h3>', unsafe_allow_html=True)
        st.dataframe(df.copy(), 800, 500)

