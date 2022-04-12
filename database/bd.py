import sqlalchemy as sql
database_type = 'mysql'

user = 'user_name'
password = 'password'
host = 'xxx.xxx.xxx.xxx:port'
database = 'database_name'
conn_string = '{}://{}:{}@{}/{}'.format(
database_type, user, password, host, database)
sql_conn = sql.create_engine(conn_string)