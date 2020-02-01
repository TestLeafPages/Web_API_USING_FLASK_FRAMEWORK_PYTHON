import boto3

# s3_obj = boto3.resource('s3', aws_access_key_id="", aws_secret_access_key="")
s3_obj = boto3.resource('s3')
print(type(s3_obj))

# list out all buckets
for each_bucket in s3_obj.buckets.all():
    print(each_bucket.name)

# # upload file in to specific bucket:-
s3_obj.Bucket('gopinath_jayakumar').put_object(Key='python_snake.db')
print('Uploaded')
