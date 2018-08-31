import sqlite3
class DBconnect:
        def __init__(self):
            self._db=sqlite3.connect("Sensor.db")
            self._db.row_factory=sqlite3.Row
            self._db.execute("create table if not exists Sensor(ID integer primary key autoincrement,Test text, Reading int, Unit text)")
            self._db.commit()

        def Add (self,Test,Reading,Unit):
            self._db.row_factory=sqlite3.Row
            self._db.execute("insert into Sensor(Test,Reading,Unit) values(?,?,?)",(Test,Reading,Unit))
            self._dc.commit()

        def ListAdmins(self):
            cursor=self._db.execute("select * from Sensor")
            for row in cursor:
                print ("ID:{},Test:{},Reading:{},Unit:{}".format(row["ID"],row["Test"],row["Reading"],row["Unit"]))
    
    
