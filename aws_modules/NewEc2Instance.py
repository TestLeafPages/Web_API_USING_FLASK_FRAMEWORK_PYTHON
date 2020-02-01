import boto3

session = boto3.Session(aws_access_key_id='AKIAJ62FNY6IVYG5SVOQ',
                        aws_secret_access_key='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',
                        region_name='ap-south-1')

ec2_con_re = session.resource('ec2')

for each_instance in ec2_con_re.instances.all():
    print(each_instance.id)