import pandas as pd

class Raporty_html:
    def mlode_html(gender, year, week, week2):
        mateczneDF = pd.read_csv("mateczne.csv", index_col=False)
        ojcowskieDF = pd.read_csv("ojcowskie.csv", index_col=False)
        del mateczneDF['Unnamed: 0']
        del ojcowskieDF['Unnamed: 0']
        dicL = {"Rasa":["WBP","PBZ","DUROC","PIET.","HAMP."],
                "Przyrost dzienny":[680,680,750,700,750],
                "% mięsa":[58,58,62,64,62],}
        referencyjneL = pd.DataFrame.from_dict(dicL)
        dicK = {'Rasa':['WBP','PBZ','DUROC','PIET.','HAMP.'],
                'Przyrost dzienny':[750,750,800,750,800],
                '% mięsa':[60,60,63,65,63]}
        referencyjneK = pd.DataFrame.from_dict(dicK)

        weekList = []
        week = int(week)
        week2 = int(week2)
        year = int(year)
        
        if week < week2:
            for i in range(week, 0, -1):
                weekList.append(i)
            for j in range(52, week2 - 1, -1):
                weekList.append(j)
        else:
            for k in range(week, week2 - 1, -1):
                weekList.append(k)
        if week < week2:
            yearStr = f"{year},{year-1}"
        else:
            yearStr = year

        weekList.sort()
        weekStr = ''
        dl = len(weekList) - 1
        licznik = 0
        for i in weekList:
            weekStr = weekStr + str(i)
            if licznik < dl:
                weekStr += ', '
            licznik += 1





        if gender == 1:
            html = f'''
                <!DOCTYPE html>
                <html lang="pl">
            
                    <head>
            
            
                        <title>Młode Knury</title>
            
                    </head>
                    <style type="text/css">
                      
                      table {{
                          font-family: Arial, Helvetica, sans-serif;
                          width: 100%;
                          text-align: center;
                          border-collapse: collapse;
                        }}
                        table td, table th {{
                          padding: 3px 2px;
                          border: 3px solid #FFFFFF
                        }}
                        table tbody td {{
                          font-size: 10px;
            
                        }}
                        table tr:nth-child(even) {{
                          background: #DEF1DC;
                        }}
                        table thead {{
                          background: #4F7849;
                          background: -moz-linear-gradient(top, #7b9a76 0%, #60855b 66%, #4F7849 100%);
                          background: -webkit-linear-gradient(top, #7b9a76 0%, #60855b 66%, #4F7849 100%);
                          background: linear-gradient(to bottom, #7b9a76 0%, #60855b 66%, #4F7849 100%);
                        }}
                        table thead th {{
                          font-size: 12px;
                          font-weight: bold;
                          color: #FFFFFF;
                          text-align: center;
                        }}
                        table tfoot td {{
                          font-size: 21px;
                        }}
                        .hr-green {{ 
                            display: block; height: 1px;
                            border: 0; border-top: 3px solid green;}}
                    </style>
            
            
                    <body>
                        <h1 style="text-align: center;line-height: 50%;"><strong>INSTYTUT ZOOTECHNIKI</strong></h1>
                        <h1 style="text-align: center;line-height: 50%;"><strong>PAŃSTWOWY INSTYTUT BADAWCZY</strong></h1>
                        <h3 style="text-align: center;line-height: 50%;">ZAKŁAD HODOWLI TRZODY CHLEWNEJ</h3>
                        <div style="text-align: center;">ul. Krakowska 1, 32-083 Balice, tel. 666 081 225;agata.bialecka@iz.edu.pl</div>
                        <hr color="black" style="width:100%;text-align:left;margin-left:0;color:black">
                        <div style="text-align: center;">&nbsp;</div>
                        <div style="background-color:#e6f2d9;">
                        <hr class="hr-green">
                        <b><p style="text-align: center;line-height: 50%;">EKSPERTYZA NR  <span style="color:
                        #ff0000;">{week}</span>/<span style="color: #ff0000;">{year}</span>/
                        <span style="color: #ff0000;">2</span></p></b>
                        <div style="text-align: center;">&nbsp;</div>
                        <div style="text-align: center;">W ZAKRESIE REKOMENDACJI <span style="color: #ff0000;">20%</span>
                         NAJLEPSZYCH <b>MŁODYCH KNURÓW HODOWLANYCH</b> ZE WZGLĘDU NA OSZACOWANĄ ZBIORCZĄ WARTOŚĆ HODOWLANA
                          (<span style="color: #ff0000;">ZWH<span style="color: #000000;">)</span></span></div>
                        <div style="text-align: center;">&nbsp;</div>
                        </div>
                        <div>&nbsp;</div>
                        <div style="background-color:#e6f2d9;">
                        <hr class="hr-green">
                        RANKING MŁODYCH KNUR&Oacute;W HODOWLANYCH  POD WZGLĘDEM <span style="color: #ff0000;">ZWH</span>
                        <div>&nbsp;</div>
                        </div>
                        <div>&nbsp;</div>
                        <b><span style="color: #ff0000;">RASY MATECZNE<span style="color: #000000;"></b>
                        {mateczneDF.to_html(index=False)}
                        <b><span style="color: #ff0000;">RASY OJCOWSKIE<span style="color: #000000;"></b>
                        {ojcowskieDF.to_html(index=False)}
                        <div style="page-break-inside: avoid;">
                        <div style="background-color:#e6f2d9;">
                        <hr class="hr-green">
                        <div style="text-align: left;">WARTOŚCI REFERENCYJNE DLA MŁODYCH KNURÓW HODOWLANYCH NA PODSTAWIE
                         PROGRAMÓW HODOWLANYCH POSZCZEGÓLNYCH RAS:</div>
                        <div>&nbsp;</div>
                        </div>
                        <div>&nbsp;</div>
                        {referencyjneK.to_html(index=False)}
                        <div>&nbsp;</div>
                        <div>&nbsp;</div>
                        <div style="background-color:#EEEEEE;">
                        <hr class="hr-green">
                        <div style="txt-align: left;">Ekspertyza dotyczy wskazania do pozostawieniu w hodowli zarodowej
                         najlepszych knurów spośród wszystkich ocenionych w <span style="color: #ff0000;">{weekStr}
                         </span> tygodniu (przebiegu) szacowania wartości hodowlanej w <span style="color: #ff0000;">
                        {yearStr}</span> r. Rekomenduje się 20% najwyżej ocenionych knurów pod względem 
                         ZWH w obrębie poszczególnych ras jako pulę zwierząt spośród których należy wybrać ojców 
                         kolejnych pokoleń. Wyniki dla rasy puławskiej mają charakter poglądowy. Rasa ta objęta jest 
                         programem ochrony zasobów genetycznych, w związku z tym nie podlega doskonaleniu cech 
                         produkcyjnych.</div>
                         <div>&nbsp;</div>
                         </div>
                         <div>&nbsp;</div>
                         <div>&nbsp;</div>
                         <p style="text-align: justify;font-size: 12px">BALICE, DNIA&nbsp; ........................................................
                                &nbsp; &nbsp;.............................................................</p>
                                <p style="font-size: 10px; padding-left: 340px;">(podpis)</p>
                         </div>
                        
                        
                        
            
                    </body>
                </html>
                '''
        elif gender == 2:

            html = f'''
                <!DOCTYPE html>
                <html lang="pl">

                    <head>


                        <title>Młode Lochy</title>

                    </head>
                    <style type="text/css">
                    
                    
                      table {{
                          font-family: Arial, Helvetica, sans-serif;
                          width: 100%;
                          text-align: center;
                          border-collapse: collapse;
                        }}
                        table td, table th {{
                          padding: 3px 2px;
                          border: 3px solid #FFFFFF
                        }}
                        table tbody td {{
                          font-size: 10px;

                        }}
                        table tr:nth-child(even) {{
                          background: #DEF1DC;
                        }}
                        table thead {{
                          background: #4F7849;
                          background: -moz-linear-gradient(top, #7b9a76 0%, #60855b 66%, #4F7849 100%);
                          background: -webkit-linear-gradient(top, #7b9a76 0%, #60855b 66%, #4F7849 100%);
                          background: linear-gradient(to bottom, #7b9a76 0%, #60855b 66%, #4F7849 100%);
                        }}
                        table thead th {{
                          font-size: 12px;
                          font-weight: bold;
                          color: #FFFFFF;
                          text-align: center;
                        }}
                        table tfoot td {{
                          font-size: 21px;
                        }}
                        .hr-green {{ 
                            display: block; height: 1px;
                            border: 0; border-top: 3px solid green;}}
                    </style>


                    <body>
                        <h1 style="text-align: center;line-height: 50%;"><strong>INSTYTUT ZOOTECHNIKI</strong></h1>
                        <h1 style="text-align: center;line-height: 50%;"><strong>PAŃSTWOWY INSTYTUT BADAWCZY</strong></h1>
                        <h3 style="text-align: center;line-height: 50%;">ZAKŁAD HODOWLI TRZODY CHLEWNEJ</h3>
                        <div style="text-align: center;">ul. Krakowska 1, 32-083 Balice, tel. 666 081 225;agata.bialecka@iz.edu.pl</div>
                        <hr color="black" style="width:100%;text-align:left;margin-left:0">
                        <div style="text-align: center;">&nbsp;</div>
                        <div style="background-color:#e6f2d9;">
                        <hr class="hr-green">
                        <b><p style="text-align: center;line-height: 50%;">EKSPERTYZA NR  <span style="color:
                        #ff0000;">{week}</span>/<span style="color: #ff0000;">{year}</span>/
                        <span style="color: #ff0000;">3</span></p></b>
                        <div style="text-align: center;">&nbsp;</div>
                        <div style="text-align: center;">W ZAKRESIE REKOMENDACJI <span style="color: #ff0000;">30%</span>
                         NAJLEPSZYCH <b>LOSZEK HODOWLANYCH</b> ZE WZGLĘDU NA OSZACOWANĄ ZBIORCZĄ WARTOŚĆ HODOWLANĄ 
                         (<span style="color: #ff0000;">ZWH<span style="color: #000000;">)</span></span></div>
                        <div style="text-align: center;">&nbsp;</div>
                        </div>
                        <div>&nbsp;</div>
                        <div style="background-color:#e6f2d9;">
                        <hr class="hr-green">
                        <div>RANKING MŁODYCH LOSZEK HODOWLANYCH  POD WZGLĘDEM <span style="color: #ff0000;">ZWH</span></div>
                        <div>&nbsp;</div>
                        </div>
                        <span style="color: #ff0000;">RASY MATECZNE<span style="color: #000000;">
                        {mateczneDF.to_html(index=False)}
                        <span style="color: #ff0000;">RASY OJCOWSKIE<span style="color: #000000;">
                        {ojcowskieDF.to_html(index=False)}
                        <div style="page-break-inside: avoid;">
                        
                        <div style="background-color:#e6f2d9;">
                        <hr class="hr-green">
                        <div style="text-align: left;">WARTOŚCI REFERENCYJNE DLA MŁODYCH LOSZEK HODOWLANYCH NA PODSTAWIE
                         PROGRAMÓW HODOWLANYCH POSZCZEGÓLNYCH RAS:</div>
                        <div>&nbsp;</div>
                        </div>
                        <div>&nbsp;</div>
                        {referencyjneL.to_html(index=False)}
                        <div>&nbsp;</div>
                        <div>&nbsp;</div>
                        <div style="background-color:#EEEEEE;">
                        <hr class="hr-green">
                        <div style="txt-align: left;">Ekspertyza dotyczy wskazania do pozostawieniu w hodowli zarodowej
                         najlepszych loszek spośród wszystkich ocenionych w <span style="color: #ff0000;">{weekStr}
                          </span>tygodniu (przebiegu) szacowania wartości hodowlanej w <span style="color: #ff0000;">
                        {yearStr}</span> r. Rekomenduje się 30% najwyżej ocenionych loszek pod względem 
                         ZWH w obrębie poszczególnych ras jako pulę zwierząt spośród których należy wybrać matki 
                         kolejnych pokoleń. Wyniki dla rasy puławskiej mają charakter poglądowy. Rasa ta objęta jest 
                         programem ochrony zasobów genetycznych, w związku z tym nie podlega doskonaleniu cech 
                         produkcyjnych.</div>
                         <div>&nbsp;</div>
                         </div>
                         <div>&nbsp;</div>
                         <div>&nbsp;</div>
                         <p style="text-align: justify;font-size: 12px">BALICE, DNIA&nbsp; ........................................................
                                &nbsp; &nbsp;.............................................................</p>
                                <p style="font-size: 10px; padding-left: 340px;">(podpis)</p>
                         </div>

                    </body>
                </html>
                '''

        with open('raport_młode.html', 'w') as f:
            f.write(html)

    def stare_html(gender,week,year):

        DF = pd.read_csv("Stare_stadne.csv", sep=";", decimal=",")


        if gender == 1:


            colors = {'Numer kolejnej oceny': '#808080', 'Aktualna liczba potom.': '#808080',
                      'Aktualna liczba kojarzeń': '#808080', 'Aktualny Blup ZWH': '#808080',
                      'Max liczba potom.': '#406c13', 'Liczba kojarzeń dla max liczby potom.': '#406c13',
                      'ZWH dla max liczby potom.': '#406c13', 'Liczba potom. dla max ZWH': '#b3e87d',
                      'Liczba kojarzeń dla max ZWH': '#b3e87d', 'Max ZWH': '#b3e87d'
                      }
        if gender == 2:

            colors = {'Aktualna liczba potomstwa lochy oceniona przyżyciowo': '#808080',
                      'Numer kolejnej oceny': '#808080','Aktualny miot':'#808080',
                      'Aktualny Blup ZWH': '#808080', 'Blup przyr. dz. dla max liczby potom.': '#4e7227',
                      'Blup % mięsa dla max liczby potom.': '#4e7227', 'Max liczba potomstwa': '#4e7227',
                      'Blup dla liczby prosiąt urodzonych':'#4e7227','Blup dla liczby prosiąt odchowanych':'#4e7227',
                      'ZWH dla max liczby potom.': '#4e7227', 'Blup przyr. dz. dla max ZWH': '#a7d17a',
                      'Blup % mięsa dla max ZWH': '#a7d17a','Liczba potomstwa lochy ocenianych przyżyciowo dla MAX ZWH': '#a7d17a',
                      'Max ZWH': '#a7d17a','Miot dla max ZWH':'#a7d17a'
                      }

        StyleDF = DF.style.set_table_styles(
            [{
                'selector': f'th.col{i}',
                'props': [('background-color', color)]
            } for i, color in enumerate(DF.columns.map(colors))
            ]).hide(axis="index")

        if gender == 1:

            html = f'''
                        <html>

                            <head>
                                <title>Knury</title>

                            </head>
                            <style type="text/css">
                              tbody>tr>:nth-child(9){{
                                 font-weight: bold;
                                }}
                                
                                
                              table {{
                                  font-family: Arial, Helvetica, sans-serif;
                                  width: 100%;
                                  text-align: center;
                                  border-collapse: collapse;
                                }}
                                table td, table th {{
                                  padding: 3px 2px;
                                  border: 3px solid #FFFFFF
                                }}
                                table tbody td {{
                                  font-size: 11px;

                                }}
                                table tr:nth-child(even) {{
                                  background: #DEF1DC;
                                }}
                                table thead {{
                                  background: #4F7849;
                                  background: -moz-linear-gradient(top, #7b9a76 0%, #60855b 66%, #4F7849 100%);
                                  background: -webkit-linear-gradient(top, #7b9a76 0%, #60855b 66%, #4F7849 100%);
                                  background: linear-gradient(to bottom, #7b9a76 0%, #60855b 66%, #4F7849 100%);
                                  height:40px
                                }}
                                table thead th {{
                                  font-size: 12px;
                                  font-weight: bold;
                                  color: #FFFFFF;
                                  text-align: center;
                                }}
                                table tfoot td {{
                                  font-size: 21px;
                                }}
                                .hr-green {{ 
                                    display: block; height: 1px;
                                    border: 0; border-top: 3px solid green;}}
                            </style>


                            <body>
                                <h1 style="text-align: center;line-height: 50%;"><strong>INSTYTUT ZOOTECHNIKI</strong></h1>
                                <h1 style="text-align: center;line-height: 50%;"><strong>PAŃSTWOWY INSTYTUT BADAWCZY</strong></h1>
                                <h3 style="text-align: center;line-height: 50%;">ZAKŁAD HODOWLI TRZODY CHLEWNEJ</h3>
                                <div style="text-align: center;">ul. Krakowska 1, 32-083 Balice, tel. 666 081 225;agata.bialecka@iz.edu.pl</div>
                                <hr color="black" style="width:100%;text-align:left;margin-left:0;color:black">
                                <div style="text-align: center;">&nbsp;</div>
                                <div style="background-color:#e6f2d9;">
                                <hr class="hr-green">
                                <b><p style="text-align: center;line-height: 50%;">EKSPERTYZA NR  <span style="color:
                                #ff0000;">{week}</span>/<span style="color: #ff0000;">{year}</span>/
                                <span style="color: #ff0000;">4</span></p></b>
                                <div style="text-align: center;">&nbsp;</div>
                                <div style="text-align: center;">W ZAKRESIE REKOMENDACJI DO WYBRAKOWANIA  "MINUS 
                                WARIANTÓW" SPOŚRÓD <b>KNURÓW STADNYCH</b> USZEREGOWANYCH POD WZGLĘDEM OSZACOWANEJ ZBIORCZEJ 
                                WARTOŚCI HODOWLANEJ (<span style="color: #ff0000;">ZWH<span style="color: #000000;">)
                                DLA MAKSYMALNEJ LICZBY POTOMSTWA Z PODANIEM ICH AKTUALNEJ I MAKSYMALNEJ ZWH</span></span>
                                </div>
                                <div>&nbsp;</div>
                                </div>
                                <div style="text-align: center;">&nbsp;</div>

                                <div style="background-color:#e6f2d9;">
                                <hr class="hr-green">
                                <div>RANKING KNURÓW STADNYCH POD WZGLĘDEM <span style="color: #ff0000;">ZWH
                                </span> REKOMENDOWANYCH DO WYBRAKOWANIA</div>
                                <div>&nbsp;</div>
                                </div>
                                <div>&nbsp;</div>
                                {StyleDF.to_html()}
                                <div style="page-break-inside: avoid;">
                                <div>&nbsp;</div>
                                <div style="background-color:#EEEEEE;">
                                <hr class="hr-green">
                                <div style="txt-align: left;">Ekspertyza dotyczy przebiegu szacowania wartości hodowlanej 
                                nr <span style="color: #ff0000;">{week}</span> w <span style="color: #ff0000;">
                                {year}</span> r. W wykazie przedstawiono listę knurów z hodowli zarodowej spośród
                                wszystkich ocenionych knurów, których potomstwo w ostatnich sześciu miesiącach było
                                poddane ocenie przyżyciowej i jednocześnie, których ZWH dla maksymalnej liczby potomstwa 
                                jest poniżej średniej dla tej wartości hodowlanej w obrębie rasy. Rekomenduje się 
                                niewykorzystywanie w hodowli osobników, których ZWH uzyskane przy maksymalnej 
                                liczbie potomstwa są poniżej wspomnianej średniej. Wyniki dla rasy puławskiej mają 
                                charakter poglądowy. Rasa ta objęta jest programem ochrony zasobów genetycznych, w 
                                związku z tym nie podlega doskonaleniu cech produkcyjnych.</div>
                                 <div>&nbsp;</div>
                                 </div>
                                 <div>&nbsp;</div>
                                 <div>&nbsp;</div>
                                 <p style="text-align: justify;font-size: 12px">BALICE, DNIA&nbsp; ........................................................
                                &nbsp; &nbsp;.............................................................</p>
                                <p style="font-size: 10px; padding-left: 340px;">(podpis)</p>
                                 

                            </body>
                        </html>
                        '''
        elif gender == 2:

            html = f'''
                        <html>

                            <head>
                                <title>Lochy</title>

                            </head>
                            <style type="text/css">
                                 
                                }}
                              tbody>tr>:nth-child(14){{
                                 font-weight: bold;
                                }}
                              table {{
                                  font-family: Arial, Helvetica, sans-serif;
                                  width: 100%;
                                  text-align: center;
                                  border-collapse: collapse;
                                }}
                                table td, table th {{
                                  padding: 3px 2px;
                                  border: 3px solid #FFFFFF
                                }}
                                table tbody td {{
                                  font-size: 11px;

                                }}
                                table tr:nth-child(even) {{
                                  background: #DEF1DC;
                                }}
                                table thead {{
                                  background: #4F7849;
                                  background: -moz-linear-gradient(top, #7b9a76 0%, #60855b 66%, #4F7849 100%);
                                  background: -webkit-linear-gradient(top, #7b9a76 0%, #60855b 66%, #4F7849 100%);
                                  background: linear-gradient(to bottom, #7b9a76 0%, #60855b 66%, #4F7849 100%);
                                  height:40px
                                }}
                                table thead th {{
                                  font-size: 12px;
                                  font-weight: bold;
                                  color: #FFFFFF;
                                  text-align: center;
                                }}
                                table tfoot td {{
                                  font-size: 21px;
                                }}
                                .hr-green {{ 
                                    display: block; height: 1px;
                                    border: 0; border-top: 3px solid green;}}
                            </style>


                            <body>
                                <h1 style="text-align: center;line-height: 50%;"><strong>INSTYTUT ZOOTECHNIKI</strong></h1>
                                <h1 style="text-align: center;line-height: 50%;"><strong>PAŃSTWOWY INSTYTUT BADAWCZY</strong></h1>
                                <h3 style="text-align: center;line-height: 50%;">ZAKŁAD HODOWLI TRZODY CHLEWNEJ</h3>
                                <div style="text-align: center;">ul. Krakowska 1, 32-083 Balice, tel. 666 081 225;agata.bialecka@iz.edu.pl</div>
                                <hr color="black" style="width:100%;text-align:left;margin-left:0;color:black">
                                <div style="text-align: center;">&nbsp;</div>
                                <div style="background-color:#e6f2d9;">
                                <hr class="hr-green">
                                <b><p style="text-align: center;line-height: 50%;">EKSPERTYZA NR  <span style="color:
                                #ff0000;">{week}</span>/<span style="color: #ff0000;">{year}</span>/
                                <span style="color: #ff0000;">5</span></p></b>
                                <div style="text-align: center;">&nbsp;</div>
                                <div style="text-align: center;">W ZAKRESIE REKOMENDACJI DO WYBRAKOWANIA TZW "MINUS 
                                WARIANTÓW" SPOŚRÓD <b>LOCH STADNYCH</b> USZEREGOWANYCH POD WZGLĘDEM OSZACOWANEJ ZBIORCZEJ
                                 WARTOŚCI HODOWLANEJ (<span style="color: #ff0000;">ZWH<span style="color: #000000;">)
                                  DLA MAKSYMALNEJ LICZBY POTOMSTWA Z PODANIEM ICH AKTUALNEJ I MAKSYMALNEJ ZWH
                                  </span></span></div>
                                <div style="text-align: center;">&nbsp;</div>
                                </div>
                                <div>&nbsp;</div>
                                <div style="background-color:#e6f2d9;">
                                <hr class="hr-green">
                                <div>RANKING LOCH STADNYCH POD WZGLĘDEM <span style="color: #ff0000;">ZWH</span> 
                                DLA MAX LICZBY POTOMSTWA  REKOMENDOWANYCH DO WYBRAKOWANIA</div>
                                <div>&nbsp;</div>
                                </div>
                                <div>&nbsp;</div>
                                {StyleDF.to_html()}
                                <div style="page-break-inside: avoid;">
                                <div>&nbsp;</div>
                                <div style="background-color:#EEEEEE;">
                                <hr class="hr-green">
                                <div style="txt-align: left;">Ekspertyza dotyczy przebiegu szacowania wartości hodowlanej 
                                nr <span style="color: #ff0000;">{week}</span> w <span style="color: #ff0000;">
                                {year}</span> r. W wykazie przedstawiono listę loch z hodowli zarodowej spośród
                                wszystkich ocenionych loch, których potomstwo w ostatnich sześciu miesiącach było
                                poddane ocenie przyżyciowej i jednocześnie, których ZWH dla maksymalnej liczby potomstwa 
                                jest poniżej średniej 
                                dla tej wartości hodowlanej w obrębie rasy. Rekomenduje się niewykorzystywanie w hodowli  
                                osobników których, ZWH uzyskane przy maksymalnej 
                                liczbie potomstwa są poniżej wspomnianej średniej. Wyniki dla rasy puławskiej mają 
                                charakter poglądowy. Rasa ta objęta jest programem ochrony zasobów genetycznych, w 
                                związku z tym nie podlega doskonaleniu cech produkcyjnych.</div>
                                 <div>&nbsp;</div>
                                 </div>
                                 <div>&nbsp;</div>
                                 <div>&nbsp;</div>
                                 <p style="text-align: justify;font-size: 12px">BALICE, DNIA&nbsp; ........................................................
                                &nbsp; &nbsp;.............................................................</p>
                                <p style="font-size: 10px; padding-left: 340px;">(podpis)</p>

                            </body>
                        </html>
                        '''
        with open('raport_stare.html', 'w') as f:
            f.write(html)
    def ile_chlewni_html(week, year):
        DF1 = pd.read_csv("Jedna_chlewnia.csv", sep=";", decimal=",")
        DF2 = pd.read_csv("Wiecej_chlewni.csv", sep=";", decimal=",")

        colors = {'Numer kolejnej oceny': '#808080', 'Aktualna liczba potom.': '#808080',
                  'Aktualna liczba kojarzeń': '#808080', 'Aktualny Blup ZWH': '#808080',
                  'Max liczba potom.': '#406c13', 'Liczba kojarzeń dla max liczby potom.': '#406c13',
                  'ZWH dla max liczby potom.': '#406c13', 'Liczba potom. dla max ZWH': '#b3e87d',
                  'Liczba kojarzeń dla max ZWH': '#b3e87d', 'Max ZWH': '#b3e87d'
                  }

        StyleDF1 = DF1.style.set_table_styles(
            [{
                'selector': f'th.col{i}',
                'props': [('background-color', color)]
            } for i, color in enumerate(DF1.columns.map(colors))
            ]).hide(axis="index")
        StyleDF2 = DF2.style.set_table_styles(
            [{
                'selector': f'th.col{i}',
                'props': [('background-color', color)]
            } for i, color in enumerate(DF2.columns.map(colors))
            ]).hide(axis="index")

        html = f'''
                            <html>

                                <head>
                                    <title>Knury</title>

                                </head>
                                <style type="text/css">
                                  .wersjaA tbody>tr>:nth-child(11){{
                                     font-weight: bold;
                                    }}
                                
                                .wersjaB tbody>tr>:nth-child(10){{
                                     font-weight: bold;
                                    }}


                                  table {{
                                      font-family: Arial, Helvetica, sans-serif;
                                      width: 100%;
                                      text-align: center;
                                      border-collapse: collapse;
                                    }}
                                    table td, table th {{
                                      padding: 3px 2px;
                                      border: 3px solid #FFFFFF
                                    }}
                                    table tbody td {{
                                      font-size: 11px;

                                    }}
                                    table tr:nth-child(even) {{
                                      background: #DEF1DC;
                                    }}
                                    table thead {{
                                      background: #4F7849;
                                      background: -moz-linear-gradient(top, #7b9a76 0%, #60855b 66%, #4F7849 100%);
                                      background: -webkit-linear-gradient(top, #7b9a76 0%, #60855b 66%, #4F7849 100%);
                                      background: linear-gradient(to bottom, #7b9a76 0%, #60855b 66%, #4F7849 100%);
                                      height:40px
                                    }}
                                    table thead th {{
                                      font-size: 12px;
                                      font-weight: bold;
                                      color: #FFFFFF;
                                      text-align: center;
                                    }}
                                    table tfoot td {{
                                      font-size: 21px;
                                    }}
                                    .hr-green {{ 
                                        display: block; height: 1px;
                                        border: 0; border-top: 3px solid green;}}
                                </style>


                                <body>
                                    <h1 style="text-align: center;line-height: 50%;"><strong>INSTYTUT ZOOTECHNIKI</strong></h1>
                                    <h1 style="text-align: center;line-height: 50%;"><strong>PAŃSTWOWY INSTYTUT BADAWCZY</strong></h1>
                                    <h3 style="text-align: center;line-height: 50%;">ZAKŁAD HODOWLI TRZODY CHLEWNEJ</h3>
                                    <div style="text-align: center;">ul. Krakowska 1, 32-083 Balice, tel. 666 081 225;agata.bialecka@iz.edu.pl</div>
                                    <hr color="black" style="width:100%;text-align:left;margin-left:0;color:black">
                                    <div style="text-align: center;">&nbsp;</div>
                                    <div style="background-color:#e6f2d9;">
                                    <hr class="hr-green">
                                    <b><p style="text-align: center;line-height: 50%;">EKSPERTYZA NR  <span style="color:
                                    #ff0000;">{week}</span>/<span style="color: #ff0000;">{year}</span>/
                                    <span style="color: #ff0000;">4</span></p></b>
                                    <div style="text-align: center;">&nbsp;</div>
                                    <div style="text-align: center;">W ZAKRESIE REKOMENDACJI DO WYBRAKOWANIA  "MINUS 
                                    WARIANTÓW" SPOŚRÓD <b>KNURÓW STADNYCH</b> USZEREGOWANYCH POD WZGLĘDEM OSZACOWANEJ ZBIORCZEJ 
                                    WARTOŚCI HODOWLANEJ (<span style="color: #ff0000;">ZWH<span style="color: #000000;">)
                                    DLA MAKSYMALNEJ LICZBY POTOMSTWA Z PODANIEM ICH AKTUALNEJ I MAKSYMALNEJ ZWH</span></span>
                                    </div>
                                    <div>&nbsp;</div>
                                    </div>
                                    <div style="text-align: center;">&nbsp;</div>

                                    <div style="background-color:#e6f2d9;">
                                    <hr class="hr-green">
                                    <div>RANKING KNURÓW STADNYCH POD WZGLĘDEM <span style="color: #ff0000;">ZWH
                                    </span> REKOMENDOWANYCH DO WYBRAKOWANIA</div>
                                    <div>&nbsp;</div>
                                    </div>
                                    <div>&nbsp;</div>
                                    <b>KNURY Z JEDNEJ CHLEWNI</b>
                                    <div>&nbsp;</div>
                                    <div class = "wersjaA">{StyleDF1.to_html()}</div>
                                    <div>&nbsp;</div>
                                    <b>KNURY Z WIĘCEJ NIŻ JEDNEJ CHLEWNI</b>
                                    <div>&nbsp;</div>
                                    <div class = "wersjaB">{StyleDF2.to_html()}</div>
                                    <div style="page-break-inside: avoid;">
                                    <div>&nbsp;</div>
                                    <div style="background-color:#EEEEEE;">
                                    <hr class="hr-green">
                                    <div style="txt-align: left;">Ekspertyza dotyczy przebiegu szacowania wartości hodowlanej 
                                    nr <span style="color: #ff0000;">{week}</span> w <span style="color: #ff0000;">
                                    {year}</span> r. W wykazie przedstawiono listę knurów z hodowli zarodowej spośród
                                    wszystkich ocenionych knurów, których potomstwo w ostatnich sześciu miesiącach było
                                    poddane ocenie przyżyciowej i jednocześnie, których ZWH dla maksymalnej liczby potomstwa 
                                    jest poniżej średniej dla tej wartości hodowlanej w obrębie rasy. Rekomenduje się 
                                    niewykorzystywanie w hodowli osobników, których ZWH uzyskane przy maksymalnej 
                                    liczbie potomstwa są poniżej wspomnianej średniej. Wyniki dla rasy puławskiej mają 
                                    charakter poglądowy. Rasa ta objęta jest programem ochrony zasobów genetycznych, w 
                                    związku z tym nie podlega doskonaleniu cech produkcyjnych.</div>
                                     <div>&nbsp;</div>
                                     </div>
                                     <div>&nbsp;</div>
                                     <div>&nbsp;</div>
                                     <p style="text-align: justify;font-size: 12px">BALICE, DNIA&nbsp; ........................................................
                                    &nbsp; &nbsp;.............................................................</p>
                                    <p style="font-size: 10px; padding-left: 340px;">(podpis)</p>


                                </body>
                            </html>
                            '''
        with open('raport_ile_chlewni.html', 'w') as f:
            f.write(html)