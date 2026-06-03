module "aws_instance" {
    source = "./modules/ec2"
    security_group_id = [module.security_groups.secuirty_group_ID]
}

# resource "local_file" "local_default" {
#     filename = "./locals/records.tf"
#     content = "CNAME: A"
# }

