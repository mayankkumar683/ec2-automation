import boto3

ec2 = boto3.resource('ec2', region_name='ap-south-1')  # Mumbai

instance = ec2.create_instances(
    ImageId='ami-053b0d53g279acc90',  # Ubuntu 22.04 LTS AMI (latest)
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='webkey',   # <-- Replace this!
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Name', 'Value': 'MyPythonInstance'}
            ]
        }
    ]
)

print("Launching EC2 Instance with ID:", instance[0].id)
