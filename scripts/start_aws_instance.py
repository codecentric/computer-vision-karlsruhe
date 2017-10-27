""" simple boto3 script to launch AWS instances

* 25.10.2017 - Oli Moser (https://twitter.com/moseroli)
"""
import boto3

boto3.setup_default_session(profile_name='codecentric', region_name='eu-west-1')
ec2 = boto3.resource('ec2')

filters = [{'Name': 'tag:Name', 'Values': ['computer-vision-gpu']}]

instances = ec2.instances.filter(Filters=filters)
num_instances = len(list(instances))

# expecting exactly 1 instance ... else break here
assert num_instances == 1

instance = list(instances).pop()


def start_instance(instance):
    if instance.state['Name'] == 'stopped':
        print("instances is currently stopped. starting it ... ")
        print(instance.start())
    else:
        print("instance not in stopped state. skipping.")


def get_public_ip(instance):
    print("Instance Pubilic IP: {0}".format(instance.public_ip_address))


start_instance(instance)
get_public_ip(instance)
