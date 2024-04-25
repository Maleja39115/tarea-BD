
import sqlite3
conn =sqlite3.connect("Suicidios")
cursor=conn.cursor()
_SQL="""
    
CREATE TABLE if not exists SUICIDIOS(
ID TEXT,
Añodelhecho TEXT,
Sexodelavictima TEXT,
Grupodeedaddelavictima TEXT,
Mesdelhecho TEXT,
Diadelhecho TEXT,
DepartamentodelhechoDANE TEXT,
MunicipiodelhechoDANE TEXT,
Lesionfataldecausaexterna TEXT,
Estado TEXT);

"""
cursor.execute(_SQL)




with open('sql.sql', 'r',encoding="UTF-8") as f:
    cursor.executescript(f.read())

conn.commit()

conn.close()
