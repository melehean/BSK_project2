class Students_Table:

    def __init__(self, db):
        self.db = db

    def read_all(self):
        cursor = self.db.cursor();
        cursor.execute('select * from Students')
        result = []
        for row in cursor:
            result.append(f'{row}')
        return result

    def search_by_pesel(self, pesel):
        cursor = self.db.cursor();
        cursor.execute('select * from Students where Pesel = ?', pesel)
        result = []
        for row in cursor:
            result.append(f'{row}')
        return result

    def search_by_name(self, name):
        cursor = self.db.cursor();
        cursor.execute('select * from Students where Name = ?', name)
        result = []
        for row in cursor:
            result.append(f'{row}')
        return result

    def search_by_surname(self, surname):
        cursor = self.db.cursor();
        cursor.execute('select * from Students where Surname = ?', surname)
        result = []
        for row in cursor:
            result.append(f'{row}')
        return result

    def search_by_app_login(self, app_login):
        cursor = self.db.cursor();
        cursor.execute('select * from Students where App_login = ?', app_login)
        result = []
        for row in cursor:
            result.append(f'{row}')
        return result

    def insert(self, pesel, name, surname):
        cursor = self.db.cursor()
        cursor.execute('insert into Students(Pesel, Name, Surname) values(?,?,?);',
        pesel, name, surname)
        cursor.commit()
        self.read_all()

    def update_surname(self, pesel, new_surname):
        cursor = self.db.cursor()
        cursor.execute('update Students set Surname = ? where Pesel = ?;',
        new_surname, pesel)
        cursor.commit()
        self.read_all()

    def delete(self, pesel):
        cursor = self.db.cursor()
        cursor.execute('delete from Students where Pesel = ?;',
        pesel)
        cursor.commit()
        self.read_all()