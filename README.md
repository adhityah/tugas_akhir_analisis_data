# Pengaruh hujan pada partikel PM2.5 dan PM10

Data yang digunakan pada project ini adalah data dari tahun 2014-2016 pada 12 statiun cuaca China yang diambil pada [sumber berikut]('https://github.com/marceloreis/HTI/tree/master/PRSA_Data_20130301-20170228')

Project dibuat dengan menggunakan bahasa Pyhton dengan versi Python 3.10.6

```
pip install pandas matplotlib seaborn numpy streamlit altair pyplot
```


## Dashboard

Dashborad ini merupakan dashborad kualitas partikel PM2.5 dan PM10 terhadap hujan.
Di dalam dashboard ini terdapat grafik pengaruh hujan pada partikel PM2.5 dan PM10 yang ditampilkan secara perbulan.
Selain itu ada grafik yang menampilkan kondisi partikel PM2.5 dan PM10 dengan ada hujan atau tidak.
Trakhir, terdapat grafik partikel PM2.5 dan PM10 terhadap intensitas hujan yang dibagi menjadi 5 klasifikasi, yaitu:

- light rain/Hujan Ringan (LR)        =   0 < R < 1.5  
- moderate rain/Hujan Sedang (MR)     =   1.5 <= R < 3.5 
- heavy rain/Hujan Deras (HR)         =   3.5 <= R < 8.0
- torrential rain/Hujan Lebat (TR)    =   8.0 <= R < 20
- downpour/Hujan Sangat Lebat (SR)    =   R > 20





### Run streamlit app

```
streamlit run dashboard/dashboard.py
```

### Preview

Dashboard Kualitas Partikel PM2.5 dan PM10 Terhadap Hujan dapat dikses pada [https://app-aqi-project-brew.streamlit.app/](https://app-aqi-project-brew.streamlit.app/)


![preview-dashboard](/preview-dashboard.png)

