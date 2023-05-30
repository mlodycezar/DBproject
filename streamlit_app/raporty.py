import pandas as pd
import datetime

class Raport:



    def raport_transmisji(year,week,engine):

        query = f"SELECT * FROM transmisja_z_polsus WHERE rok_p = {year} and tyd_p = {week};"
        DF = pd.read_sql(sql=query, con=engine)

        czystoWbp = len(DF[(DF.kro == 10) & (DF.krm == 10)])
        czystoWbpk = len(DF[(DF.kro == 10) & (DF.krm == 10) & (DF.kp == 1)])
        czystoWbpl = len(DF[(DF.kro == 10) & (DF.krm == 10) & (DF.kp == 2)])

        czystoPbz = len(DF[(DF.kro == 20) & (DF.krm == 20)])
        czystoPbzk = len(DF[(DF.kro == 20) & (DF.krm == 20) & (DF.kp == 1)])
        czystoPbzl = len(DF[(DF.kro == 20) & (DF.krm == 20) & (DF.kp == 2)])

        czystoPulawska = len(DF[(DF.kro == 40) & (DF.krm == 40)])
        czystoPulawskak = len(DF[(DF.kro == 40) & (DF.krm == 40) & (DF.kp == 1)])
        czystoPulawskal = len(DF[(DF.kro == 40) & (DF.krm == 40) & (DF.kp == 2)])

        czystoHamp = len(DF[(DF.kro == 60) & (DF.krm == 60)])
        czystoHampk = len(DF[(DF.kro == 60) & (DF.krm == 60) & (DF.kp == 1)])
        czystoHampl = len(DF[(DF.kro == 60) & (DF.krm == 60) & (DF.kp == 2)])

        czystoDuroc = len(DF[(DF.kro == 70) & (DF.krm == 70)])
        czystoDurock = len(DF[(DF.kro == 70) & (DF.krm == 70) & (DF.kp == 1)])
        czystoDurocl = len(DF[(DF.kro == 70) & (DF.krm == 70) & (DF.kp == 2)])

        czystoPietrain = len(DF[(DF.kro == 80) & (DF.krm == 80)])
        czystoPietraink = len(DF[(DF.kro == 80) & (DF.krm == 80) & (DF.kp == 1)])
        czystoPietrainl = len(DF[(DF.kro == 80) & (DF.krm == 80) & (DF.kp == 2)])

        ile_knurki = len(DF.where(DF["kp"] == 1).dropna(how="all"))
        ile_loszki = len(DF.where(DF["kp"] == 2).dropna(how="all"))

        czystorasowe_razem = czystoWbp + czystoPbz + czystoPulawska + czystoHamp + czystoDuroc + czystoPietrain
        czystorasowe_knurki = czystoWbpk + czystoPbzk + czystoPulawskak + czystoHampk + czystoDurock + czystoPietraink
        czystorasowe_loszki = czystoWbpl + czystoPbzl + czystoPulawskal + czystoHampl + czystoDurocl + czystoPietrainl

        dane_razem = [ile_knurki,ile_loszki,czystorasowe_razem,czystorasowe_knurki,czystorasowe_loszki]
        WBPxPBZ = len(DF[(DF.kro == 20) & (DF.krm == 10)])
        WBPxPBZk = len(DF[(DF.kro == 20) & (DF.krm == 10) & (DF.kp == 1)])
        WBPxPBZl = len(DF[(DF.kro == 20) & (DF.krm == 10) & (DF.kp == 2)])

        PBZxWBP = len(DF[(DF.kro == 10) & (DF.krm == 20)])
        PBZxWBPk = len(DF[(DF.kro == 10) & (DF.krm == 20) & (DF.kp == 1)])
        PBZxWBPl = len(DF[(DF.kro == 10) & (DF.krm == 20) & (DF.kp == 2)])

        WBPxPOL = len(DF[(DF.kro == 40) & (DF.krm == 10)])
        WBPxPOLk = len(DF[(DF.kro == 40) & (DF.krm == 10) & (DF.kp == 1)])
        WBPxPOLl = len(DF[(DF.kro == 40) & (DF.krm == 10) & (DF.kp == 2)])

        POLxWBP = len(DF[(DF.kro == 10) & (DF.krm == 40)])
        POLxWBPk = len(DF[(DF.kro == 10) & (DF.krm == 40) & (DF.kp == 1)])
        POLxWBPl = len(DF[(DF.kro == 10) & (DF.krm == 40) & (DF.kp == 2)])

        PBZxPOL = len(DF[(DF.kro == 40) & (DF.krm == 20)])
        PBZxPOLk = len(DF[(DF.kro == 40) & (DF.krm == 20) & (DF.kp == 1)])
        PBZxPOLl = len(DF[(DF.kro == 40) & (DF.krm == 20) & (DF.kp == 2)])

        POLxPBZ = len(DF[(DF.kro == 20) & (DF.krm == 40)])
        POLxPBZk = len(DF[(DF.kro == 20) & (DF.krm == 40) & (DF.kp == 1)])
        POLxPBZl = len(DF[(DF.kro == 20) & (DF.krm == 40) & (DF.kp == 2)])

        DURxPIET = len(DF[(DF.kro == 80) & (DF.krm == 70)])
        DURxPIETk = len(DF[(DF.kro == 80) & (DF.krm == 70) & (DF.kp == 1)])
        DURxPIETl = len(DF[(DF.kro == 80) & (DF.krm == 70) & (DF.kp == 2)])

        PIETxDUR = len(DF[(DF.kro == 70) & (DF.krm == 80)])
        PIETxDURk = len(DF[(DF.kro == 70) & (DF.krm == 80) & (DF.kp == 1)])
        PIETxDURl = len(DF[(DF.kro == 70) & (DF.krm == 80) & (DF.kp == 2)])

        DURxHAMP = len(DF[(DF.kro == 60) & (DF.krm == 70)])
        DURxHAMPk = len(DF[(DF.kro == 60) & (DF.krm == 70) & (DF.kp == 1)])
        DURxHAMPl = len(DF[(DF.kro == 60) & (DF.krm == 70) & (DF.kp == 2)])

        HAMPxDUR = len(DF[(DF.kro == 70) & (DF.krm == 60)])
        HAMPxDURk = len(DF[(DF.kro == 70) & (DF.krm == 60) & (DF.kp == 1)])
        HAMPxDURl = len(DF[(DF.kro == 70) & (DF.krm == 60) & (DF.kp == 2)])

        HAMPxPIET = len(DF[(DF.kro == 80) & (DF.krm == 60)])
        HAMPxPIETk = len(DF[(DF.kro == 80) & (DF.krm == 60) & (DF.kp == 1)])
        HAMPxPIETl = len(DF[(DF.kro == 80) & (DF.krm == 60) & (DF.kp == 2)])

        PIETxHAMP = len(DF[(DF.kro == 60) & (DF.krm == 80)])
        PIETxHAMPk = len(DF[(DF.kro == 60) & (DF.krm == 80) & (DF.kp == 1)])
        PIETxHAMPl = len(DF[(DF.kro == 60) & (DF.krm == 80) & (DF.kp == 2)])

        czystorasoweDic = {
            "Rasa": ["WBP", "PBZ", "PUŁ.", "HAMP.", "DUROC", "PIET."],
            "Razem": [czystoWbp, czystoPbz, czystoPulawska, czystoHamp, czystoDuroc, czystoPietrain],
            "Knurki": [czystoWbpk, czystoPbzk, czystoPulawskak, czystoHampk, czystoDurock,czystoPietraink],
            "Loszki": [czystoWbpl, czystoPbzl, czystoPulawskal, czystoHampl, czystoDurocl,czystoPietrainl]
        }

        mieszanceDic = {
            "Lochy": ['WBP', 'PBZ', 'WBP', 'PUŁ.', 'PBZ', 'PUŁ.', 'DUROC', 'PIET.', 'DUROC', 'HAMP.', 'HAMP.', 'PIET.'],
            "": ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            "Knury": ['PBZ', 'WBP', 'PUŁ.', 'WBP', 'PUŁ.', 'PBZ', 'PIET.', 'DUROC', 'HAMP.', 'DUROC', 'PIET.', 'HAMP.'],
            "Razem": [WBPxPBZ, PBZxWBP, WBPxPOL, POLxWBP, PBZxPOL, POLxPBZ, DURxPIET, PIETxDUR, DURxHAMP, HAMPxDUR,
                      HAMPxPIET, PIETxHAMP],
            "Knurki": [WBPxPBZk, PBZxWBPk, WBPxPOLk, POLxWBPk, PBZxPOLk, POLxPBZk, DURxPIETk, PIETxDURk, DURxHAMPk,
                       HAMPxDURk, HAMPxPIETk, PIETxHAMPk],
            "Loszki": [WBPxPBZl, PBZxWBPl, WBPxPOLl, POLxWBPl, PBZxPOLl, POLxPBZl, DURxPIETl, PIETxDURl, DURxHAMPl,
                       HAMPxDURl, HAMPxPIETl, PIETxHAMPl]
        }

        czystorasoweDF = pd.DataFrame.from_dict(czystorasoweDic)
        mieszanceDF = pd.DataFrame.from_dict(mieszanceDic)

        html = f'''
                    <!DOCTYPE html>
                    <html lang="pl">

                        <head>
                            

                            <title>Raport Transmisji</title>

                        </head>

                        <style>
                            .hr-green {{ 
                                display: block; height: 1px;
                                border: 0; border-top: 3px solid green;}}
                            p.ex1 {{ 
                              padding-left: 50px;
                            }}
                            table {{
                                border-collapse: collapse;
                            }}
                            table, tr, td, th{{
                                padding: 10px;
                                text-align: center;
                                border: none;
                            }}
                            table th, table td{{
                                padding: 5px 25px
                                }}
                            table thead th {{
                                font-size: 15px;
                                font-weight: bold;
                                }}
                            
                        </style>
                        <body>
                            <h1 style="text-align: center;line-height: 50%;"><strong>INSTYTUT ZOOTECHNIKI</strong></h1>
                            <h1 style="text-align: center;line-height: 50%;"><strong>PAŃSTWOWY INSTYTUT BADAWCZY</strong></h1>
                            <h3 style="text-align: center;line-height: 50%;">ZAKŁAD HODOWLI TRZODY CHLEWNEJ</h3>
                            <div style="text-align: center;">ul. Krakowska 1, 32-083 Balice, tel. 666 081 225;agata.bialecka@iz.edu.pl</div>
                            <hr color="black" style="width:100%;text-align:left;margin-left:0;">
                            <p style="line-height: 0%;">&nbsp;</p>
                            <div style="background-color:#e6f2d9;">
                            <hr class="hr-green">
                            <b><p style="text-align: center;line-height: 50%;">EKSPERTYZA NR  <span style="color:
                             #ff0000;">{week}</span>/<span style="color: #ff0000;">{year}</span>/<span style="color: #ff0000;">1</span></p></b>
                            <b><p style="text-align: center;line-height: 50%;">RAPORT TRANSMISJI DANYCH DO IZ PIB z dnia 
                            <span style="color: #ff0000;">{DF['kd'][0]}</span></p></b>
                            
                            
                            <p style="line-height: 0%;">&nbsp;</p>
                            </div>
                            <div style="background-color:#e6f2d9;">
                            <hr class="hr-green">
                            <b><p style="line-height: 50%;">Łączna liczba zwierząt w aktualnej transmisji (Razem/Knurki/
                            Loszki): <span style="color: #ff0000;">{len(DF)}</span>/<span style="color: #ff0000;">
                            {ile_knurki}</span>/<span style="color: #ff0000;">{ile_loszki}</span></p></b>
                            <p style="line-height: 0%;">&nbsp;</p>
                            </div>
                            <div style="background-color:#e6f2d9;">
                            <hr class="hr-green">
                            <b><p style="line-height: 50%;">CZYSTORASOWE:</p></b>
                            
                            <p class="ex1">{czystorasoweDF.to_html(index=False)}</p>
                            <p><b>ŁĄCZNIE </b>(Razem/Knurki/Loszki): {czystorasowe_razem}/{czystorasowe_knurki}/{czystorasowe_loszki}</p>
                            <p style="line-height: 0%;">&nbsp;</p>
                            </div>
                            <p style="line-height: 10%;">&nbsp;</p>

                                <div style="background-color:#EEEEEE;">
                                <hr class="hr-green" >
                                <b><p>MIESZAŃCE DWURASOWE:</p></b>
                                <p class="ex1">{mieszanceDF.to_html(index=False)}</p>
                                <p style="line-height: 50%">Łącznie:  {sum(mieszanceDF.Razem)}</p>
                                <p style="line-height: 0%">&nbsp;</p>

                                </div>

                            <p>&nbsp;</p>
                                <p style="text-align: justify;font-size: 12px">BALICE, DNIA&nbsp; ........................................................
                                &nbsp; &nbsp;.............................................................</p>
                                <p style="font-size: 10px; padding-left: 340px;">(podpis)</p>

                        </body>
                    </html>
                    '''
        with open('raport_transmisji.html', 'w') as f:
            f.write(html)
        return True

    def raport_naj_10(gender, year, week, week2, engine, procent):
        weekList = []
        DFM = pd.DataFrame()
        if int(week) < int(week2):
            for i in range(int(week), 0, -1):
                weekList.append(i)
            for j in range(52, int(week2) - 1, -1):
                weekList.append(j)
        else:
            for k in range(int(week), int(week2) - 1, -1):
                weekList.append(k)
        print(weekList)
        for number in weekList:
            querry = f"SELECT * FROM mlode WHERE rok_p = {year} and tyd_p = {number} and kp = {gender};"
            tempDF = pd.read_sql(sql=querry, con=engine)

            DFM = pd.concat([DFM, tempDF])
            if number == 1:
                year = int(year)-1


        DFM = DFM[(DFM.blup_zwh > 10)]
        wbpDF = DFM[(DFM.rasa == 10)]

        wbpDF = wbpDF[(wbpDF.h_pd >= -3)]
        wbpDF = wbpDF[(wbpDF.h_pm >= -3)]
        wbpDF = wbpDF[(wbpDF.s1 >= 0)]
        wbpDF = wbpDF[(wbpDF.s2 >= 0)]

        pbzDF = DFM[(DFM.rasa == 20)]

        pbzDF = pbzDF[(pbzDF.h_pd >= -3)]
        pbzDF = pbzDF[(pbzDF.h_pm >= -3)]
        pbzDF = pbzDF[(pbzDF.s1 >= 0)]
        pbzDF = pbzDF[(pbzDF.s2 >= 0)]

        pulDF = DFM[(DFM.rasa == 40)]

        pulDF = pulDF[(pulDF.h_pd >= -3)]
        pulDF = pulDF[(pulDF.h_pm >= -3)]
        pulDF = pulDF[(pulDF.s1 >= 0)]
        pulDF = pulDF[(pulDF.s2 >= 0)]

        hampDF = DFM[(DFM.rasa == 60)]

        #hampDF = hampDF[(hampDF.h_pd >= 0)]
        #hampDF = hampDF[(hampDF.h_pm >= 0)]
        #hampDF = hampDF[(hampDF.s1 >= -3)]
        #hampDF = hampDF[(hampDF.s2 >= -3)]

        durocDF = DFM[(DFM.rasa == 70)]

        #durocDF = durocDF[(durocDF.h_pd >= 0)]
        #durocDF = durocDF[(durocDF.h_pm >= 0)]
        #durocDF = durocDF[(durocDF.s1 >= -3)]
        #durocDF = durocDF[(durocDF.s2 >= -3)]

        pitDF = DFM[(DFM.rasa == 80)]

        #pitDF = pitDF[(pitDF.h_pd >= 0)]
        #pitDF = pitDF[(pitDF.h_pm >= 0)]
        #pitDF = pitDF[(pitDF.s1 >= -3)]
        #pitDF = pitDF[(pitDF.s2 >= -3)]

        dic_of_race = {"WBP": wbpDF, "PBZ": pbzDF, "PUL": pulDF, "HAMP": hampDF, "DUROC": durocDF, "PIT": pitDF}

        mateczneDF = pd.DataFrame()
        ojcowskieDF = pd.DataFrame()


        if gender == 1:
            procent = int(procent)
            procent = procent / 100
            for race in dic_of_race:
                cal = len(dic_of_race[race]) * procent
                cal = round(cal)
                if cal == 0:
                    cal = 1
                some_race = dic_of_race[race]
                some_race = some_race.nlargest(cal, 'blup_zwh')
                some_race.drop(some_race.columns.difference(
                    ['nr_zwierz', 'rasa', 'blup_zwh', 'h_pd', 'przyrost', 'h_pm', 'proc_mies', 's1', 's2']), 1,
                               inplace=True)
                if race == "WBP" or race == "PBZ" or race == "PUL":
                    mateczneDF = pd.concat([mateczneDF, some_race])
                else:
                    ojcowskieDF = pd.concat([ojcowskieDF, some_race])

        elif gender == 2:
            for race in dic_of_race:
                cal = len(dic_of_race[race]) * 0.3
                cal = round(cal)
                if cal == 0:
                    cal = 1
                some_race = dic_of_race[race]
                some_race = some_race.nlargest(cal, 'blup_zwh')
                some_race.drop(some_race.columns.difference(
                    ['nr_zwierz', 'rasa', 'blup_zwh', 'h_pd', 'przyrost', 'h_pm', 'proc_mies', 's1', 's2']), 1,
                               inplace=True)
                if race == "WBP" or race == "PBZ" or race == "PUL":
                    mateczneDF = pd.concat([mateczneDF, some_race])
                else:
                    ojcowskieDF = pd.concat([ojcowskieDF, some_race])

        if gender == 1:
            mateczneDF.rename(columns={'blup_zwh': 'ZWH', 'nr_zwierz': 'Nr Knura', 'rasa': 'Rasa',
                                       'h_pd': 'Wart. hod. przyrost dzienny', 'przyrost': 'Przyrost dzienny standaryz.',
                                       'h_pm': 'Wart. hod. % mięsa', 'proc_mies': '% mięsa standaryz.',
                                       's1': 'Wart. hod. I. prosiąt urodz.', 's2': 'Wart. hod I. prosiąt w 21 dniu'},
                              inplace=True)
            ojcowskieDF.rename(columns={'blup_zwh': 'ZWH', 'nr_zwierz': 'Nr Knura', 'rasa': 'Rasa',
                                        'h_pd': 'Wart. hod. przyrost dzienny',
                                        'przyrost': 'Przyrost dzienny standaryz.', 'h_pm': 'Wart. hod. % mięsa',
                                        'proc_mies': '% mięsa standaryz.', 's1': 'Wart. hod. I. prosiąt urodz.',
                                        's2': 'Wart. hod I. prosiąt w 21 dniu'}, inplace=True)
            mateczneDF = mateczneDF.reindex(
                columns=['Nr Knura', 'Rasa', 'ZWH', 'Wart. hod. przyrost dzienny', 'Przyrost dzienny standaryz.',
                         'Wart. hod. % mięsa', '% mięsa standaryz.', 'Wart. hod. I. prosiąt urodz.',
                         'Wart. hod I. prosiąt w 21 dniu'])

            ojcowskieDF = ojcowskieDF.reindex(
                columns=['Nr Knura', 'Rasa', 'ZWH', 'Wart. hod. przyrost dzienny', 'Przyrost dzienny standaryz.',
                         'Wart. hod. % mięsa', '% mięsa standaryz.', 'Wart. hod. I. prosiąt urodz.',
                         'Wart. hod I. prosiąt w 21 dniu'])

        elif gender == 2:
            mateczneDF.rename(columns={'blup_zwh': 'ZWH', 'nr_zwierz': 'Nr Lochy', 'rasa': 'Rasa',
                                       'h_pd': 'Wart. hod. przyrost dzienny', 'przyrost': 'Przyrost dzienny standaryz.',
                                       'h_pm': 'Wart. hod. % mięsa', 'proc_mies': '% mięsa standaryz.',
                                       's1': 'Wart. hod. I. prosiąt urodz.', 's2': 'Wart. hod I. prosiąt w 21 dniu'},
                              inplace=True)

            ojcowskieDF.rename(columns={'blup_zwh': 'ZWH', 'nr_zwierz': 'Nr Lochy', 'rasa': 'Rasa',
                                        'h_pd': 'Wart. hod. przyrost dzienny',
                                        'przyrost': 'Przyrost dzienny standaryz.', 'h_pm': 'Wart. hod. % mięsa',
                                        'proc_mies': '% mięsa standaryz.', 's1': 'Wart. hod. I. prosiąt urodz.',
                                        's2': 'Wart. hod I. prosiąt w 21 dniu'}, inplace=True)

            mateczneDF = mateczneDF.reindex(
                columns=['Nr Lochy', 'Rasa', 'ZWH', 'Wart. hod. przyrost dzienny', 'Przyrost dzienny standaryz.',
                         'Wart. hod. % mięsa', '% mięsa standaryz.', 'Wart. hod. I. prosiąt urodz.',
                         'Wart. hod I. prosiąt w 21 dniu'])
            ojcowskieDF = ojcowskieDF.reindex(
                columns=['Nr Lochy', 'Rasa', 'ZWH', 'Wart. hod. przyrost dzienny', 'Przyrost dzienny standaryz.',
                         'Wart. hod. % mięsa', '% mięsa standaryz.', 'Wart. hod. I. prosiąt urodz.',
                         'Wart. hod I. prosiąt w 21 dniu'])
        mateczneDF['Przyrost dzienny standaryz.'] = mateczneDF['Przyrost dzienny standaryz.'].astype(int)
        ojcowskieDF['Przyrost dzienny standaryz.'] = ojcowskieDF['Przyrost dzienny standaryz.'].astype(int)

        mateczneDF.to_csv("mateczne.csv")
        ojcowskieDF.to_csv("ojcowskie.csv")
        return [mateczneDF,ojcowskieDF]

    def zwh_knurow(year,week,engine):
        query = f"SELECT * FROM knury WHERE rok_p = {year} and tyd_p = {week};"
        DFK = pd.read_sql(sql=query, con=engine)

        DFK = DFK[(DFK.rasa != 90)]
        DFK.drop(DFK.columns.difference(['nr_knura', 'rasa', 'blup_zwh', 'il_potom', 'il_kojarz']), 1, inplace=True)
        DFK.rename(columns={'nr_knura':'Nr Knura'},inplace=True)

        DFK.set_index("Nr Knura", inplace=True)

        year_now = datetime.date.today().year
        year_need = year_now - 5

        for number in DFK.index:
            querryPotomMax = f"SELECT nr_knura,rasa,blup_zwh,il_potom,il_kojarz,tyd_p,rok_p,h_pm,h_pd from knury where rok_p > {year_need} and nr_knura = '{number}';"
            querryCount = f"SELECT count(*) from knury where rok_p > {year_need} and nr_knura = '{number}';"
            countDF = pd.read_sql(sql=querryCount, con=engine)
            count = countDF.iloc[0][0]
            potomMaxDF = pd.read_sql(sql=querryPotomMax, con=engine)
            potomMaxDF.dropna(inplace=True)
            if potomMaxDF.empty:
                continue
            max_potom = max(potomMaxDF['il_potom'])
            temp_varriable = potomMaxDF.where(potomMaxDF['il_potom'] == max_potom).dropna()
            temp_varriable.sort_values(by='blup_zwh', ascending=False, inplace=True)
            max_series = temp_varriable.iloc[0]
            DFK.loc[number, 'il_potom_max_1'] = max_series['il_potom']
            DFK.loc[number, 'il_kojarz_1'] = max_series['il_kojarz']
            DFK.loc[number, 'ZWH_1'] = max_series['blup_zwh']
            DFK.loc[number, 'k_ocena'] = count

            potomMaxDF.dropna(inplace=True)
            max_zwh = max(potomMaxDF['blup_zwh'])
            temp_varriable = potomMaxDF.where(potomMaxDF['blup_zwh'] == max_zwh).dropna()
            max_series = temp_varriable.iloc[0]

            DFK.loc[number, 'il_potom_2'] = max_series['il_potom']
            DFK.loc[number, 'il_kojarz_2'] = max_series['il_kojarz']
            DFK.loc[number, 'ZWH_max_2'] = max_series['blup_zwh']

        DFK = DFK[DFK['k_ocena']>26]

        DFK['rasa'] = DFK['rasa'].astype(int)
        DFK['k_ocena'] = DFK['k_ocena'].astype(int)
        DFK['il_potom'] = DFK['il_potom'].astype(int)
        DFK['il_kojarz'] = DFK['il_kojarz'].astype(int)
        DFK['il_potom_max_1'] = DFK['il_potom_max_1'].astype(int)
        DFK['il_kojarz_1'] = DFK['il_kojarz_1'].astype(int)
        DFK['il_potom_2'] = DFK['il_potom_2'].astype(int)
        DFK['il_kojarz_2'] = DFK['il_kojarz_2'].astype(int)

        DFK = DFK[(DFK.ZWH_1 < 10)]

        DFK.rename(columns={'rasa':'Rasa','k_ocena':'Numer kolejnej oceny','il_potom':'Aktualna liczba potom.',
                            'il_kojarz':'Aktualna liczba kojarzeń','blup_zwh':'Aktualny Blup ZWH',
                            'il_potom_max_1':'Max liczba potom.','il_kojarz_1':'Liczba kojarzeń dla max liczby potom.',
                            'ZWH_1':'ZWH dla max liczby potom.','il_potom_2':'Liczba potom. dla max ZWH',
                            'il_kojarz_2':'Liczba kojarzeń dla max ZWH','ZWH_max_2':'Max ZWH'},inplace=True)

        DFK= DFK[['Rasa','Numer kolejnej oceny','Aktualna liczba potom.','Aktualna liczba kojarzeń','Aktualny Blup ZWH',
                   'Max liczba potom.','Liczba kojarzeń dla max liczby potom.','ZWH dla max liczby potom.',
                   'Liczba potom. dla max ZWH','Liczba kojarzeń dla max ZWH','Max ZWH']]
        DFK = DFK[DFK['Aktualny Blup ZWH'].notna()]
        DFK.sort_values(by=['Rasa', 'ZWH dla max liczby potom.'], ascending=True, inplace=True)
        DFK.to_csv("Stare_stadne.csv",sep=";")

        return DFK

    def lochy_ujemne_zwh(year,week,engine):

        query = f"SELECT * FROM lochy WHERE rok_p = {year} and tyd_p = {week};"
        DFL = pd.read_sql(sql=query, con=engine)

        filterM1 = DFL["rasa"] == 10
        filterM2 = DFL["rasa"] == 20
        filterM3 = DFL["rasa"] == 40
        filterO1 = DFL["rasa"] == 60
        filterO2 = DFL["rasa"] == 70
        filterO3 = DFL["rasa"] == 80

        DFLM = DFL.where(filterM1 | filterM2 | filterM3).dropna()
        DFLO = DFL.where(filterO1 | filterO2 | filterO3).dropna()
        DFLM = DFLM[(DFLM.s1 < 0) & (DFLM.s2 < 0)]
        DFLO = DFLO[(DFLO.h_pd < 0) & (DFLO.h_pm < 0)]
        DFL = pd.concat([DFLM, DFLO])

        DFL.drop(DFL.columns.difference(['nr_lochy', 'rasa', 'blup_zwh', 'blup_miot', 'il_potom', 'il_kojarz']), 1, inplace=True)
        DFL.rename(columns={"nr_lochy":"Nr Lochy"},inplace=True)
        DFL = DFL[(DFL.blup_zwh < 11)]
        DFL.set_index("Nr Lochy", inplace=True)

        year_now = datetime.date.today().year
        year_need = year_now - 10

        for number in DFL.index:
            miot = DFL.loc[[number],'blup_miot']
            miot = miot.tolist()
            miot = miot[0]
            querryPotomMax = f"SELECT nr_lochy, rasa, blup_zwh, il_potom, tyd_p, rok_p, h_pm, h_pd, blup_miot, s1, s2 from lochy where rok_p > {year_need} and nr_lochy = '{number}';"
            potomMaxDF = pd.read_sql(sql=querryPotomMax, con=engine)
            potomMaxDF.dropna(inplace=True)
            if potomMaxDF.empty:
                continue
            #miot = max(potomMaxDF['blup_miot'])
            max_potom = max(potomMaxDF['il_potom'])

            temp_varriable = potomMaxDF.where(potomMaxDF['il_potom'] == max_potom).dropna()
            temp_varriable.sort_values(by=['il_potom','blup_zwh'], ascending=False, inplace=True)
            max_series = temp_varriable.iloc[0]
            if max_series.blup_zwh >= 10:
                continue


            DFL.loc[number, 'h_pd_1'] = max_series['h_pd']
            DFL.loc[number, 'h_pm_1'] = max_series['h_pm']
            DFL.loc[number, 'il_potom_max_1'] = max_series['il_potom']
            DFL.loc[number, 'ZWH_1'] = max_series['blup_zwh']

            DFL.loc[number, 's1'] = max_series['s1']
            DFL.loc[number, 's2'] = max_series['s2']
            potomMaxDF.dropna(inplace=True)
            max_zwh = max(potomMaxDF['blup_zwh'])
            temp_varriable = potomMaxDF.where(potomMaxDF['blup_zwh'] == max_zwh).dropna()
            max_series = temp_varriable.iloc[0]

            DFL.loc[number, 'Miot dla max ZWH'] = max_series['blup_miot']

            DFL.loc[number, 'il_potom_2'] = max_series['il_potom']
            DFL.loc[number, 'ZWH_max_2'] = max_series['blup_zwh']
            DFL.sort_values(by=['rasa', 'blup_zwh'], ascending=True, inplace=True)

        DFL.dropna(inplace=True)

        DFL = DFL[DFL['blup_miot'] > 1]
        DFL['rasa'] = DFL['rasa'].astype(int)

        DFL['blup_miot'] = DFL['blup_miot'].astype(int)
        DFL['il_potom'] = DFL['il_potom'].astype(int)
        DFL['il_potom_max_1'] = DFL['il_potom_max_1'].astype(int)
        DFL['il_potom_2'] = DFL['il_potom_2'].astype(int)
        DFL['Miot dla max ZWH'] = DFL['Miot dla max ZWH'].astype(int)

        DFL = DFL[(DFL.ZWH_1 < 10)]
        DFL = DFL[(DFL.s1 < 0)]
        DFL = DFL[(DFL.s2 < 0)]

        DFL.rename(columns={'rasa': 'Rasa','blup_miot':'Aktualny miot',
                            'il_potom': 'Aktualna liczba potomstwa lochy oceniona przyżyciowo', 'blup_zwh': 'Aktualny Blup ZWH',
                            'h_pd_1':'Blup przyr. dz. dla max liczby potom.',
                            'h_pm_1':'Blup % mięsa dla max liczby potom.','il_potom_max_1': 'Max liczba potomstwa',
                            'ZWH_1':'ZWH dla max liczby potom.',
                            'il_potom_2':'Liczba potomstwa lochy ocenianych przyżyciowo dla MAX ZWH',
                            'ZWH_max_2':'Max ZWH','s1':'Blup dla liczby prosiąt urodzonych',
                            's2':'Blup dla liczby prosiąt odchowanych'}, inplace=True)

        DFL = DFL[['Rasa','Aktualny miot','Aktualna liczba potomstwa lochy oceniona przyżyciowo',
                   'Aktualny Blup ZWH', 'Miot dla max ZWH','Liczba potomstwa lochy ocenianych przyżyciowo dla MAX ZWH',
                   'Max ZWH','Blup przyr. dz. dla max liczby potom.','Blup % mięsa dla max liczby potom.',
                   'Blup dla liczby prosiąt urodzonych','Blup dla liczby prosiąt odchowanych','Max liczba potomstwa',
                   'ZWH dla max liczby potom.'
                   ]]
        DFL.sort_values(by=['Rasa', 'ZWH dla max liczby potom.'], ascending=True, inplace=True)
        DFL.to_csv("Stare_stadne.csv", sep=";")
        return DFL

    def ile_chlewni(year,week,engine):
        query = f"SELECT * FROM knury WHERE rok_p = {year} and tyd_p = {week};"
        DFK = pd.read_sql(sql=query, con=engine)

        DFK = DFK[(DFK.rasa != 90)]
        DFK.drop(DFK.columns.difference(['nr_knura', 'rasa', 'blup_zwh', 'il_potom', 'il_kojarz']), 1, inplace=True)
        DFK.rename(columns={'nr_knura': 'Nr Knura'}, inplace=True)
        DFK.dropna(inplace=True)
        DFK.set_index("Nr Knura", inplace=True)

        year_need = int(year) - 5
        year_needd = datetime.date(year_need, 1, 1)
        date = str(year) + "-W" + str(week)
        r = datetime.datetime.strptime(date + '-1', "%Y-W%W-%w")
        r = str(r)
        r = r[:10]
        for number in DFK.index:
            querryPotomMax = f"SELECT nr_knura,rasa,blup_zwh,il_potom,il_kojarz,tyd_p,rok_p,h_pm,h_pd from knury where rok_p > {year_need} and '{r}' >= kd and nr_knura = '{number}';"
            querryCount = f"SELECT count(*) from knury where rok_p > {year_need} and '{r}' >= kd and nr_knura = '{number}';"
            querryChlewnia = f"Select chlew from mioxx where nroj = '{number}' and '{r}' >= dop"
            querryParowanie = f"Select count(*) from mioxx where nroj = '{number}' and '{r}' >= dop"

            chlewnia = pd.read_sql(sql=querryChlewnia, con=engine)
            chlew = chlewnia.chlew.to_list()
            ile_chlewni = len(set(chlewnia.chlew.to_list()))

            if ile_chlewni>0:
                chlew = chlew[0]
            print(chlew)
            if chlew == []:
                chlew = 0

            countDF = pd.read_sql(sql=querryCount, con=engine)
            count = countDF.iloc[0][0]
            countDF2 = pd.read_sql(sql=querryParowanie, con=engine)
            count2 = countDF2.iloc[0][0]
            potomMaxDF = pd.read_sql(sql=querryPotomMax, con=engine)
            potomMaxDF.dropna(inplace=True)
            if potomMaxDF.empty:
                continue
            max_potom = max(potomMaxDF['il_potom'])
            temp_varriable = potomMaxDF.where(potomMaxDF['il_potom'] == max_potom).dropna()
            temp_varriable.sort_values(by='blup_zwh', ascending=False, inplace=True)
            max_series = temp_varriable.iloc[0]
            DFK.loc[number, 'il_potom_max_1'] = max_series['il_potom']
            DFK.loc[number, 'il_kojarz_1'] = max_series['il_kojarz']
            DFK.loc[number, 'ZWH_1'] = max_series['blup_zwh']
            DFK.loc[number, 'k_ocena'] = count
            DFK.loc[number, 'il_chlewni'] = ile_chlewni
            DFK.loc[number, 'Numer chlewni'] = chlew
            DFK.loc[number, 'Liczba kojarzeń'] = count2

            potomMaxDF.dropna(inplace=True)
            max_zwh = max(potomMaxDF['blup_zwh'])
            temp_varriable = potomMaxDF.where(potomMaxDF['blup_zwh'] == max_zwh).dropna()
            max_series = temp_varriable.iloc[0]

            DFK.loc[number, 'il_potom_2'] = max_series['il_potom']
            DFK.loc[number, 'il_kojarz_2'] = max_series['il_kojarz']
            DFK.loc[number, 'ZWH_max_2'] = max_series['blup_zwh']
        DFK.dropna(inplace=True)
        DFK['rasa'] = DFK['rasa'].astype(int)
        DFK['k_ocena'] = DFK['k_ocena'].astype(int)
        DFK['il_potom'] = DFK['il_potom'].astype(int)
        DFK['il_kojarz'] = DFK['il_kojarz'].astype(int)
        DFK['il_potom_max_1'] = DFK['il_potom_max_1'].astype(int)
        DFK['il_kojarz_1'] = DFK['il_kojarz_1'].astype(int)
        DFK['il_potom_2'] = DFK['il_potom_2'].astype(int)
        DFK['il_kojarz_2'] = DFK['il_kojarz_2'].astype(int)
        DFK['Numer chlewni'] = DFK['Numer chlewni'].astype(int)
        DFK['Liczba kojarzeń'] = DFK['Liczba kojarzeń'].astype(int)
        # DFK['Pozycja'] = DFK['Pozycja'].astype(int)
        DFK.rename(columns={'rasa': 'Rasa', 'k_ocena': 'Numer kolejnej oceny', 'il_potom': 'Aktualna liczba potom.',
                            'il_kojarz': 'Aktualna liczba kojarzeń', 'blup_zwh': 'Aktualny Blup ZWH',
                            'il_potom_max_1': 'Max liczba potom.',
                            'il_kojarz_1': 'Liczba kojarzeń dla max liczby potom.',
                            'ZWH_1': 'ZWH dla max liczby potom.', 'il_potom_2': 'Liczba potom. dla max ZWH',
                            'il_kojarz_2': 'Liczba kojarzeń dla max ZWH', 'ZWH_max_2': 'Max ZWH'}, inplace=True)

        DFK = DFK[
            ['Rasa','Liczba kojarzeń','Numer chlewni', 'Numer kolejnej oceny', 'Aktualna liczba potom.', 'Aktualna liczba kojarzeń', 'Aktualny Blup ZWH',
             'Max liczba potom.', 'Liczba kojarzeń dla max liczby potom.', 'ZWH dla max liczby potom.',
             'Liczba potom. dla max ZWH', 'Liczba kojarzeń dla max ZWH', 'Max ZWH', "il_chlewni"]]
        DFK = DFK[DFK['Aktualny Blup ZWH'].notna()]
        DFK1 = DFK[DFK['il_chlewni'] == 1]
        DFK2 = DFK[DFK['il_chlewni'] > 1]
        del DFK1['il_chlewni']
        del DFK2['il_chlewni']
        del DFK2['Numer chlewni']
        DFK1.sort_values(by=['Rasa', 'ZWH dla max liczby potom.'], ascending=True, inplace=True)
        DFK2.sort_values(by=['Rasa', 'ZWH dla max liczby potom.'], ascending=True, inplace=True)
        DFK1.to_csv("Jedna_chlewnia.csv", sep=";")
        DFK2.to_csv("Wiecej_chlewni.csv", sep=";")

        return DFK