from distutils.command.config import config
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.models.user import Base, User

engine = create_engine(config('DB_ENGINE'))
engine = create_engine('postgresql://postgres:12345@localhost/example')


Session = sessionmaker(engine)
session = Session() 
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine) 


user1 = User(username='User1', email='user1@Example.com')
user2 = User(username='User2', email='user2@Example.com')
user3 = User(username='User3', email='user3@Example.com')

session.add(user1)
session.add(user2)
session.add(user3)     

session.commit()

# select * from users;
users = session.query(User.id, User.username, User.email, User.create_at).filter(
    User.id >= 2
)

for use in users :
    print(use)