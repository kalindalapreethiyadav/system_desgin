########################################
#Developer: Preethi
# Terraform POc's
########################################

resource "aws_instance" "main_default" {
    instance_type = "t2-micro"
    ami = "ami-83hf892gh894gf79"
    tags = {
        description = "ec2-default"
        owner = "preethi@gmail.com"
    }
}