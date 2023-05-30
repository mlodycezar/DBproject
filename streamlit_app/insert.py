import pandas as pd
from sqlalchemy import create_engine

def insert_files(files):
    for filename in files:
        print(filename.name)
        tablename = filename.name.replace(".csv", "")
        DF = pd.read_csv(filename,sep=',',low_memory=False)
        DF.columns = map(str.lower, DF.columns)
        tablename = tablename.lower()
        engine = create_engine('postgresql://maciek:Test1234!!!!@10.64.10.85:5432/IZ_DB')
        if filename.name.lower() == 'mag.csv' or filename.name.lower() == 'mag_zapas':
            DF.to_sql(tablename, engine,if_exists='replace',index=False,chunksize=10000)
        else:
            DF.to_sql(tablename, engine, if_exists='append', index=False, chunksize=10000)


        print(f"File {tablename} insert  correctly..")

