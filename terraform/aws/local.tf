########################################
#Developer: Preethi
# Terraform POc's
########################################

locals {
  environment = "dev"
  region      = "us-east-1"
  name_prefix = "myapp-${local.environment}"
}

