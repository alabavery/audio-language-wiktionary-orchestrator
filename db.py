class DB:
    USER="al"
    PASSWORD="pw"
    DB_NAME="words"
    SSL_MODE="disable"
    NETWORK="words-db"
    HOST="words-db"
    PORT="5432"

CONNECTION_STRING = "postgresql://{user}:{pw}@{host}:{port}/{db}?sslmode={ssl}".format(
    host=DB.HOST,
    port=DB.PORT,
    user=DB.USER,
    pw=DB.PASSWORD,
    db=DB.DB_NAME,
    ssl=DB.SSL_MODE,
)
