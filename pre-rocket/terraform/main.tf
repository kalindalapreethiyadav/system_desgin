###################################################################
# Terraform POC - Infrastructure Automation
# This project is a proof of concept demonstrating AWS resource
# provisioning using Terraform modules.
# Copyright (c) 2026 Your Name / Organization
# Permission is granted to use, copy, modify, and distribute this
# software for educational and non-commercial purposes, provided
# this notice is included.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
####################################################################

module "vpc" {
  source     = "./modules/vpc"
  cidr_block = "10.0.0.0/16"

}

module "routetables" {
  source = "./modules/routetables"
  vpc_id = module.vpc.vpc_id
}

module "s3" {
  source      = "./modules/s3"
  bucket_name = "dev-zerohub-app-bucket"
}

module "aws_iam_role" {
  source = "./modules/iam"
}

module "ec2" {
  source                    = "./modules/ec2"
  ec2_instance_profile_name = var.ec2_instance_profile_name
  subnet_id                 = var.subnet_id
  depends_on                = [module.aws_iam_role]
}

module "alb" {
  source      = "./modules/lb"
  lb_name     = "${var.Environment}-${var.Tenant}-lb"
  vpc_id      = module.vpc.vpc_id
  subnet_ids  = module.vpc.public_subnet_ids
  instance_id = module.ec2.instance_id
}

module "igw" {
  source = "./modules/igw"
  vpc_id = module.vpc.vpc_id
}
