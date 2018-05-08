import mysql.connector

querystring1 = """
    DELETE FROM Attribute
"""
querystring2 = """
    DELETE FROM User
"""

try:
    connection = mysql.connector.connect(host='localhost',
        port=3307,
        database='raw_ta',
        user='root',
        password='password')
    if connection.is_connected():
        print('Connected to MySQL database')
    
    cursor = connection.cursor()
    cursor.execute(querystring1)
    connection.commit()
    cursor.execute(querystring2)
    connection.commit()

except Error as e:
    print(e)

finally:
    connection.close()
    print('Connection closed.')