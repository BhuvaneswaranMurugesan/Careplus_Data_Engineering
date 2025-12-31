import json
import boto3

glue = boto3.client('glue')

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    s3_input_path = f's3://{bucket}/{key}' #

    print(f"Triggering Glue Job with file: {s3_input_path}")

    glue.start_job_run(
        JobName = 'automate_etl_with_glue',
        Arguments = {
            '--input_file_path': s3_input_path
        }
    )