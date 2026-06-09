terraform {
    backend "s3" {
        bucket = "zerohunger-terraform-state-dev"
        key = "dev"
        region = "us-eat-1"
        use_lockfile = true
    }
}