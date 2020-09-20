import json
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
def lambda_handler(event, context):
    connection = mysql.connector.connect(host='app1project1db.cdtvwz5lqonj.us-east-1.rds.amazonaws.com',database='employeedb',user='admin',
    password='UlMysql#436')
    mysql_empsql_insert_query = "INSERT INTO employee (empid, empname, empaddress)    VALUES (%s, %s, %s)"
    rows = [['300', 'vamsi',  'AP'],['400', 'krishna',  'Karnataka']]
    cursor = connection.cursor()
    cursor.executemany(mysql_empsql_insert_query,rows)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into employee table")
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
