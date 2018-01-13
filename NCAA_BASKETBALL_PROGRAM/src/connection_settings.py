import pymysql.cursors

def initConnectionSettings():
    config = {'user_name':'tester',
        'password':'tester',
        'host': '10.0.0.94',
        'db':'ncaa_basketball_test',
        'charset':'utf8mb4',
        'cursorclass':pymysql.cursors.DictCursor
        }

    return config

def createConnection():
    connSettings = initConnectionSettings();

    connection = pymysql.connect(host=connSettings['host'],
                                 user=connSettings['user_name'],
                                 password=connSettings['password'],
                                 db=connSettings['db'],
                                 charset=connSettings['charset'],
                                 cursorclass=connSettings['cursorclass'])

    return connection
    
    