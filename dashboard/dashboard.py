import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
import altair as alt


df = pd.read_csv('dashboard/main_data.csv')



with st.sidebar:
    st.header('Filter:')
    year_filter = st.sidebar.multiselect(
        "Tahun:",
        options=df["year"].unique(),
        default=df["year"].unique()
    )

    st_filter = st.sidebar.multiselect(
        "Stasiun Air Quality:",
        options=df["station"].unique(),
        default=df["station"].unique()
    )


df_data = df.query(
    "station == @st_filter & year == @year_filter"
)


with st.container():    
    st.header('Dashborad Kualitas Partikel PM2.5 dan PM10 Terhadap Hujan')

    st.subheader('Pengaruh hujan pada partikel PM2.5 dan PM10')
    df_summary = df_data.groupby(['month'], as_index=False).agg({
        'PM2.5' : 'mean',
        'PM10' : 'mean',
        'RAIN' : 'sum' 
    })

    df_partikel = pd.melt(df_summary, id_vars='month', value_vars=['PM2.5','PM10'], var_name='partikel_name', value_name='partikel_value')

    partikel = alt.Chart(df_partikel).mark_line(point=True).encode(
        x=alt.X('month',title='Bulan Januari - Desember'),
        y='partikel_value',
        color='partikel_name'
    )

    hujan = alt.Chart(df_summary).mark_line(point=True).encode(
        x='month',
        y='RAIN',
        color=alt.value("#FFAA00")
    )

    graph_line = alt.layer(partikel, hujan).resolve_scale(
        y='independent'
    )

    st.altair_chart(graph_line, use_container_width=True)






    st.subheader('Kondisi partikel PM2.5 dan PM10 saat ada hujan atau tidak')
    
    col1, col2 = st.columns([1, 1])

    df_tanpa_hujan = df_data[df_data['RAIN'] > 0.0]
    df_dengan_hujan = df_data[df_data['RAIN'] == 0.0]


    df_tanpa_rekap_hujan = df_tanpa_hujan.groupby(['month'], as_index=False).agg(
        avg_PM25=('PM2.5','mean'),
        avg_PM10=('PM10','mean')
    )

    print(df_tanpa_rekap_hujan.info())

    df_dengan_rekap_hujan = df_dengan_hujan.groupby(['month'], as_index=False).agg(
        avg_PM25=('PM2.5','mean'),
        avg_PM10=('PM10','mean')
    )

    with col1:
        pm25_dengan_hujan = alt.Chart(df_dengan_rekap_hujan).mark_line(point=True).encode(
            x=alt.X('month',title='Bulan Januari - Desember'),
            color=alt.value("#FFAA00"),
            y=alt.Y('avg_PM25',title='Rata-Rata PM2.5')
        )

        pm25_tanpa_hujan = alt.Chart(df_tanpa_rekap_hujan).mark_line(point=True).encode(
            x='month',
            y='avg_PM25',
        )

        graph_line_pm25 = alt.layer(pm25_dengan_hujan, pm25_tanpa_hujan)

        st.altair_chart(graph_line_pm25, use_container_width=True)
    
    with col2:
        pm10_dengan_hujan = alt.Chart(df_dengan_rekap_hujan).mark_line(point=True).encode(
            x=alt.X('month',title='Bulan Januari - Desember'),
            color=alt.value("#FFAA00"),
            y=alt.Y('avg_PM10',title='Rata-Rata PM10')
        )

        pm10_tanpa_hujan = alt.Chart(df_tanpa_rekap_hujan).mark_line(point=True).encode(
            x='month',
            y='avg_PM10',
        )

        graph_line_pm10 = alt.layer(pm10_dengan_hujan, pm10_tanpa_hujan)

        st.altair_chart(graph_line_pm10, use_container_width=True)





    st.subheader('Intensitas hujan terhadap partikel PM2.5 dan PM10')

    def rain_classification(rain):
        if rain >= 0 and rain < 1.5:
            return "Light Rain"
        elif rain >= 1.5 and rain < 3.5:
            return "Moderate Rain"
        elif rain >= 3.5 and rain < 8.0:
            return "Heavy Rain"
        elif rain >= 8.0 and rain < 20.0:
            return "Torrential Rain"
        else:
            return 'Downpour'
        
    df_rain_class = df_data;
    df_rain_class['class'] = df_rain_class['RAIN'].apply(rain_classification)

    df_rekap_rain = df_rain_class.groupby(['class']).agg(
        avg_PM25=('PM2.5','mean'),
        avg_PM10=('PM10','mean')
    )

    


    df_rekap_rain = df_rekap_rain.reindex(['Light Rain','Moderate Rain','Heavy Rain','Torrential Rain','Downpour'])
    df_rekap_rain.reset_index(inplace=True)

    df_rekap_rain_melt = pd.melt(
                            df_rekap_rain, 
                            id_vars='class', value_vars=['avg_PM25','avg_PM10'], var_name='partikel_name', value_name='nilai')
    

    partikel = alt.Chart(df_rekap_rain_melt).mark_line(point=True).encode(
        x=alt.X('class',title='Klasifikasi Intensitas Hujan',sort=['Light Rain','Moderate Rain','Heavy Rain','Torrential Rain','Downpour']),
        y=alt.Y('nilai',title='Jumlah partikel'),
        color='partikel_name'
    )

    st.altair_chart(partikel, use_container_width=True)
