#!/usr/bin/python
from distutils.command.config import config
from msilib.schema import Error
from .Get_Data import get_data_local
import io,requests,os.path,os
from requests.exceptions import HTTPError, ConnectionError
from decouple import config
from src.repository.user_queries import queries


class Fuente:
    def __init__(self) -> None:
        pass

    def extraccion(self):
        with requests.Session() as s:
            try:
                get_data_local(config('CSV_URL_M'),'Museo')
                get_data_local(config('CSV_URL_C'),'Cines')
                get_data_local(config('CSV_URL_B'),'Biblioteca')
            except HTTPError as http_err:
                print(f"HTTP error ocurrido: {http_err}")
            except ConnectionError as err:
                print(f"Error de conexion: {err}")
            else:
                print("success")
    """extraer csv y guardar archivo """

    def create_tabla_and_data(self):
        queries()
        return 'success'
