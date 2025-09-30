import gdown
import pandas as pd
FILE_ID = "14L8b_zXrpf57KosWqFY3n9cVFyQcUd6L"
URL = f"https://drive.google.com/uc?id={FILE_ID}"
OUTPUT = "dataset.csv"  
gdown.download(URL, OUTPUT, quiet=False)
raw_data = pd.read_csv(OUTPUT)

print(raw_data.head(10)) 
del raw_data['EASE-MENT'] #удалила пустой столбец
import pandas as pd # Заменила все варианты пустых значений на NaN
raw_data = raw_data.replace(['', ' ', '-', ' - ', ' -', '- ', '-  ', '  -', ' -  ', '  - '], pd.NA)
# Удалила строки, где в любом столбце есть NaN
raw_data = raw_data.dropna()
print(f"После очистки осталось {len(raw_data)} строк")

print(raw_data.dtypes) #текущие данные
print(raw_data.head(10)) 
columns = ["LAND SQUARE FEET", "GROSS SQUARE FEET"] #столбцы, формат которых нужно перевести в числовой
raw_data[columns]=raw_data[columns].astype(int)
raw_data["SALE DATE"] = pd.to_datetime(raw_data["SALE DATE"])  # Перевела данные столбца в тип "дата"
print(raw_data.dtypes)
