terraform {
  backend "s3" {
    bucket         = var.BUCKET_NAME
    key            = "terraform.tfstate"
    region         = "us-east-1"
    encrypt        = false
    #dynamodb_table = "terraform-locks" #
  }
}