import boto3

class DynamoDB:
    def __init__(self):
        self.table_name = 'your_table_name'
        self.region_name = 'your_aws_region'
        self.dynamodb = boto3.resource('dynamodb', region_name=self.region_name)
        self.table = self.dynamodb.Table(self.table_name)

    def put_item(self, content):
        self.table.put_item(Item={'content': content})