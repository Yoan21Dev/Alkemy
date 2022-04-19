import imp
from src.controller import Fuente
from src.models import db_db 
from src.models import user


def main():
    a=Fuente()
    a.extraccion()

def run():
    pass


if __name__ == '__main__':
    # main()
    db_db.Base.metadata.create_all(db_db.engine)
    run()
            
        