import mysql
import mysql.connector
import config

class DataIngestionPipeline:
    def __init__(self, host, user, password, db_name) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name
        self.db = None
        
        
    def connect(self):
        try:
            self.db =  mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db_name
            )
        except Exception as e:
            print(str(e))
            self.db = None
        

    def creat_db(self):
         if(self.db):
                cursor = self.db.cursor()
                cursor.execute(f"""CREATE DATABASE IF NOT EXISTS {self.db_name}""")
         else:
             # Connecting to db
             self.connect()
             
    
        
        
data_pipeline = DataIngestionPipeline(config.DB_HOST, config.DB_USER, config.DB_PASSWORD, 'uhall')
data_pipeline.connect()
        