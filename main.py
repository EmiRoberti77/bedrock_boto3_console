import boto3
import json

bedrock_runtime = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)
while (True):
    prompt = input('=> ')
    if (prompt == 'x'):
        print('bye for now')
        break

    kwargs = {
        "modelId": "ai21.j2-ultra-v1",
        "contentType": "application/json",
        "accept": "*/*",
        "body": "{\"prompt\":\""+prompt+"\",\"maxTokens\":200,\"temperature\":0.7,\"topP\":1,\"stopSequences\":[],\"countPenalty\":{\"scale\":0},\"presencePenalty\":{\"scale\":0},\"frequencyPenalty\":{\"scale\":0}}"
    }
    # print(kwargs)
    response = bedrock_runtime.invoke_model(**kwargs)
    # print(response)
    response_body = json.loads(response.get('body').read())
    print(response_body)
    print("________________________________________________")
    print("________________________________________________")
    print("________________________________________________")
    print("________________________________________________")
    print("________________________________________________")
    print("________________________________________________")
    completion = response_body.get('completions')[0].get('data').get('text')
    print(completion)
