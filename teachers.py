class Teachers_Table:
    def __init__(self, db):
        self.db = db

    def read_all(self):
        print("Read All")
        cursor = self.db.cursor();
        cursor.execute('select * from Teachers')
        result = []
        for row in cursor:
            result.append(f'{row}')
        return result

    def search_by_pesel(self, pesel):
        print('Search by Pesel')
        cursor = self.db.cursor();
        cursor.execute('select * from Teachers where Pesel = ?', pesel)
        result = []
        for row in cursor:
            result.append(f'{row}')
        return result

    def search_by_name(self, name):
        print('Search by Name')
        cursor = self.db.cursor();
        cursor.execute('select * from Teachers where Name = ?', name)
        result = []
        for row in cursor:
            result.append(f'{row}')
        return result

    def search_by_surname(self, surname):
        print('Search by Surname')
        cursor = self.db.cursor();
        cursor.execute('select * from Teachers where Surname = ?', surname)
        result = []
        for row in cursor:
            result.append(f'{row}')
        return result

    def search_by_degree(self, degree):
        print('Search by Pesel')
        cursor = self.db.cursor();
        cursor.execute('select * from Teachers where Degree = ?', degree)
        result = []
        for row in cursor:
            result.append(f'{row}')
        return result

    def search_by_app_login(self, app_login):
        print('Search by App_login')
        cursor = self.db.cursor();
        cursor.execute('select * from Teachers where App_login = ?', app_login)
        result = []
        for row in cursor:
            result.append(f'{row}')
        return result

    def insert(self, pesel, name, surname, degree):
        print('Insert')
        cursor = self.db.cursor()
        cursor.execute('insert into Teachers(Pesel, Name, Surname, Degree) values(?,?,?,?);',
        pesel, name, surname, degree)
        cursor.commit()
        self.read_all()

    def update_surname(self, pesel, new_surname):
        print('Update')
        cursor = self.db.cursor()
        cursor.execute('update Teachers set Surname = ? where Pesel = ?;',
        new_surname, pesel)
        cursor.commit()
        self.read_all()

    def delete(self, pesel):
        print('Delete')
        cursor = self.db.cursor()
        cursor.execute('delete from Teachers where Pesel = ?;',
        pesel)
        cursor.commit()
        self.read_all()