import boto3

def get_account_details():
    access_console = boto3.session.Session(profile_name='username')
    service_sts    = access_console.client('sts')

    print(service_sts.get_access_key_info(AccessKeyId='access_key'))
    print(service_sts.get_caller_identity())
    print(service_sts.get_federation_token(Name='name'))
    print(service_sts.get_session_token())

get_account_details()
