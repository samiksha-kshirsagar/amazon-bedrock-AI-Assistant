import boto3
import json
import time
from botocore.exceptions import ClientError

class BedrockClient:

    def __init__(self):

        self.client = boto3.client(
            service_name="bedrock-runtime",
            region_name="us-east-1"
        )

    def invoke(self, prompt, max_retries=2, initial_wait=1):

        try:

            body = {
                "inputText": prompt
            }

            for attempt in range(max_retries + 1):
                try:
                    response = self.client.invoke_model(
                        modelId="amazon.nova-lite-v1:0",
                        body=json.dumps(body),
                        contentType="application/json",
                        accept="application/json"
                    )

                    response_body = json.loads(
                        response["body"].read()
                    )

                    return str(response_body)

                except ClientError as e:
                    error_code = e.response.get("Error", {}).get("Code", "")
                    
                    if error_code == "ThrottlingException":
                        if attempt < max_retries:
                            wait_time = initial_wait * (2 ** attempt)
                            print(f"Rate limited. Waiting {wait_time} seconds before retry...")
                            time.sleep(wait_time)
                            continue
                        else:
                            return "Error: API quota exceeded for today. Please try again tomorrow or contact AWS support to increase your quota."
                    else:
                        raise

        except Exception as e:

            return f"Error: {str(e)}"