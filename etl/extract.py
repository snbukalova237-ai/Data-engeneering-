#Только Google Drive
import gdown
import pandas as pd

def read_data(url: str, output_name: str) -> pd.DataFrame:
  gdown.download(url, output_name, quiet=False)
  df = pd.read_csv(output_name)
  # Удалим первый столбец
  df = df.drop('Unnamed: 0', axis=1)
  # Изменим регистр названий столбцов
  df.columns = df.columns.str.capitalize()
  print('Данные загружены')
  return df