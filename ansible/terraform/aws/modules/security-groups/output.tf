########################################
#Developer: Preethi
# Terraform POc's
########################################

output "secuirty_group_ID" {
    description = "The EC@ security group ID"
    value = module.aws_security_group.allow_tls.id
}