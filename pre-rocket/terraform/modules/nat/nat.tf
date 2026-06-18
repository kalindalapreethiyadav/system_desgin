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

resource "aws_eip" "nat" {
  domain = "vpc"
}

resource "aws_nat_gateway" "nat" {
  allocation_id = aws_eip.nat.id
  subnet_id     = aws_subnet.public[0].id
}