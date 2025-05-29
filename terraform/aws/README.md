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

