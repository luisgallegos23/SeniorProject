import psycopg2
import sys 

conn = psycopg2.connect(sslmode="verify-ca", sslrootcert="server-ca.pem", sslcert="client-cert.pem", sslkey="client-key.pem", hostaddr="104.155.144.9", port="5432", user="sylly", dbname="sylly", password="Sylly2023" )
cur = conn.cursor()  # make a cursor (allows us to execute queries)

file = open("schema.sql", "r") # open the file
alltext = file.read() # read all the text
cur.execute(alltext) # execute all the SQL in the file
conn.commit()  # Actually make the changes to the db

cur.close()  
conn.close() # close everything