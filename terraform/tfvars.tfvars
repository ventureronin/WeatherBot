variable "GCP_PROJECT_ID" {}

variable "GCP_CREDENTIALS" {}

variable "region_prj" {
  description = "Region for the project"
  type        = string
  default     = "us-central1"
}

variable "zone_prj" {
  description = "Zone for the project"
  type        = string
  default     = "us-central1-a"
}