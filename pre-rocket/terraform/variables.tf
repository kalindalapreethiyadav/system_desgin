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

variable "AWS_ACCESS_KEY_ID" {
  description = "This is access key"
  type        = string
  default     = "bdhduohsjabckjsc"
}

variable "AWS_SECRET_ACCESS_KEY" {
  description = "This is secert key"
  type        = string
  default     = "bdhduohsjabckjsc"
}

variable "region" {
  type    = string
  default = "us-east-1"
}

variable "ec2_instance_profile_name" {
  type    = string
  default = "ec2-profile-name"
}

variable "subnet_id" {
  type    = string
  default = "subnet-ibahdaouhou87"
}

variable "cidr_block" {
  type    = string
  default = "10.0.0.0/16"
}

variable "Environment" {
  description = "Environment name"
  type        = string
  default     = "dev"
}

variable "Tenant" {
  description = "Tenant name"
  type        = string
  default     = "zerohunger"
}

variable "ssm_role_name" {
  type = string
}