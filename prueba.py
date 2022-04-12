from os import sep
import pandas as pd 
import io, requests
from decouple import config



with requests.Session() as s:
    r = s.get(config('CSV_URL_M'))
    decode_content = r.content.decode('utf-8')  
    df = pd.read_csv(io.StringIO(decode_content),sep= ',')
    print(df['Cod_Loc'])


  