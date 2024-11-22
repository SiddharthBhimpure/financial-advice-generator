import boto3
import botocore.config
import json
from datetime import datetime

def financial_advice_generate_using_bedrock(financial_query:str)-> str:
    # Updated prompt structure for the new model
    prompt = f"""<s>[INST] Provide personalized financial advice based on the following query: {financial_query} [/INST]"""

    body = {
        "prompt": prompt,
        "max_tokens": 200,
        "temperature": 0.5,
        "top_p": 0.9,
        "top_k": 50
    }

    try:
        bedrock = boto3.client("bedrock-runtime", region_name="us-east-1",
                               config=botocore.config.Config(read_timeout=300, retries={'max_attempts': 3}))
        # Use the updated model ID
        response = bedrock.invoke_model(body=json.dumps(body), modelId="mistral.mixtral-8x7b-instruct-v0:1")

        response_content = response.get('body').read()
        response_data = json.loads(response_content)
        print(response_data)
        advice = response_data.get('generation', '')  # Handle case if 'generation' is not present
        return advice
    except Exception as e:
        print(f"Error generating financial advice: {e}")
        return ""

def save_advice_to_s3(s3_key, s3_bucket, generated_advice):
    s3 = boto3.client('s3')

    try:
        s3.put_object(Bucket=s3_bucket, Key=s3_key, Body=generated_advice)
        print("Financial advice saved to S3")
    except Exception as e:
        print("Error when saving financial advice to S3")

def lambda_handler(event, context):
    # Parse the input event
    event = json.loads(event['body'])
    financial_query = event['financial_query']

    # Generate financial advice using the query
    generated_advice = financial_advice_generate_using_bedrock(financial_query=financial_query)

    if generated_advice:
        current_time = datetime.now().strftime('%H%M%S')
        s3_key = f"financial-advice-output/{current_time}.txt"
        s3_bucket = 's3b12'
        save_advice_to_s3(s3_key, s3_bucket, generated_advice)
    else:
        print("No financial advice was generated")

    return {
        'statusCode': 200,
        'body': json.dumps('Financial advice generation is completed')
    }
