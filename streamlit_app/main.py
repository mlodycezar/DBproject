import pandas as pd
import streamlit as st
import insert
import structure
import zipfile
import os
from raporty import Raport
from raporty_html import Raporty_html
from sqlalchemy import create_engine

@st.cache
def convert_df(df):
    return df.to_csv(sep= ';',decimal=',').encode('utf-8')

def zip_files(dic_df,zip_name):
    with zipfile.ZipFile(zip_name+".zip", 'w') as zf:
        for name,df in dic_df.items():
            df.to_csv(f'{name}.csv',encoding='utf-8',index=False)  # this will convert the dataframe to a .csv
            zf.write(f'{name}.csv')  # this will put the .csv in the zipfile
            os.remove(f'{name}.csv')  # this will delete the .csv created

def zip_button(zip_name):
    with open(zip_name+".zip", "rb") as fp:
        btn = st.download_button(
            label="Download ZIP",
            data=fp,
            file_name=zip_name+".zip",
            mime="application/zip")
    os.remove(zip_name+".zip")

engine = create_engine('postgresql://maciek:Test1234!!!!@10.64.10.85:5432/IZ_DB').connect()
choose = st.sidebar.selectbox("Wybierz operację",["Przekształć pliki wejściowe","Wrzuć pliki na serwer","Select","Raporty"])
chooseD = st.sidebar.checkbox("Wyświetl Pliki do pobrania")

if choose == "Wrzuć pliki na serwer":
    st.header("Wrzuć pliki na serwer")
    uploaded_files = st.file_uploader("Proszę wybrać pliki csv", accept_multiple_files=True)
    if st.button("Rozpocznij proces"):
        insert.insert_files(uploaded_files)


elif choose == "Przekształć pliki wejściowe":
    st.header("Przekształć pliki wejściowe")
    uploaded_files = st.file_uploader("Proszę wybrać pliki csv", accept_multiple_files=True)

    if st.button("Rozpocznij proces"):
        data1 = structure.create_structure(uploaded_files)
        mlode = data1[0]
        lochy = data1[1]
        knury = data1[2]
        rozplodowa = data1[3]
        polsus = data1[4]
        if chooseD:
            st.text("Młode")
            st.dataframe(mlode)
            st.text("Lochy")
            st.dataframe(lochy)
            st.text("Knury")
            st.dataframe(knury)
            st.text("Rozplodowa")
            st.dataframe(rozplodowa)
            st.text("Transmisja z polsus")
            st.dataframe(polsus)
        df_dic = {'mlode': mlode,'lochy':lochy,'knury': knury,'rozplodowa': rozplodowa,'transmisja_z_polsus':polsus}
        zip_files(df_dic,"Przeksztalcone_pliki")
        zip_button("Przeksztalcone_pliki")
        st.success("Proces zakończony pomyślnie")
    
