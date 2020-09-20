import json
import boto3
import csv
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
s3_client = boto3.client('s3')
def lambda_handler(event, context):
    # TODO implement
    bucket = event['Records'][0]['s3']['bucket']['name']
    csv_file = event['Records'][0]['s3']['object']['key']
    csv_file_obj = s3_client.get_object(Bucket=bucket, Key=csv_file)
    lines = csv_file_obj['Body'].read().decode('utf-8').split()
    results = []
    for row in csv.DictReader(lines):
        results.append(row.values())
    print(results)
    connection = mysql.connector.connect(host='app1project1db.cdtvwz5lqonj.us-east-1.rds.amazonaws.com',database='employeedb',user='admin',
    password='UlMysql#436')
    mysql_empsql_insert_query = "INSERT INTO employee (empid, empname, empaddress)    VALUES (%s, %s, %s)"
    cursor = connection.cursor()
    cursor.executemany(mysql_empsql_insert_query,results)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into employee table")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
