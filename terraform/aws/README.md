# Resource --> which object manged by , 100's of resources can be created.
#HCL - Hashicorp lanaguage to provision the infra structure

<block> "resource type" "resource name" {
    arguments1
    arguments2
}

example:
resource "local_file" "local"
{
    filename = "./locals/records.tf"
    content = "Cname: A"
}

# Instance Types in AWS for Ec2 instance

🔹 General Purpose Instances - Designed for a balance of compute, memory, and networking.
    T Series: t3, t3a, t4g
    M Series: m5, m5a, m5n, m5zn, m6a, m6g, m6i, m7a, m7g, m7i
🔹 Compute Optimized Instances - Ideal for compute-bound applications.
    C Series: c5, c5a, c5n, c6a, c6g, c6i, c7a, c7g, c7i



✅ How Terraform Knows Which AWS Account to Use
Terraform uses the AWS provider, and the credentials you supply determine the account. Here's how you can specify them:

    export AWS_ACCESS_KEY_ID="your-access-key"
    export AWS_SECRET_ACCESS_KEY="your-secret-key"
    export AWS_DEFAULT_REGION="us-east-1"

 2. Shared Credentials File (~/.aws/credentials)
    Use the AWS CLI to configure:

        aws configure --profile dev


To store a Terraform plan locally in a file, you can use the -out flag with the terraform plan command. This is useful for reviewing or applying the plan later.

✅ Command to Save the Plan to a File
    
    terraform plan -out=tfplan.out

This saves the plan to a binary file named tfplan.out.

✅ To Apply the Saved Plan
    
    terraform apply tfplan.out

This ensures that only the changes in the saved plan are applied, which is useful for automation and approvals.

✅ Optional: Convert Plan to Human-Readable Format

    terraform show tfplan.out


If you want to view the plan in a readable format, use:

    terraform show -no-color tfplan.out > plan.txt

Or to save it to a text file:


# terraform init
# terraform plan -out=tfplan.tf
# terraform apply tfplan.out -var-file="dev.tfvars"
# terraform plan -destroy -out=destroy.tfplan
# terraform apply destroy.tfplan
# terraform state rm <address>
# terraform state list
# terraform state show
# terraform state show module.aws_instance.aws_instance.main_default
# terraform taint aws_instance.web # destroy and re-create
# terraform untaint aws_instance.web
# terraform taint module.my_module.aws_instance.web
# terraform import [options] ADDRESS ID
# terraform import aws_instance.my_instance i-1234567890abcdef0  # once import is done...recheck with plan(should match..Zero add,destroy,change)

# terraform apply -lock=false
# terrafomr fmt


Using a Plan File with terraform destroy
You can create a destroy plan and save it to a file like this:

terraform plan -destroy -out=destroy.tfplan

1. Local Values
Terraform allows you to define local variables using the locals block.

locals {
  environment = "dev"
  region      = "us-east-1"
  name_prefix = "myapp-${local.environment}"
}

You can then use these locals throughout your configuration:

resource "aws_s3_bucket" "example" {
  bucket = "${local.name_prefix}-bucket"
  acl    = "private"
}

# terraform taint

terraform taint is a command used to manually mark a resource for recreation during the next terraform apply. It tells Terraform that a particular resource is "tainted" or no longer valid, even if the configuration hasn't changed.

Use Case
You might use terraform taint when:

      --->  A resource is behaving incorrectly or is corrupted.
      --->  You want to force a fresh deployment of a specific resource.
      --->  You’ve made manual changes outside Terraform and want to reset the resource.

# ✅ What is terraform import?

    terraform import is a command that allows you to bring existing infrastructure (created outside of Terraform) under Terraform management without recreating it.

🔧 Why Use It?
    You already have AWS resources (like EC2, S3, RDS) created manually or via another tool.
    You want to manage those resources using Terraform going forward.
    You want to avoid downtime or duplication.

    -->terraform import [options] ADDRESS ID

    terraform import aws_instance.my_instance i-1234567890abcdef0


# ✅ terraform force-unlock Command
    The terraform force-unlock command is used to manually remove a state lock when Terraform gets stuck due to an interrupted or failed operation.

    terraform force-unlock LOCK_ID

    ⚠️ Warning
            Use force-unlock only when you're sure no other Terraform process is running.
            Forcing unlock while another process is active can corrupt your state.


# <filename>.tfvars & <filename>.autotfvars

variables in file should start with "TF_VAR_instance_type=t3.micro

    --> terraform apply tfplan.out -var-file="dev.tfvars"


# local-exec, remote-exec, and file provision


🧩 1. local-exec Provisioner
        Runs a command on the machine where Terraform is executed (your local machine or CI/CD runner).

        🔧 Example:
        ✅ Use Cases:
                Triggering local scripts
                Sending notifications (e.g., Slack, email)
                Running CLI tools (e.g., aws, kubectl)
                
🌐 2. remote-exec Provisioner
        Runs commands on the remote resource (e.g., an EC2 instance) after it's created.

        🔧 Example:
        ✅ Use Cases:
        Installing software
        Running configuration scripts
        Bootstrapping servers
        
📁 3. file Provisioner
        Uploads files from your local machine to the remote resource.

        🔧 Example:
        ✅ Use Cases:
        Uploading config files
        Copying scripts or binaries
        Transferring certificates or secrets (carefully)