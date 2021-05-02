class Courses_Table:
    
    def __init__(self, db):
        self.db = db

    def read_all(self):
        cursor = self.db.cursor()
        cursor.execute('select * from Courses')
        result = []
        for row in cursor:
            result.append(f'{row}')
        return result

    def search_by_name(self, name):
        cursor = self.db.cursor()
        cursor.execute('select * from Courses where Name = ?', name)
        result = []
        for row in cursor:
            result.append(f'{row}')
        return result

    def search_by_etcs(self, etcs):
        cursor = self.db.cursor()
        cursor.execute('select * from Courses where ETCS = ?', etcs)
        result = []
        for row in cursor:
            result.append(f'{row}')
        return result

    def insert(self, name, etcs):
        cursor = self.db.cursor()
        cursor.execute('insert into Courses(Name, ETCS) values(?,?);',
        name, etcs)
        cursor.commit()
        self.read_all()

    def update_etcs(self, name, new_etcs):
        cursor = self.db.cursor()
        cursor.execute('update Courses set ETCS = ? where Name = ?;',
        new_etcs, name)
        cursor.commit()
        self.read_all()

    def delete(self, name):
        cursor = self.db.cursor()
        cursor.execute('delete from Courses where Name = ?;',
        name)
        cursor.commit()
        self.read_all()