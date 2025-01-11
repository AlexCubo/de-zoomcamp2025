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
  project = var.project
  region  = var.region
}

resource "google_storage_bucket" "dezc2025-bucket" {
  name          = var.gcs_bucket_name
  location      = var.location
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

resource "google_bigquery_dataset" "dezc2025-dataset" {
  dataset_id = var.bq_dataset_name

}
