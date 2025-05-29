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


