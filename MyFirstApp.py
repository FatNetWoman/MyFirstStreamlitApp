#importing modules
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

#import data
data = pd.read_csv('student-mat.csv', sep=';')
pd.set_option('display.max_columns',None)
data.head()

#defining plotly functions
def draw_hist(data):
    fig = px.histogram(data, x='G3')
    return fig
    
def draw_heatmap(data):    
    fig = px.density_heatmap(data, x="age", y="G3", labels={'G3':'Final Grade'}, text_auto=True)
    return fig

def draw_scatter(data):
    fig = px.scatter(data, x="G1", y="G3", color="Medu", size='G3', trendline='ols')
    return fig

def draw_animscatter(data):
    fig = px.scatter(data, x="G1", y="G3", animation_frame="age",
               size="G3", color="Medu",
               log_x=True)
    return fig

def draw_funnel(data):
    fig = px.funnel(data, x='G3', y='Medu')
    return fig

def draw_3dfig(data):
    fig = go.Figure(data=go.Surface(z=data, showscale=True))
    fig.update_layout(
        title='Grades',
        width=400, height=400,
        margin=dict(t=40, r=0, l=20, b=20)
    )
    return fig



#streamlit section

#Title & Page description
st.markdown('## My First Awesome App ')
st.text('To better understand what factors may affect the academic performance of students, \n this page gives multiple types of graphs to visualize the correlation \n between some features from different angles, and then explains it \n from several aspects.  ')

#filter sidebar based on gender
sex = ['M','F','Population']          
option_two = st.sidebar.selectbox('choose your filter based on gender: ', sex)
if option_two == 'M' or option_two =='F':
    gender = data.loc[data['sex'] == option_two]
else:
    gender = data

#defining variables as functions' output
hist = draw_hist(gender)
heatmap = draw_heatmap(gender)
scat = draw_scatter(gender)
animscat = draw_animscatter(gender)
funnel = draw_funnel(gender)
fig_3d = draw_3dfig(gender)

#creating selectbox with multiple plot options
#adding a description button to each plot
lst = ('No Selection', 'Histogram', 'Heatmap', 'Scatter', 'Animated Scatter', 'Funnel', '3D Figure')
option = st.selectbox('Choose your style: ', lst)

if option == 'Histogram':
    st.plotly_chart(hist, use_container_width=True)
    button = st.button('Description')
    if button:
        st.text('This Histogram describes how the value of the final grade \n is distributed along the population (in this case students), \n we can notice that the population follows Normal distribution.')
if option == 'Scatter':
    st.plotly_chart(scat, use_container_width=True)
    button = st.button('Description')
    if button:
        st.text('Scatter plots gives a detailed visualisation of how the first grades \n can predict the upcoming behavior of the student, \n on the other hand another factor may also interfere in the process: Mother Education. \n When colors are more darker means a higher level of mother educational level. ')
if option == 'Animated Scatter':
    st.plotly_chart(animscat, use_container_width=True)
    button = st.button('Description')
    st.text('The animated scatter takes the same concept of the classical scatter plot, \n but with an additional changing factor, the age. \n By clicking on the play button, you can visualize the transformation of the given population \n in terms of age.')
if option == 'Funnel':
    st.plotly_chart(funnel, use_container_width=True)
    button = st.button('Description')
    if button:
        st.text('Funnel is a type of pipe plot. In this case, \n it simply describes how mother education can be an important factor, \n in maintaining the student performance.')
if option == '3D Figure':
    st.plotly_chart(fig_3d, use_container_width=True)
    button = st.button('Description')
    if button:
        st.text('The entire given informations are visualized in this three dimensional figure.\n It is hard to gain any insights, as it is chaotic and almost randomly distributed.')
if option == 'Heatmap':
    st.plotly_chart(heatmap, use_container_width=True)
    button = st.button('Description')
    if button:
        st.text('This graph is called heatmap. We can see how age can affect the overall performance, \n  as if age increase the number of students having a higher grade decrease.')        

#end of the project
#thank you