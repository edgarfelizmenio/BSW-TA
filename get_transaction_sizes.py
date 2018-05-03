import mysql.connector

querystring = """
    SELECT (user.size + attribute.size) as transaction_size FROM
    (SELECT user_id, (
    LENGTH(user_id) +
    IFNULL(LENGTH(first_name), 0) +
    IFNULL(LENGTH(last_name), 0)
    ) AS size FROM User) as user JOIN
    (SELECT user_id, SUM(
            LENGTH(attribute_id) +
            IFNULL(LENGTH(user_id), 0) +
            IFNULL(LENGTH(value), 0)
    ) AS size FROM Attribute
    GROUP BY user_id) as attribute ON user.user_id = attribute.user_id;
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
    cursor.execute(querystring)
    rows = cursor.fetchall()

    transaction_sizes = [int(txn[0]) for txn in rows]

    with open('attribute_transaction_sizes.txt', 'w') as txn_sizes_file:
        txn_sizes_file.writelines(["{}\n".format(txn_size) for txn_size in transaction_sizes])

except Error as e:
    print(e)

finally:
    connection.close()
    print('Connection closed.')