from sqlalchemy import create_engine
import pymysql
import os 


def create_insert_Database():
	try:
		#Setting SQL env
		db_user = os.environ.get('MYSQL_USER')
		db_host = os.environ.get('MYSQL_HOST')
		db_password = os.environ.get('MYSQL_PASSWORD')
		db_name = os.environ.get('MYSQL_DATABASE')
		
		#Connection to SQL
		#engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@db/{db_name}')

		connection = pymysql.connect(
            host=db_host,
            user=db_user,
            passwd=db_password
        )
	
		
		cursor = connection.cursor()

		cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name};")
		cursor.execute(f"USE {db_name};")
		
		# Create dataBase
		create_body_table = """
		CREATE TABLE IF NOT EXISTS Body (
    		BodyID INT PRIMARY KEY AUTO_INCREMENT,
    		Name VARCHAR(255) NOT NULL
		);
		"""
		
		create_muscle_table = """
		CREATE TABLE IF NOT EXISTS Muscle (
    		MuscleID INT PRIMARY KEY AUTO_INCREMENT,
    		Name VARCHAR(255) NOT NULL,
    		Description TEXT
		);
		"""
		create_muscle_mapping_table = """
		CREATE TABLE IF NOT EXISTS MuscleMapping (
   		MuscleMappingID INT PRIMARY KEY AUTO_INCREMENT,
   		BodyID INT,
    		MuscleID INT,
    		FOREIGN KEY (BodyID) REFERENCES Body(BodyID),
    		FOREIGN KEY (MuscleID) REFERENCES Muscle(MuscleID)
		);
		"""
		
		insert_sample_data_body = """
		INSERT INTO Body (Name) VALUES
		    ('Upper Body'),
		    ('Lower Body'),
		    ('Core');
		"""
		
		insert_sample_data_muscle = """
		INSERT INTO Muscle (Name, Description) VALUES
   		('Biceps', 'Front upper arm muscle'),
    		('Quadriceps', 'Front thigh muscle'),
    		('Abdominals', 'Stomach muscles');
		"""
		
		insert_sample_data_mapping = """
		INSERT INTO MuscleMapping (BodyID, MuscleID) VALUES
		(1, 1), -- Upper Body includes Biceps
    		(2, 2), -- Lower Body includes Quadriceps
    		(3, 3); -- Core includes Abdominals
		"""
		

		cursor.execute(create_body_table)
		cursor.execute(create_muscle_table)
		cursor.execute(create_muscle_mapping_table)
		cursor.execute(insert_sample_data_body)
		cursor.execute(insert_sample_data_muscle)
		cursor.execute(insert_sample_data_mapping)
		
		connection.commit()
		cursor.close()
		
	except Exeption as e:
		print("FAILED TO CREATE DATABASE", e)

if __name__ == "__main__":
	create_insert_Database()
	
		
		
		
