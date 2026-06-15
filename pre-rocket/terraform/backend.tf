terraform {
  backend "s3" {
    bucket         = "${var.Tenant}-${var.Enviornment}-bucket"
    key            = "${var.Tenant}/${var.Enviornment}/terraform.tfstate"
    region         = "ap-south-1"
    encrypt        = true
    #dynamodb_table = "terraform-locks" #
    use_lockfile = true
  }
}