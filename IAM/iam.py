import boto3, sys

access_console = boto3.session.Session(profile_name = 'username')

def client_code():
    #define service
    console_iam = access_console.client('iam')

    #print all data
    print(console_iam.list_users())

    #print specific data
    for i in console_iam.list_users()['Users']:
        print(i.get('UserName'))
    
def resource_code():
    #define service
    console_iam = access_console.resource('iam')

    #print all data
    for i in console_iam.users.all():
        print(i)

    #alternatively
    n = 5
    for i in console_iam.users.limit(n):
        print(i)
        
    #print specific data
    for i in console_iam.users.all(): 
        print(i.user_name)
        
    #alternatively
    for i in console_iam.users.limit(10): 
        print(i.user_name)

if __name__ == '__main__':
    x = 'client'
    y = 'resource'
    try:
        if sys.argv[1] == x: client_code()
        if sys.argv[1] == y: resource_code()
    except Exception as e:
        print('Use either client or resource as command line argument')
        sys.exit()
        
    
