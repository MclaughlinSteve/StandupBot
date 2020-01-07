import json
import random

def lambda_handler(event, context):
    order = event['text'].split()
    random.shuffle(order)
    return {
        'statusCode': 200,
        "response_type": "in_channel",
        "text": 'Today\'s order is ' + ' '.join(order)
    }
