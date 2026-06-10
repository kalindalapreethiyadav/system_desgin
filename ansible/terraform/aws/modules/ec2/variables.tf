########################################
#Developer: Preethi
# Terraform POc's
########################################


variable "prefix" {
   description = "The prefix of the enviornment"
   type = string
   default = "preek"
}

variable "env" {
    description = "The environment type"
    type = string
    default = "dev"
}

variable "security_group_id" {
    description = "The environment type"
    type = list[string]
    default = "dev"
}