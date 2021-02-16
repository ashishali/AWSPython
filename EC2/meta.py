import boto3 as b3
import sys
from pprint import pprint

def metaTest():
    access_console  = b3.session.Session(profile_name='charlie')
    service_console = access_console.resource('ec2')

    li = service_console.meta.client.describe_regions().get('Regions')

    for i in li:
        pprint(i['Endpoint'] + ' : ' + i['RegionName'])

metaTest()
