
########################################
#Developer: Preethi
# Terraform POc's
########################################

/*To store the Terraform state file in a remote backend (like AWS S3), 
you define the backend configuration in a file typically named backend.tf. 

bucket --> Name of the S3 bucket to store the state file.
key: Path within the bucket (acts like a file path).
region: AWS region where the bucket is located.
dynamodb_table: (Optional) Enables state locking to prevent concurrent changes.
encrypt: Ensures the state file is encrypted at rest. */
########################################################


terraform {
  backend "s3" {
    bucket = "poc-terraform-statefile-preek"
    region = "us-east-1"
    key = "dev/terraform.tfstate"
   # dynamodb_table = "terraform-locks"  # <1.10 terraform version - works
    use_lockfile = true
    encrypt = true
  }
}

#With Terraform 1.10, HashiCorp introduced native S3 locking. 
#By simply adding a new parameter “use_lockfile = true”, 
#Terraform will automatically create a lock file in your S3 bucket whenever a state-changing operation is in progress. 
#Once the process is done, the lock is released