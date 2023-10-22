import boto3
import json

bedrock_runtime = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

prompt = """here is the text between the <text></text> tags
<text>i have been to the beach and had ice cream</text>
Give me a title to put in these tags <title></title>""".encode('unicode_escape').decode('utf-8')


kwargs = {
    "modelId": "anthropic.claude-v2",
    "contentType": "application/json",
    "accept": "*/*",
    "body": "{\"prompt\":\"Human: "+prompt+"\\nAssistant:\",\"max_tokens_to_sample\":300,\"temperature\":1,\"top_k\":250,\"top_p\":0.999,\"stop_sequences\":[\"\\n\\nHuman:\"],\"anthropic_version\":\"bedrock-2023-05-31\"}"
}

response = bedrock_runtime.invoke_model(**kwargs)
response_body = json.loads(response.get('body').read())
print(response_body)
print("________________________________________________")
completion = response_body.get('completion')
print(completion)
