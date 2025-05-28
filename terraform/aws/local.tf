########################################
#Developer: Preethi
# Terraform POc's
########################################

resource "local_file" "local_default" {
    filename = "./locals/records.tf"
    content = "CNAME: A"
}