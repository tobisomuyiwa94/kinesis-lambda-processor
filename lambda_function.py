import base64
import json

def lambda_handler(event, context):
    for record in event['Records']:
        # Decode the base64 data
        decoded_data = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        print(f"Decoded payload: {decoded_data}")
        
        # Attempt JSON parsing only if the decoded data seems JSON-like
        try:
            payload = json.loads(decoded_data)
            print(f"Parsed JSON payload: {payload}")
        except json.JSONDecodeError:
            # Handle the case where decoded data is not JSON
            print("Decoded data is not in JSON format or is empty")
            
    return {'statusCode': 200, 'body': 'Data processed successfully'}
