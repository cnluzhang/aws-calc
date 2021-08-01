import boto3
import sys

num_dic = {"nano": 0.25, "micro": 0.5, "small": 1, "medium": 2, "large": 4, "xlarge": 8, "2xlarge": 16, "4xlarge": 32,
           "8xlarge": 64, "12xlarge": 96, "16xlarge": 128, "18xlarge": 144, "24xlarge": 192}


class Resource(object):
    def __init__(self, region_name):
        self.region_name = region_name
        self.session = boto3.Session()

    @staticmethod
    def ec2_num(*args, **kwargs):
        for instance in args:
            try:
                if "State" in instance.keys() and instance["State"] != "active":
                    continue
                else:
                    type_size = instance["InstanceType"].split(".")
                    instance_type = type_size[0]
                    instance_size = type_size[1]

                    if instance_type in kwargs.keys():
                        kwargs[instance_type] = kwargs[instance_type] + num_dic[instance_size] * instance[
                            "InstanceCount"]
                    else:
                        kwargs[instance_type] = num_dic[instance_size] * \
                            instance["InstanceCount"]
            except AttributeError:
                if instance.state["Name"] == "running":
                    type_size = instance.instance_type.split(".")
                    instance_type = type_size[0]
                    instance_size = type_size[1]

                    if instance_type in kwargs.keys():
                        kwargs[instance_type] = kwargs[instance_type] + \
                            num_dic[instance_size]
                    else:
                        kwargs[instance_type] = num_dic[instance_size]
                else:
                    continue

        print(kwargs)

    def ec2_running_instances(self):
        ec2 = self.session.resource("ec2", region_name=self.region_name)
        instance_iterator = ec2.instances.all()
        return instance_iterator

    def ec2_reserved_instances(self):
        ec2 = boto3.client("ec2", region_name=self.region_name)
        response = ec2.describe_reserved_instances(DryRun=False)
        instance_list = response["ReservedInstances"]
        return instance_list


if __name__ == "__main__":
    service = Resource(sys.argv[1])

    ec2_instance_dic = {}
    ec2_running_list = service.ec2_running_instances()
    ec2_reserved_list = service.ec2_reserved_instances()
    print("EC2 Calc: ")
    print("Running Instances: ")
    service.ec2_num(*ec2_running_list, **ec2_instance_dic)
    print("Reserved Instances: ")
    service.ec2_num(*ec2_reserved_list, **ec2_instance_dic)
