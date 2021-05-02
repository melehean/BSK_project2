class Teachers_Table:
    def __init__(self, db):
        self.db = db

    def read_all(self):
        cursor = self.db.cursor();
        cursor.execute('select * from Teachers')
        result = []
        for row in cursor:
            result.append(f'{row}')
        return result

    def search_by_pesel(self, pesel):
        cursor = self.db.cursor();
        cursor.execute('select * from Teachers where Pesel = ?', pesel)
        result = []
        for row in cursor:
            result.append(f'{row}')
        return result

    def search_by_name(self, name):
        cursor = self.db.cursor();
        cursor.execute('select * from Teachers where Name = ?', name)
        result = []
        for row in cursor:
            result.append(f'{row}')
        return result

    def search_by_surname(self, surname):
        cursor = self.db.cursor();
        cursor.execute('select * from Teachers where Surname = ?', surname)
        result = []
        for row in cursor:
            result.append(f'{row}')
        return result

    def search_by_degree(self, degree):
        cursor = self.db.cursor();
        cursor.execute('select * from Teachers where Degree = ?', degree)
        result = []
        for row in cursor:
            result.append(f'{row}')
        return result

    def search_by_app_login(self, app_login):
        cursor = self.db.cursor();
        cursor.execute('select * from Teachers where App_login = ?', app_login)
        result = []
        for row in cursor:
            result.append(f'{row}')
        return result

    def insert(self, pesel, name, surname, degree):
        cursor = self.db.cursor()
        cursor.execute('insert into Teachers(Pesel, Name, Surname, Degree) values(?,?,?,?);',
        pesel, name, surname, degree)
        cursor.commit()
        self.read_all()

    def update_surname(self, pesel, new_surname):
        cursor = self.db.cursor()
        cursor.execute('update Teachers set Surname = ? where Pesel = ?;',
        new_surname, pesel)
        cursor.commit()
        self.read_all()

    def delete(self, pesel):
        cursor = self.db.cursor()
        cursor.execute('delete from Teachers where Pesel = ?;',
        pesel)
        cursor.commit()
        self.read_all()