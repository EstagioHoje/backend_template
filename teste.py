import boto3
client = boto3.client('dynamodb', aws_access_key_id='yyyy', aws_secret_access_key='xxxx', region_name='us-east-2')

student_table = client.Table('Student')
company_table = client.Table('Company')
teacher_table = client.Table('Teacher')
vacancy_table = client.Table('Vacancy')
report_table = client.Table('Report')
contract_table = client.Table('Contract')



