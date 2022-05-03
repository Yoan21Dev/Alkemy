from src.controller import Fuente
import db 
from src.models import data


def main():
    a=Fuente()
    a.extraccion()
    a.create_tabla_and_data()
    
def run():
    pass

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    run()
    main()