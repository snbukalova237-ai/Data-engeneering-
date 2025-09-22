import gdown
import pandas as pd
FILE_ID = "14L8b_zXrpf57KosWqFY3n9cVFyQcUd6L"
URL = f"https://drive.google.com/uc?id={FILE_ID}"
OUTPUT = "dataset.csv"  
gdown.download(URL, OUTPUT, quiet=False)
raw_data = pd.read_csv(OUTPUT)
print(raw_data.head(10)) 