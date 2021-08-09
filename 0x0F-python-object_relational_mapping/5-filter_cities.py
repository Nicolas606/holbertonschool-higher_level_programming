#!/usr/bin/python3
''' script that takes in the name of a state as an argument and lists all
    cities of that state, using the database hbtn_0e_4_usa'''

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    # User credentials
    user_name = argv[1]
    user_pass = argv[2]
    db_name = argv[3]
    state_name = argv[4]
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
    sql = """SELECT cities.name FROM cities
             JOIN states ON cities.state_id = states.id
             WHERE states.name = %s"""
    cursor.execute(sql, (state_name,))
    result = cursor.fetchall()

    # print each elements in result
    if len(result) == 0:
        print("")

    for i in range(len(result)):
        if i < len(result) - 1:
            print(result[i][0], end=", ")
        else:
            print(result[i][0])

    # disconnect from server
    cursor.close()
    db.close()
