import pymysql.cursors

def initConnectionSettings():
    config = {'user_name':'python',
        'password':'Zeppelin32!',
        'host': '192.168.0.18',
        'db':'ncaa_basketball_test',
        'charset':'utf8mb4',
        'cursorclass':pymysql.cursors.DictCursor,
        'port':3306
        }

    return config

def createConnection():
    connSettings = initConnectionSettings();

    connection = pymysql.connect(host=connSettings['host'],
                                 user=connSettings['user_name'],
                                 password=connSettings['password'],
                                 db=connSettings['db'],
                                 port=connSettings['port'],
                                 charset=connSettings['charset'],
                                 cursorclass=connSettings['cursorclass'])

    return connection
    
    