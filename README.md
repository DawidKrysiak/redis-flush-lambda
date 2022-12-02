# redis-flush-lambda
a simple tool to flush AWS Elasticache for Redis


## Deployment

### Preparations
* modify the code to add the access point to your Redis cluster
* prepare the package

```
cd <directory with the script>
pip install  redis -t .
```
* zip the content of the folder

* deploy Lambda by uploading the zip
* make sure Lambda function has access to your cluster (most likely you'll have to deploy lambda into a vpc where the cluster is deployed

## Usage
If you wish to automate the cleardown rather than trigger it manually:
* create an SNS topic
* add your Lambda as a subscriber
* create a CloudWatch alarm monitoring the Namespace: AWS/ElastiCache, Metric name: DatabaseMemoryUsagePercentage and triggered at a desired level
* subscribe your SNS topic to ALARM and OK

