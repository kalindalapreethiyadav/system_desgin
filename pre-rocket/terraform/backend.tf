terraform {
  backend "s3" {
    bucket         = "$Environment-$Tenant-bucket-bucket"
    key            = "terraform.tfstate"
    region         = "us-east-1"
    encrypt        = false
    #dynamodb_table = "terraform-locks" #
    use_lockfile = true
  }
}