# 💰 AI-Powered Financial Advice Generator  

An AWS Lambda-based application that leverages **Amazon Bedrock (Mistral Mixtral-8x7B)** to generate personalized financial advice. The generated insights are stored in **Amazon S3** for persistence and easy retrieval.  

This project demonstrates **serverless AI application development** using Bedrock, Lambda, and S3 integration.  

---

## 🚀 Features
- ✅ Generate **personalized financial advice** using Amazon Bedrock  
- ✅ Secure and scalable **serverless architecture with AWS Lambda**  
- ✅ Persist generated advice in **Amazon S3**  
- ✅ Error handling for robust performance  
- ✅ Demonstrates **LLM + Cloud integration**  


---

## 🛠️ Tech Stack
- **AWS Lambda** (serverless compute)  
- **Amazon Bedrock** (LLM inference – Mistral Mixtral-8x7B Instruct)  
- **Amazon S3** (data storage)  
- **Python (Boto3 SDK)**  

---

## ⚙️ Setup Instructions  

### 1. Clone the repository
git clone https://github.com/your-username/financial-advice-generator.git
cd financial-advice-generator

### 2. Install dependencies
Make sure you have Python 3.9+ and AWS SDK installed
pip install -r requirements.txt

### 3. Configure AWS
Ensure your AWS CLI is configured with the correct credentials:
aws configure

### 4. Deploy Lambda
Upload the Python script as an AWS Lambda function and attach necessary IAM roles with access to:
bedrock:InvokeModel
s3:PutObject

### 5. Trigger Lambda
Invoke the Lambda function with an event containing a financial_query:

{
  "body": "{\"financial_query\": \"How should I plan for retirement savings at age 30?\"}"
}



## 👤 Author
**Siddharth Bhimpure**  
- 🎓 B.Tech in AI & Data Science  
