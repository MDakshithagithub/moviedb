import sqlite3
from movie import Movie

conn=sqlite3.connect(':memory:')# create a new database on each run
c=conn.cursor()
c.execute("""CREATE TABLE movies (
	name text,
	actor text,
	actress text, 
    director text, 
    year integer
	)""")#creating a table

mov_1 = Movie('Radhe Shyam','Prabhas','Pooja Hegde','Radha Krishna Kumar',2022)
mov_2 = Movie('Baahubali: The Beginning','Prabhas','Tamanna','S. S. Rajamouli',2015)
mov_3= Movie('Vaikuntapuram','Allu Arjun','Pooja Hegde','Trivikram Srinivas',2020)#inserting 3 values
def insert_mov(mov):
    with conn:
        c.execute("INSERT INTO movies VALUES (:name, :actor, :actress,:director,:year)", {'name': mov.name, 'actor': mov.actor, 'actress': mov.actress, 'director': mov.director, 'year': mov.year})

insert_mov(mov_1)
insert_mov(mov_2)
insert_mov(mov_3)#inserting into table
       
c.execute("SELECT * FROM movies")
print(c.fetchall())# fetching all the rows from the table
c.execute("SELECT name FROM movies WHERE actor='Prabhas'")
print(c.fetchall())# fetching movie name based on actor name
conn.commit()
conn.close()
