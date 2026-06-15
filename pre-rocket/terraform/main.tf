terraform {
  backend "s3" {
    bucket         = "${var.Tenant}-${var.Env}"
    key            = "envs/dev/terraform.tfstate"
    region         = "ap-south-1"
    encrypt        = true
  }
}
