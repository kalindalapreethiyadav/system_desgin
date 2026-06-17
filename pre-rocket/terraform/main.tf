module "aws_iam_role" {
    source = "./modules/iam"
}

module "ec2_server" {
    source = "./modules/ec2"
    ec2_instance_profile_name  = module.iam.ec2_instance_profile_name
}