elif choose == "Raporty":
    maxDF = pd.read_sql_query("Select max(rok_p) from mlode;",engine)
    rokMax = maxDF['max'][0]
    maxTDF = pd.read_sql_query(f"Select max(tyd_p) from mlode where rok_p = {rokMax};",engine)
    tydMax = maxTDF['max'][0]
    st.header("Raporty")
    wybierz = st.selectbox("Wybierz Raport do wygenerowania",["Raport transmisji",
                                                              "Młode knury hodowlane",
                                                              "Młode lochy hodowlane",
                                                              "Knury stadne",
                                                              "Lochy stadne",
                                                              "Ile chlewni"])
    if wybierz == "Raport transmisji":
        year = st.text_input("Podaj rok")
        week = st.text_input("Podaj tydzień")

        if st.button("Rozpocznij proces"):
            try:
                raport1 = Raport.raport_transmisji(year,week,engine)

                if chooseD:
                    st.text("Raport transmisji")
                    st.text(raport1)

                html_raport_transmisji = open("raport_transmisji.html", "r")
                data = f'_{week}_{year}'
                st.download_button(
                    label='Pobierz plik',
                    data=html_raport_transmisji,
                    file_name=f'raport_transmisji{data}.html',
                    mime='text/html'
                )
            except:
                st.error("Podano błędną wartość!")
                st.warning("Podaj rok i tydzień za pomocą klawiatury numerycznej")




    elif wybierz == "Młode knury hodowlane":

        year = st.text_input("Podaj rok")
        week = st.text_input("Podaj tydzień(początek zakresu)")
        week2 = st.text_input("Podaj tydzień(koniec zakresu)")
        procent = st.text_input("Podaj ile % osobników chcesz brać pod uwagę")
        gender = 1
        if st.button("Rozpocznij proces"):
            try:
                raport2 = Raport.raport_naj_10(gender, year, week, week2, engine, procent)
                raportM = raport2[0]
                raportO = raport2[1]
                dic_df = {"Mateczne":raportM, "Ojcowskie":raportO}
                if chooseD:
                    st.text("Matczyne")
                    st.dataframe(raportM)
                    st.text("Ojcowskie")
                    st.dataframe(raportO)
                #zip_files(dic_df,"Mlode_knury_hodowlane")
                #zip_button("Mlode_knury_hodowlane")
                Raporty_html.mlode_html(gender, year, week,week2)
                html_mlode_knury = open("raport_młode.html", "r")
                data = f'_{week}_{year}'
                pobrane = st.download_button(
                    label='Pobierz plik',
                    data=html_mlode_knury,
                    file_name=f'raport_młode_knury{data}.html',
                    mime='text/html'
                )
                if pobrane:
                    os.remove('raport_młode.html')
            except:
                st.error("Podano błędną wartość!")
                st.warning("Podaj rok i tydzień za pomocą klawiatury numerycznej")





    elif wybierz == "Młode lochy hodowlane":
        try:
            year = st.text_input("Podaj rok")
            week = st.text_input("Podaj tydzień(początek zakresu)")
            week2 = st.text_input("Podaj tydzień(koniec zakresu)")
            gender = 2

            if st.button("Rozpocznij proces"):

                raport2 = Raport.raport_naj_10(gender, year, week, week2, engine, procent=100)
                raportM = raport2[0]
                raportO = raport2[1]
                dic_df = {"Matczyne":raportM, "Ojcowskie":raportO}

                if chooseD:
                    st.text("Matczyne")
                    st.dataframe(raportM)
                    st.text("Ojcowskie")
                    st.dataframe(raportO)

                Raporty_html.mlode_html(gender, year, week, week2)
                html_mlode_lochy = open("raport_młode.html","r")
                data = f'_{week}_{year}'

                pobrane = st.download_button(
                    label='Pobierz plik',
                    data=html_mlode_lochy,
                    file_name=f'raport_młode_lochy{data}.html',
                    mime='text/html'
                    )

                if int(week2) > tydMax:
                    st.warning("Zakres wykracza poza dostępny obszar")
                if pobrane:
                    os.remove('raport_młode.html')
        except:
            st.error("Podano błędną wartość!")
            st.warning("Podaj rok i tydzień za pomocą klawiatury numerycznej")


    elif wybierz == "Knury stadne":
        try:
            year = st.text_input("Podaj rok")
            week = st.text_input("Podaj tydzień")
            gender = 1

            if st.button("Rozpocznij proces"):
                raport3 = Raport.zwh_knurow(year,week,engine)
                rap = convert_df(raport3)
                if chooseD:
                    st.text("Knury stadne")
                    st.dataframe(raport3)

                Raporty_html.stare_html(gender,week,year)
                html_knury = open("raport_stare.html", "r")
                data = f'_{week}_{year}'

                pobrane = st.download_button(
                    label='Pobierz plik',
                    data=html_knury,
                    file_name=f'raport_knury{data}.html',
                    mime='text/html'
                    )
                if pobrane:
                    os.remove('raport_stare.html')
        except:
            st.error("Podano błędną wartość!")
            st.warning("Podaj rok i tydzień za pomocą klawiatury numerycznej")

    elif wybierz == "Lochy stadne":

        year = st.text_input("Podaj rok")
        week = st.text_input("Podaj tydzień")
        gender = 2

        if st.button("Rozpocznij proces"):
            raport4 = Raport.lochy_ujemne_zwh(year,week,engine)
            csv = convert_df(raport4)
            if chooseD:
                st.text("Lochy stadne")
                st.dataframe(raport4)

            Raporty_html.stare_html(gender, week, year)
            html_lochy = open("raport_stare.html", "r")
            data = f'_{week}_{year}'

            pobrane = st.download_button(
                label='Pobierz plik',
                data=html_lochy,
                file_name=f'raport_lochy{data}.html',
                mime='text/html'
            )
            if pobrane:
                os.remove('raport_stare.html')



    elif wybierz == "Ile chlewni":

        year = st.text_input("Podaj rok")
        week = st.text_input("Podaj tydzień")

        if st.button("Rozpocznij proces"):
            raport3 = Raport.ile_chlewni(year, week, engine)
            rap = convert_df(raport3)
            if chooseD:
                st.text("Knury stadne")
                st.dataframe(raport3)

            Raporty_html.ile_chlewni_html(week, year)
            html_knury = open("raport_ile_chlewni.html", "r")
            data = f'_{week}_{year}'

            pobrane = st.download_button(
                label='Pobierz plik',
                data=html_knury,
                file_name=f'raport_ile_chlewni{data}.html',
                mime='text/html'
            )
            if pobrane:
                os.remove('raport_ile_chlewni.html')




