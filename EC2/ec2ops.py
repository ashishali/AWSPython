import boto3 as b3
import sys


class ec2Ops:

    def __init__(self):
        access_console = b3.session.Session(profile_name = 'username', region_name = 'region')
        self.console_ec2 = access_console.resource('ec2')

    def get_id(self):
        for i,j in enumerate(self.console_ec2.instances.all(),start=1):
            print(str(i)+'. ',j.id,'[',j.state.get('Name'),']')

    def start(self, id):
        id = self.id 
        try:
            self.console_ec2.instances.filter(InstanceIds=id).start()
            print("\nStarting instance {}".format(id))
            sys.exit()

        except Exception as e:
            print(e)

    def stop(self, id):
        id = self.id 
        try:
            self.console_ec2.instances.filter(InstanceIds=id).stop()
            print("\nStopping instance {}".format(id))
            sys.exit()

        except Exception as e:
            print(e)

    def terminate(self, id):
        id = self.id 
        try:
            self.console_ec2.instances.filter(InstanceIds=id).terminate()
            print("\nTerminating instance {}\nNote: This action cannot be undone\n".format(id))
            sys.exit()

        except Exception as e:
            print(e)


    def main(self):
        self.id = []
        n = 1 #n can be greater than 1 based on the requirement
        self.get_id()

        for i in range(0,n):
            temp = input("ID: ")
            self.id.append(temp)

        while True:
            ask = int(input("1. Start\n2. Stop\n3. Terminate\n4. Exit\nPunch in the option:"))

            if ask   == 1: self.start(self.id)
            elif ask == 2: self.stop(self.id)
            elif ask == 3: self.terminate(self.id)
            elif ask == 4: sys.exit()
            else:
                print('Invalid Choice\n')

        
ob = ec2Ops()
ob.main()
        
