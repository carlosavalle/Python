import boto3

iam = boto3.client('iam')
sns = boto3.client('sns', region_name='us-west-2')#check your region
iamresponse  = iam.list_users()
NoMFA =[]

for user in iamresponse ['Users']:
    MfaUser = iam.list_mfa_devices(UserName=user['UserName']) 
    if len(MfaUser['MFADevices']) == 0:
        NoMFA.append(user['UserName']) 
print(NoMFA)
if len(NoMFA)>0:       
    snsresponse = sns.publish(
    TopicArn='arn:aws:sns:us-west-2:688648888474:Carlos', #Change for your SNS ARN   
    Message='These Users do not have MFA Enabled: \n\n' + '\n'.join(NoMFA)
)
