import boto3

access_console = boto3.session.Session(profile_name = 'username')

def client_code():
  #define service
  service_iam = access_console.client('iam')
  
  #print all data
  print(service_iam.list_users())
  
  #print specific data
  for i in console_iam.list_users()['Users']:
    print(i.get('UserName'))
    
def resource_code():
  #define service
  service_iam = access_console.resource('iam')
  
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
