########################################
#Developer: Preethi
# Terraform POc's
########################################

output "ec2_instance_id" {
    description = "Instance ID"
    value = aws_instance.main_default
}