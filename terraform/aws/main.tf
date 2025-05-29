module "aws_instance" {
    source = "./modules/ec2"
}

resource "aws_s3_bucket" "telmate_bucket"
{
    bucket = "${var.prefix}_bucket_main"
    acl = "private"
}