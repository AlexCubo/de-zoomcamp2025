variable "project" {
  description = "Project"
  default     = "de-zoomcamp2025"
}

variable "region" {
  description = "Region"
  default     = "europe-west1"
}

variable "location" {
  description = "Project Location"
  default     = "EU"
}

variable "bq_dataset_name" {
  description = " BigQuery dataset"
  default     = "dezc2025_bq_dataset"
}

variable "gcs_storage class" {
  description = "Class of the gc storage bucket"
  default     = "STANDARD"
}

variable "gcs_bucket_name" {
  description = "Name of the bucket for the de zoomcamp course"
  default     = "dezc2025-bucket_prj639804374698"
}