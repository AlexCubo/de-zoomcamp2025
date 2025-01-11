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

resource "google_storage_bucket" "dezc2025-bucket" {
  name          = "dezc2025-bucket_prj639804374698"
  location      = "EU"
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
  dataset_id                  = "dezc2025_bq_dataset"

}
