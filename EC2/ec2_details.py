import boto3, sys

access_console = boto3.session.Session(profile_name = 'username', region_name = 'region_name')

def resource_code():
    counter = 0
    print('Using Resource Code')
    console_ec2 = access_console.resource('ec2')
    for j,i in enumerate(console_ec2.instances.all(), start=1):
        counter += 1
        print("\n{}. Instance Id        : {}".format(j, i.instance_id))
        print("   Image Id           : {}".format(i.image_id))
        print("   Instance type      : {}".format(i.instance_type))
        print("   Launch Time        : {}".format(i.launch_time))
        print("   Private IP Address : {}".format(i.private_ip_address))
        print("   Public IP Address  : {}".format(i.public_ip_address))

    print("\nTotal Number of Instances: "+str(counter))


def client_code():
    console_ec2 = access_console.client('ec2')
    print('Using Client Code')
    counter = 0 
    for i in console_ec2.describe_instances()['Reservations']:
        for j in i['Instances']:
            counter +=1
            print("\n{}. Instance Id          : {}".format(str(counter), j['InstanceId']))
            print("   Image Id             : {}".format(j['ImageId']))
            print("   Instance Type        : {}".format(j['InstanceType']))
            print("   Launch Time          : {}".format(j['LaunchTime']))
            print("   Private IP Address   : {}".format(j['PrivateIpAddress']))
            print("   Public IP Address    : {}".format(j['PublicIpAddress']))

    print("\nTotal number of instances: "+str(counter))
            
if __name__ == '__main__':
    x = 'client'
    y = 'resource'
    try:
        if sys.argv[1] == x: client_code()
        if sys.argv[1] == y: resource_code()
    except Exception as e:
        print('Use either client or resource as command line argument')
        sys.exit()
