# Lambda Function I: Serialise Image Data

import json
import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    """A function to serialize target data from S3"""

    # Get the s3 address from the Step Function event input
    key = event["s3_key"]## TODO: fill in
    bucket = event["s3_bucket"]## TODO: fill in

    # Download the data from s3 to /tmp/image.png
    ## TODO: fill in
    file_name = '/tmp/image.png'
    s3.download_file(bucket, key, file_name)

    # We read the data from a file
    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read())

    # Pass the data back to the Step Function
    print("Event:", event.keys())
    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
        }
    }

# Lambda Function II: Create/Do Inference

import json
import boto3
import base64

rt_sagemaker = boto3.client("runtime.sagemaker")

# Fill this in with the name of your deployed model
ENDPOINT = "image-classification-2022-01-22-15-40-53-009"

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event["image_data"]) 

    # Instantiate a Predictor
    response = rt_sagemaker.invoke_endpoint(EndpointName = ENDPOINT, ContentType= 'image/png', Body=image)
    
    inference = json.loads(response["Body"].read())
    print(inference)
    
    event["inferences"] = inference

    # We return the data back to the Step Function    
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }

# Lambda Function III: Check for Threshold set at 0.9

import json


THRESHOLD = .90
class Threshold_Error(Exception):
    pass

def lambda_handler(event, context):

    # Grab the inferences from the event
    inferences = event["inferences"]

    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = inferences[0] >= THRESHOLD or inferences[1] >= THRESHOLD

    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise Threshold_Error("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }