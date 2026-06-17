resource "aws_instance" "ec2" {
  ami           = "ami-0152204c1a187337c"
  instance_type = "t2.micro"
  iam_instance_profile = var.ec2_instance_profile_name

  tags = {
    Name = "docker-instance",
    env = "dev"
  }
}