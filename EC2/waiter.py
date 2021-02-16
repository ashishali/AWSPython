import boto3 as b3
import sys
from pprint import pprint

class ResourceWaiter:
    def __init__(self) -> None:
        access_console       = b3.session.Session(profile_name = 'username', region_name = 'region')
        self.service_console = access_console.resource('ec2')

    def get_id(self):
        for i,j in enumerate(self.service_console.instances.all(), start=1):
            print(i, j.id, j.state['Name'])
    
    def start(self, id):
        id = self.id 
        ob_id = ''.join(id)
        try:
            print("\nStarting instance {}".format(id))
            self.service_console.instances.filter(InstanceIds=id).start()
            ob = self.service_console.Instance(ob_id)
            ob.wait_until_running()
            print("\nStarted {}".format(ob_id))
            sys.exit()

        except Exception as e:
            print(e)

    def stop(self, id):
        id    = self.id 
        ob_id = ''.join(id)
        try:
            print("\nStopping instance {}".format(id))
            self.service_console.instances.filter(InstanceIds=id).stop()
            ob = self.service_console.Instance(ob_id)
            ob.wait_until_stopped()
            print("\nStopped {}".format(ob_id))
            sys.exit()

        except Exception as e:
            print(e)

    
    def terminate(self, id):
        id    = self.id 
        ob_id = ''.join(id)
        try:
            print("Terminating instance {}".format(id))
            self.service_console.instances.filter(InstanceIds=id).terminate()
            ob = self.service_console.Instance(ob_id)
            ob.wait_until_stopped()
            print("Terminated {}".format(ob_id))
            sys.exit()

        except Exception as e:
            print(e)


    def main(self):
        self.id = []
        self.get_id()

        for i in range(0,1):
            temp = input("ID: ")
            self.id.append(temp)

        while True:
            ask = int(input("1. Start\n2. Stop\n3. Terminate\n4. Exit \nPunch in the option:"))

            if ask   == 1: self.start(self.id)
            elif ask == 2: self.stop(self.id)
            elif ask == 3: self.terminate(self.id)
            elif ask == 4: sys.exit()
            else:
                print('Invalid Choice\n')


r = ResourceWaiter()
r.main()
