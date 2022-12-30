import pymysql


conn = pymysql.connect(host='localhost',
                       user='root',
                       password='chy200412',
                       database='proxy_pool')
cursor = conn.cursor()
