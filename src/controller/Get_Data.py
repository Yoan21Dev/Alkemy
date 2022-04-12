from datetime import date
from msilib.schema import Error
import pandas as pd 
import io,requests,os.path,os,arrow
import sqlalchemy as sql 


def get_data(data, data_name): 
    with requests.Session() as s:
        try:
            r = s.get(data)
            decode_content = r.content.decode('utf-8')  
            df = pd.read_csv(io.StringIO(decode_content),index_col=0)
            today = date.today()
            month = arrow.utcnow().format('MMMM', locale='es')     
            directorio=(f'Dates\\{data_name}\\{today.year}-{month}\\{data_name} -{today}')
            os.makedirs(directorio,exist_ok=True)
            df.to_csv(f'{directorio}/{data_name}.csv')
        except Error:
            print({Error})
    return print('finish')





# nombre_fichero = os.path.join(os.sep, "home", "manolo", "miscosas", "fichero.txt")
# f = os.makedirs(nombre_fichero, "w")
# file = open("/ruta/filename.txt", "w")
# os.makedirs("Musica/Pop/2014", open("archivo.csv","w"))
# date_string = "21 June, 2018"

# print("date_string =", date_string)   
# print(dir(os))
# date_object = datetime.strptime(date_string, "%d %B, %Y")
# print("date_object =", date_object)