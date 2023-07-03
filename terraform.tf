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
  project     = var.project_id
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

variable "project_id" {
  default = ""
}

variable "region_prj" {
  default = "us-central1"
}

variable "zone_prj" {
  default = "us-central1-a"
}
