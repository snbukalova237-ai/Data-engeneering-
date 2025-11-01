import argparse
import os
import sys

from dotenv import load_dotenv
from dataclasses import dataclass
from extract import read_data
from transform import transform_data_types, clean_data, validate_data, convert_to_parquet
from load import get_engine, data_exporting

@dataclass
class Config:
    PARQUET_FILE: str
    DB_URL: str
    DB_USER: str
    DB_PASSWORD: str
    DB_PORT: int = 5432
    GDRIVE_URL: str = "-"
    INPUT_FILE: str = "data/raw/data.csv"
    OUTPUT_PATH: str = "data/processed/data.csv"

def load_environment_variables() -> Config:
    load_dotenv()
    return Config(
        PARQUET_FILE=os.getenv("PARQUET_FILE", "output/data.parquet"),
        DB_URL=os.getenv("DB_HOST", "localhost"),
        DB_PORT=int(os.getenv("DB_PORT", "5432")),
        DB_USER=os.getenv("DB_USER", "user"),
        DB_PASSWORD=os.getenv("DB_PASSWORD", "password"),
        GDRIVE_URL =os.getenv("GDRIVE_URL", "https://drive.google.com"),
        INPUT_FILE=os.getenv("INPUT_FILE", "input/data.csv"),
        OUTPUT_PATH=os.getenv("OUTPUT_PATH", "output/data.csv"),
    )

def etl_process(etl_config: Config) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--db_name', type=str, help='Область базы данных')
    parser.add_argument('--table_name', type=str, help='Фамилия на латинице')
    args = parser.parse_args()
    
    print("Начинаем ETL")

    # Extract
    print("Extracting data...")
    df = read_data(etl_config.GDRIVE_URL, etl_config.INPUT_FILE)

    # Transform
    print("Transforming data...")
    df = transform_data_types(df)
    df = clean_data(df)
    validate_data(df)

    # Load
    print("Loading data...")
    convert_to_parquet(df, etl_config.OUTPUT_PATH)
    
    engine = get_engine(args.db_name)
    data_exporting(engine, etl_config.PARQUET_FILE, args.table_name)

if __name__ == "__main__":
    config: Config = load_environment_variables()
    etl_process(config)