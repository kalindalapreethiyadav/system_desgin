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