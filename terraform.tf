variable "GCP_PROJECT_ID" {
  description = "Google Cloud Project ID"
  default     = var.GCP_PROJECT_ID != "" ? var.GCP_PROJECT_ID : var.secret_project_id
  type        = string
}

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

terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.71.0"
    }
  }
}

provider "google" {
  credentials = file("credentials.json")
  project     = var.GCP_PROJECT_ID
  region      = var.region_prj
  zone        = var.zone_prj
}

resource "google_compute_instance" "WeatherBotServer" {
  machine_type = "f1-micro"
  name         = "Weather-Bot-Server"

  network_interface {
    network = "default"
  }

  boot_disk {
    mode = "READ_WRITE"  # Замените на соответствующее значение для вашего случая
  }
}
