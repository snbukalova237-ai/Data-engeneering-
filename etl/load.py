import os
import pandas as pd

from sqlalchemy import create_engine
from dotenv import load_dotenv

def get_engine(db_name):
  #получаем учетные данные
  user = os.getenv("DB_USER")
  password = os.getenv("DB_PASSWORD")
  url = os.getenv("DB_URL")
  port = os.getenv("DB_PORT")
  #подключение
  engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{url}:{port}/{db_name}")
  return engine

def data_exporting(engine, parquet_name, table_name):
  df = pd.read_parquet(parquet_name)
  df = df.head(100)
  df.to_sql(
      name=table_name,
      con=engine,
      schema="public",
      if_exists="replace",
      index=False
  )
  print("Успешно")
  df_check = pd.read_sql_table(table_name, con=engine, schema="public")
  print("Вывод")
  print(df_check)
