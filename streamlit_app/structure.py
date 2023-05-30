import pandas as pd
import datetime

listOfFiles = []
tempDF = pd.DataFrame()

def create_new_column(df,file):
    df["TYD_P"] = file.name[1:3]
    df["ROK_P"] = "20" + str(file.name[6:8])
    date = "20" + str(file.name[6:8]) + "-W" + str(file.name[1:3])
    r = datetime.datetime.strptime(date + '-1', "%Y-W%W-%w")
    r = str(r)
    d = r[:10]
    df["KD"] = d
    df["RASA"] = file.name[4:6]
    if file.name[3:4] == "R":
        if str(df["DWYB"]) == '0.0':
            df["DWYB"] = df["DWYB"].where(data == '-', None)
    gender = ['R', 'L', 'D']
    if file.name[3:4] in gender:
        df["KP"] = 2
    else:
        df["KP"] = 1
    return df


def create_new_column_polsus(df,file):
    df["TYD_P"] = file.name[4:6]
    df["ROK_P"] = "20" + str(file.name[6:8])
    date = "20" + str(file.name[6:8]) + "-W" + str(file.name[4:6])

    r = datetime.datetime.strptime(date + '-1', "%Y-W%W-%w")
    r = str(r)
    d = r[:10]
    df["KD"] = d
    return df

def create_structure(files):
    for file in files:
        listOfFiles.append(file)

    rozplodowaDF = pd.DataFrame()
    knuryDF = pd.DataFrame()
    lochyDF = pd.DataFrame()
    mlodeDF = pd.DataFrame()
    polsusTDF = pd.DataFrame()
    for file in listOfFiles:
        print(file.name)
        if file.name[3:4] == "R" and file.name[0] != "K":
            dR = pd.read_csv(file, sep=',')
            tempDR = create_new_column(dR,file)
            rozplodowaDF = pd.concat([rozplodowaDF, tempDR])

        elif file.name[3:4] == "S" or file.name[3:4] == "s" and file.name != "MAG.csv":
            dS = pd.read_csv(file, sep=',')
            tempDS = create_new_column(dS,file)
            knuryDF = pd.concat([knuryDF, tempDS])

        elif file.name[3:4] == "D" or file.name[3:4] == "d":
            dD = pd.read_csv(file, sep=',')
            tempDD = create_new_column(dD,file)
            lochyDF = pd.concat([lochyDF, tempDD])

        elif file.name[3] == "K" or file.name[3] == "L":
            kl = pd.read_csv(file, sep=',')
            tempKL = create_new_column(kl,file)
            mlodeDF = pd.concat([mlodeDF, tempKL])

        elif file.name[0:4] == "KNUR":
            polsus = pd.read_csv(file, sep=',')
            tempPolsus = create_new_column_polsus(polsus,file)
            polsusTDF = pd.concat([polsusTDF, tempPolsus])

    mlodeDF = mlodeDF.drop(['WYSLANY', 'JEST'],axis=1,errors='ignore')
    lochyDF = lochyDF.drop(['WYSLANY', 'JEST'],axis=1,errors='ignore')
    knuryDF = knuryDF.drop(['WYSLANY', 'JEST'],axis=1,errors='ignore')
    rozplodowaDF = rozplodowaDF.drop(['WYSLANY', 'JEST'],axis=1,errors='ignore')

    return [mlodeDF,lochyDF,knuryDF,rozplodowaDF,polsusTDF]