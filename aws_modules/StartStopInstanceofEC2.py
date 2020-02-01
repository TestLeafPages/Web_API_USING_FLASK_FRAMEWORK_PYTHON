import os
import boto3


def welcome():
    print('This script will help you to start or stop ec2 instances based on your required region and instance id')


def get_ec2_con_for_region(my_region):
    session = boto3.Session(aws_access_key_id='AKIAJ62FNY6IVYG5SVOQ',
                            aws_secret_access_key='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',
                            region_name=my_region)
    ec2_con_re = session.resource('ec2')
    return ec2_con_re


def list_instances_on_my_region(ec2_con_re):
    for each in ec2_con_re.instances.all():
        print(each.id)


def get_instance_state(ec2_con_re, in_id):
    for each in ec2_con_re.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': [in_id]}]):
        pr_st = each.state['Name']
        return pr_st


def start_instance(ec2_con_re, in_id):
    pr_st = get_instance_state(ec2_con_re, in_id)
    print(pr_st)
    if (pr_st == 'running'):
        print('Instance is already running')
    else:
        for each in ec2_con_re.instances.filter(Filters=[{'Name': 'instance-id', 'Values': [in_id]}]):
            each.start()
            print('please wait it is going to start, once if it is started then we will let you know')
            each.wait_until_running()
            print('now it is running')


def stop_instance(ec2_con_re, in_id):
    pr_st = get_instance_state(ec2_con_re, in_id)
    if (pr_st == 'stopped'):
        print('Instance is already stopped')
    else:
        for each in ec2_con_re.instances.filter(Filters=[{'Name': 'instance-id', 'Values': [in_id]}]):
            each.stop()
            print('please wait it is going to stop, once if it is stopped  then we will let you know')
            each.wait_until_stopped()
            print('now it is stopping')


def thank_you():
    print('\n\n *************Thank you for using this script***************')
    return None


def main():
    welcome()
    my_region = input('Enter the region_name: ')
    print("please wait....... connecting to your aws ec2 console.....")

    ec2_con_re = get_ec2_con_for_region(my_region)
    print(f'please wait listing all instances ids in your region {my_region}')
    list_instances_on_my_region(ec2_con_re)

    in_id = input('Now choose your instance id to start or stop: ')
    start_stop = input('Enter either stop or start command for your ec2 instance ')
    while True:
        if start_stop not in ['start', 'stop']:
            start_stop = input('Enter only stop or start commands')
            continue
        else:
            break

    if start_stop == 'start':
        start_instance(ec2_con_re, in_id)
    else:
        stop_instance(ec2_con_re, in_id)

    thank_you()



if __name__ == "__main__":
    os.system('cls')
    main()
