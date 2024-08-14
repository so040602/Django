import sqlite3
import pandas as pd

csv_file = './data/kmdb_get_movie_list_100_new.csv'
df = pd.read_csv(csv_file)

conn = sqlite3.connect('./../mydatabase.sqlite3')
cursor = conn.cursor()

# 테이블을 생성하는 문장입니다.
sql = '''
create table movies(
movieCd integer primary key autoincrement,
movieNm text,
movieNmEn text,
prdtYear real,
openDt real,
typeNm text,
prdtStatNm text,
nationAlt text,
genreAlt text,
repNationNm text,
repGenreNm text
)
'''

cursor.execute(sql)

df.to_sql('movies', conn, if_exists='append', index=False)

conn.commit()
conn.close()

print('데이터 베이스 파일에 데이터 추가를 성공하였습니다.')