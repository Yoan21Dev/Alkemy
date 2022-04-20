from src.controller import Fuente
import db 
from src.models import user


def main():
    a=Fuente()
    a.extraccion()

def run():
    pass


if __name__ == '__main__':
    # main()
    db.Base.metadata.drop_all(db.engine)
    db.Base.metadata.create_all(db.engine)
    run()
            
        