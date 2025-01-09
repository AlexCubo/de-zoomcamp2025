terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.15.0"
    }
  }
}

provider "google" {
    #credentials = "/home/alessandro/.terraform.d/keys/de-zoocamp2025_terraform-sa_key6b8a5.json"
    project = "de-zoomcamp2025"
    region  = "europe-west1"
  }
