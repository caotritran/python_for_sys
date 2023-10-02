import boto3

def get_acm_arn(domain_name, region):
    session = boto3.Session(profile_name='aprod')
    client = session.client('acm', region_name=region)
    arn = None
    next_token = None
    
    while True:
        response = client.list_certificates(NextToken=next_token) if next_token else client.list_certificates()
        
        for cert in response['CertificateSummaryList']:
            if cert['DomainName'] == domain_name:
                return cert['CertificateArn']
        
        # Check if there are more pages
        if 'NextToken' in response:
            next_token = response['NextToken']
        else:
            break  # No more pages
        
    return arn

if __name__ == "__main__":
    print(get_acm_arn("*.domainabc.xyz", "us-east-1"))
