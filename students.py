class Students_Table:

    def __init__(self, db):
        self.db = db

    def read_all(self):
        print("Read All")
        cursor = self.db.cursor();
        cursor.execute('select * from Students')
        for row in cursor:
            print(f'row = {row}')
        print()

    def search_by_pesel(self, pesel):
        print('Search by Pesel')
        cursor = self.db.cursor();
        cursor.execute('select * from Students where Pesel = ?', pesel)
        for row in cursor:
            print(f'row = {row}')
        print()

    def search_by_name(self, name):
        print('Search by Name')
        cursor = self.db.cursor();
        cursor.execute('select * from Students where Name = ?', name)
        for row in cursor:
            print(f'row = {row}')
        print()

    def search_by_surname(self, surname):
        print('Search by Surname')
        cursor = self.db.cursor();
        cursor.execute('select * from Students where Surname = ?', surname)
        for row in cursor:
            print(f'row = {row}')
        print()

    def insert(self, pesel, name, surname):
        print('Insert')
        cursor = self.db.cursor()
        cursor.execute('insert into Students(Pesel, Name, Surname) values(?,?,?);',
        pesel, name, surname)
        cursor.commit()
        self.read_all()

    def update_surname(self, pesel, new_surname):
        print('Update')
        cursor = self.db.cursor()
        cursor.execute('update Students set Surname = ? where Pesel = ?;',
        new_surname, pesel)
        cursor.commit()
        self.read_all()

    def delete(self, pesel):
        print('Delete')
        cursor = self.db.cursor()
        cursor.execute('delete from Students where Pesel = ?;',
        pesel)
        cursor.commit()
        self.read_all()