import pyodbc

def connect_to_db():
    connection = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server=DESKTOP-8H66QCO;" # change to your server, rest should be the same
        "Database=university;"
        "Trusted_Connection=yes;"
    )
    return connection