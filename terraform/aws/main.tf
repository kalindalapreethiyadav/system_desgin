locals {
  environment = "dev"
  region      = "us-east-1"
  name_prefix = "myapp-${local.environment}"
}

module "aws_instance" {
    source = "./modules/ec2"
}

