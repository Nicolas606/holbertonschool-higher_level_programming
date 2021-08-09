#!/usr/bin/python3
''' script that takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument.'''

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    # User credentials
    user_name = argv[1]
    user_pass = argv[2]
    db_name = argv[3]
    name = argv[4]
    host_name = 'localhost'
    host_port = 3306

    # Connect to MySQL DB and create the cursor
    db = MySQLdb.connect(host_name,
                         user_name,
                         user_pass,
                         db_name,
                         port=host_port)
    cursor = db.cursor()

    # Make and tun query
    sql = """SELECT * FROM states
            WHERE BINARY states.name='{}'
            COLLATE latin1_general_cs
            ORDER BY states.id""".format(name)
    cursor.execute(sql)
    result = cursor.fetchall()

    # print each elements in result
    for each in result:
        print(each)

    # disconnect from server
    cursor.close()
    db.close()
