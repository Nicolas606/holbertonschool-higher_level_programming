#!/usr/bin/python3
'''  script that takes in arguments and displays all values in the states table
    of hbtn_0e_0_usa where name matches the argument. But this time, write one
    that is safe from MySQL injections!'''

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
            WHERE states.name=%s"""
    cursor.execute(sql, (name, ))
    result = cursor.fetchall()

    # print each elements in result
    for each in result:
        print(each)

    # disconnect from server
    cursor.close()
    db.close()
