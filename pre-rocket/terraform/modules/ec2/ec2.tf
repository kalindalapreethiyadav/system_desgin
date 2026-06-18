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

resource "aws_instance" "ec2" {
  ami           = "ami-0152204c1a187337c"
  instance_type = "t2.micro"
  iam_instance_profile = var.ec2_instance_profile_name
  subnet_id = var.subnet_id

  tags = {
    Name = "docker-instance",
    env = "dev"
  }
}