import os
import pandas as pd
from dotenv import load_dotenv

from sqlalchemy import create_engine, Column, Integer, String, Float, text
from sqlalchemy.orm import declarative_base

load_dotenv()

def get_engine():
    #получаем учетные данные
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    url = os.getenv("DB_URL")
    port = os.getenv("DB_PORT")
    #подключение
    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{url}:{port}/homeworks")
    return engine

def data_exporting(engine, table_name):
    df = pd.read_parquet("nyc-rolling-sales.parquet")
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

engine = get_engine()
table_name = "bukalova"
data_exporting(engine, table_name)