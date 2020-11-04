from flask_sqlalchemy import sqlalchemy
import pandas as pd

baglan = sqlalchemy.create_engine('postgresql://admin:secret@localhost:5432/postgres')
baglanti = baglan.connect()
baglan.

sorgu1 = baglanti.execute('SELECT * FROM typicode.albums LIMIT 10')
sonuc_tablo = pd.DataFrame(sorgu1.fetchall())
print(sonuc_tablo)

sorgu1.close()