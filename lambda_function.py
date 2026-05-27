from bedrock_client import BedrockClient

client = BedrockClient()

def lambda_handler(event, context):

    prompt = event.get("prompt", "Hello AI")

    result = client.invoke(prompt)

    return {
        "statusCode": 200,
        "body": result
    }