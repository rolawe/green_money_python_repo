#AWS Service Inventory

#The list should be empty initially
aws_service_inventory = []


#Populate the list using append or insert
aws_service_inventory.append("S3")
aws_service_inventory.append("Lamda")
aws_service_inventory.append("EC2")
aws_service_inventory.append("DynamoDB")
aws_service_inventory.append("Elasticache")
aws_service_inventory.insert(2, "LightSail")
aws_service_inventory.insert(4, "Cloud9")


#Print the list and length of the list
print(aws_service_inventory)
print(len(aws_service_inventory))


#Remove two specific services from the list by name or by index
aws_service_inventory.remove("Lamda")
del aws_service_inventory[2]



#Print the new list and the new length of the list
print(aws_service_inventory)
print(len(aws_service_inventory))