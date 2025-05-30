module "aws_instance" {
    source = "./modules/ec2"
}

resource "local_file" "local_default" {
    filename = "./locals/records.tf"
    content = "CNAME: A"
}

