#!/usr/bin/python
from distutils.command.config import config
from src.controller.Get_Data import logging
from msilib.schema import Error
from .Get_Data import get_data_local
import io,requests,os.path,os
from requests.exceptions import HTTPError, ConnectionError
from decouple import config
from src.repository.data_queries import queries


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
                logging.error(f'error https a ocurrido:{http_err}')
            except ConnectionError as err:
                print(f"Error de conexion:{err}")
                logging.error(f'error de conexion:{err} ')
            else:
                print("success")
    """extraer csv y guardar archivo """

    def create_tabla_and_data(self):
        try:
            queries()
            logging.info('importacion del data de dataframe')
        except Exception as ex:
            print('error inesperado in repository')
            logging.error(f'error inesperado con la base de dato{ex}')
        return 'success'
