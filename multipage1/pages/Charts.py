import streamlit as st
import plotly.express as px
st.set_page_config(
        layout = 'wide',
        page_title = 'DashBoard',
        page_icon= '📊'
)

tab1, tab2 = st.tabs(['📈 Describtive Stats','📊 Charts'])
df = px.data.tips()
num = df.describe()
cat = df.describe(include = 'O')

with tab1:
    col1, col2, col3 = st.columns([6,0.5,6])
    with col1:
        st.subheader('Numerical Describtive Statistics')
        st.dataframe(num.T, 700, 150)
    with col3:
        st.subheader('Categorical Describtive Statistics')
        st.dataframe(cat, 500, 200)
with tab2:
    day = st.sidebar.selectbox("Select Day", df['day'].unique())
    time = st.sidebar.selectbox('select Meal Time', df['time'].unique())
    size = st.sidebar.radio('Select How many Dishes', sorted(df['size'].unique()), 3, horizontal=True)
    col1, col2, col3 = st.columns([5,1, 5])
    with col1:
        new_df1 = df[df['day'] == day]
        fig = px.histogram(new_df1, x = 'total_bill', color = 'sex',
                           title=f'totalt bill for {day}day'.title(), color_discrete_sequence=px.colors.qualitative.Bold)
        st.plotly_chart(fig,use_container_width=True)
        
        
        new_df2 = df[df['time'] == time]
        fig = px.scatter(new_df2, x='total_bill', y = 'tip', size = 'size', size_max=20,color = 'sex',
                         title=f'correlation between total bill and tips on {time}', color_discrete_sequence=px.colors.qualitative.Bold)
        st.plotly_chart(fig,use_container_width=True)
        
    with col3:
        new_df1 = df[df['size'] == size]
        fig = px.pie(new_df1, names = 'time', color = 'sex',
                     title=f'count of each meal time according to {size} dishes'.title(),
                     color_discrete_sequence=px.colors.qualitative.Bold).update_traces(textinfo='value')
        st.plotly_chart(fig,use_container_width=True)
        
        
        fig = px.treemap(df, path= ['day', 'time', 'size'], color = 'tip',
                          title=f'counting over day, time and size over tips'.title(),color_continuous_scale= px.colors.sequential.Mint)
        st.plotly_chart(fig,use_container_width=True)
