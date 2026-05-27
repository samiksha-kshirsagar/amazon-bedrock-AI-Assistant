# Amazon Bedrock AI Assistant

An AI-powered assistant built using Amazon Bedrock that enables users to interact with foundation models through a simple interface. This project demonstrates how to connect AWS Lambda with Amazon Bedrock for generating intelligent AI responses.

# Features
AI-powered chatbot

1. Uses Amazon Bedrock foundation models
2. Serverless backend using AWS Lambda
3. Secure AWS integration
4. Fast and scalable architecture

# Prerequisites

Before running the project, ensure you have:

1. AWS Account
2. IAM User with Bedrock permissions
3. Python 3.10+
4. AWS CLI configured
5. Access enabled for Amazon Bedrock models

Enable model access from the Amazon Bedrock Console.

# How It Works
1. User enters a prompt in the application.
2. app.py sends the request.
3. lambda_function.py processes the request.
4. bedrock_client.py connects to Amazon Bedrock.
5. Bedrock generates the AI response.
6. Response is displayed to the user.
