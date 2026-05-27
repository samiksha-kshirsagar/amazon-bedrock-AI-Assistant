# Amazon Bedrock AI Assistant

An AI-powered assistant built using Amazon Bedrock that enables users to interact with foundation models through a simple interface. This project demonstrates how to connect AWS Lambda with Amazon Bedrock for generating intelligent AI responses.

# Features
AI-powered chatbot
Uses Amazon Bedrock foundation models
Serverless backend using AWS Lambda
Secure AWS integration
Fast and scalable architecture

# Prerequisites

Before running the project, ensure you have:

AWS Account
IAM User with Bedrock permissions
Python 3.10+
AWS CLI configured
Access enabled for Amazon Bedrock models

Enable model access from the Amazon Bedrock Console.

# How It Works
User enters a prompt in the application.
app.py sends the request.
lambda_function.py processes the request.
bedrock_client.py connects to Amazon Bedrock.
Bedrock generates the AI response.
Response is displayed to the user.
