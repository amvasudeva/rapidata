#! /usr/bin/python 
import boto3

#AWS_ACCESS_KEY_ID = "AKIAJQV2SI2USW7HZIXQ"
#AWS_SECRET_ACCESS_KEY = "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"

#session = boto3.Session(
#    aws_access_key_id=AWS_ACCESS_KEY_ID,
#    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
#)


#instances = ec2.instances.filter(
#    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
#for instance in instances:
#    print(instance.id, instance.instance_type, instance.key_name, instance.private_ip_address, instance.public_dns_name ,instance.tags[0].get("Value"))


ec2 = boto3.resource('ec2', region_name='us-east-1')
#instance = ec2.create_instances(
#    ImageId='ami-6d1c2007',
#    MinCount=1,
#    MaxCount=1,
#    InstanceType='t2.micro')
#print instance[0].id

s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print bucket.name
    print "---"
    for item in bucket.objects.all():
        print "\t%s" % item.key
