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