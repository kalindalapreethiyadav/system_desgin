########################################
#Developer: Preethi
# Terraform POc's
########################################

resource "aws_instance" "main_default" {
    instance_type = "t2.micro"
    ami           = "resolve:ssm:/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64"
    security_groups = var.security_group_id
    tags = {
        description = "ec2-default"
        owner = "preethi@gmail.com"
        name = "$var.prefix-$var.env"
    }

    lifecycle {
        # create_before_destroy = true
        # prevent_destroy = false
        ignore_changes = [ tags ]
    }

}