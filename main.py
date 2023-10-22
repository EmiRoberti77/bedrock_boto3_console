import boto3
import json

bedrock_runtime = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

prompt = "create a story about a planet called Foo"


kwargs = {
    "modelId": "anthropic.claude-v2",
    "contentType": "application/json",
    "accept": "*/*",
    "body": "{\"prompt\":\"Human: "+prompt+"\\nAssistant:\",\"max_tokens_to_sample\":300,\"temperature\":1,\"top_k\":250,\"top_p\":0.999,\"stop_sequences\":[\"\\n\\nHuman:\"],\"anthropic_version\":\"bedrock-2023-05-31\"}"
}

response = bedrock_runtime.invoke_model_with_response_stream(**kwargs)
stream = response.get('body')
if stream:
    for event in stream:
        chunk = event.get('chunk')
        if (chunk):
            print(json.loads(chunk.get('bytes')).get('completion'), end="")
