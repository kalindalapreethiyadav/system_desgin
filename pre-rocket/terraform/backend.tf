terraform {
  backend "s3" {
    bucket         = "dev-zerohunger-bucket"
    key            = "terraform.tfstate"
    region         = "us-east-1"
    encrypt        = false
    #dynamodb_table = "terraform-locks" #
  }
}