import os

def lambda_handler(event, context):
    username = event['queryStringParameters']['username']
    environment = os.getenv('ENVIRONMENT', 'staging')
    
    if environment == 'staging':
        api_url = "https://staging.api.example.com"
    else:
        api_url = "https://api.example.com"

    return {
        'statusCode': 200,
        'body': f"Hello, {username}. Environment: {environment}. API URL: {api_url}"
    }
