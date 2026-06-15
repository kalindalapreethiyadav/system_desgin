resource "aws_instance" "zerohunger-ec2" {
    instance_type  = "t2.micro"
    ami   = "ami-0152204c1a187337c"
    tags = {
        env = "dev"
    }
}