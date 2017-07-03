import sqlite3

conn = sqlite3.connect('./db/crimemap')

c = conn.cursor()

c.execute("""drop table if exists crimes""")
c.execute("""drop table if exists hotels""")

conn.commit()

c.execute("""create table crimes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        latitude float(10,6),
        longitude float(10,6),
        date datetime,
        category varchar(50),
        description varchar(1000),
        updated_at timestamp)""")

# c.execute("""create table hotels (
#         hid int primary key not NULL ,
#         tid int,
#         name text,
#         address text,
#         rooms int,
#         rate float)""")
c.execute("Insert into crimes (description) values ('TEST Insert 1')")
# c.execute("""insert into towns values (1, "Melksham", "SN12")""")
# c.execute("""insert into towns values (2, "Cambridge", "CB1")""")
# c.execute("""insert into towns values (3, "Foxkilo", "CB22")""")

# c.execute("""insert into hotels values (1, 2, "Hamilkilo Hotel", "Chesterton Road", 15, 40.)""")
# c.execute("""insert into hotels values (2, 2, "Arun Dell", "Chesterton Road", 60, 70.)""")
# c.execute("""insert into hotels values (3, 2, "Crown Plaza", "Downing Street", 100, 105.)""")
# c.execute("""insert into hotels values (4, 1, "Well House Manor", "Spa Road", 5, 80.)""")
# c.execute("""insert into hotels values (5, 1, "Beechfield House", "The Main Road", 26, 110.)""")

conn.commit()

#c.execute ("""select * from towns left join hotels on towns.tid = hotels.tid""")

for row in c:
        print (row)

c.close()