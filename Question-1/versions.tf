terraform {
  required_version = "1.4.6"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.50.0"
    }
  }

  backend "s3" {
    bucket = "demo-kpmg-bucket"
    key    = "terraform.tfstate"
    region = "eu-west-2"
  }
}