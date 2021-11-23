import pandas as pd
import streamlit as st
from PIL import Image

st.title("Get Your Best Movie")
image = Image.open('img.png')

df = pd.read_csv(r"imdb_top_1000.csv")
df = df.drop(columns='Poster_Link')
sidebar1=[]
sidebar2=[]
st.set_option('deprecation.showPyplotGlobalUse', False)
st.sidebar.image(image)
radio1 = st.sidebar.radio("IMDB",
                  ("Movie", "Dataset", "Visualize"))
if radio1=="Movie":
    sidebar1 = st.sidebar.selectbox(
        'Genre',
        ('Action', 'Drama', 'Crime', 'Adventure', 'Biography', 'History', 'Sci-Fi', 'Romance', 'Western', 'Western',
         'Fantasy', 'Comedy', 'War', 'Mystery', 'Family', 'Music', 'Horror', 'Sport'))
    sds = sidebar1
elif radio1 == "Dataset":
    st.dataframe(df.style.set_properties(**{'background-color':'black','color':'orange'}))
elif radio1 == "Visualize":
    st.subheader("Top 10 movies according to IMDB Rating")
    sd4 = df.sort_values(by=['IMDB_Rating'], ascending=False)
    sd4 = sd4.set_index('Series_Title')
    st.bar_chart(sd4['IMDB_Rating'][:10])

    st.subheader("Top movies according to Gross")
    sd2 = df.sort_values(by=['Gross'], ascending=False)
    sd3 = sd2.set_index('Series_Title')
    st.bar_chart(sd3['Gross'][:10])

    st.subheader("Movies released ")
    sd2 = df.sort_values(by=['Released_Year'], ascending=False)
    sd3 = sd2.set_index('Series_Title')
    st.bar_chart(sd3['Released_Year'][:40])

    st.subheader("50 Movies according to Runtime ")
    sd2 = df.sort_values(by=['Runtime'])
    sd3 = sd2.set_index('Series_Title')
    st.line_chart(sd3['Runtime'][:50])


def showdata(str):
    st.info('Scroll down to find movie based on IMDB Rating, Released Year and Movie Duration')
    st.header(f"Top {str} movie recommendation based on your preference")
    x1 = pd.DataFrame()
    for i in df['Genre']:
        if (i.count(str) > 0):
            sd = df[(df['Genre'] == i)]
        else:
            continue
        x1 = x1.append(sd)
    x1 = x1.set_index('Series_Title')
    st.dataframe(x1)

    st.subheader("Find movies By:-")
    sidebar2 = st.selectbox("Select",(
                            'IMDB Rating','Movie Duration', 'Released Year'))
    if sidebar2=='IMDB Rating':
        df.set_index('Series_Title')
        first_column = df.pop('IMDB_Rating')
        df.insert(0, 'IMDB_Rating', first_column)
        sd = df.sort_values(by=['IMDB_Rating'], ascending=False)
        sd = sd.set_index('Series_Title')
        st.dataframe(sd)
        st.bar_chart(sd['IMDB_Rating'][:10])

    elif sidebar2=='Movie Duration':
        df.set_index('Series_Title')
        first_column = df.pop('Runtime')
        df.insert(0, 'Runtime', first_column)
        sd = df.sort_values(by=['Runtime'], ascending=False)
        sd = sd.set_index('Series_Title')
        st.dataframe(sd)
        st.bar_chart(sd['IMDB_Rating'][:10])
    elif sidebar2=='Released Year':
        df.set_index('Series_Title')
        first_column = df.pop('Released_Year')
        df.insert(0, 'Released_Year', first_column)
        sd = df.sort_values(by=['Released_Year'], ascending=False)
        sd = sd.set_index('Series_Title')
        st.dataframe(sd)
        st.bar_chart(sd['IMDB_Rating'][:10])

for i in sidebar1:
    if sidebar1==sds:
        showdata(sds)
        break
    else:
        continue
