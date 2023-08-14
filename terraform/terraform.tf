terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.71.0"
    }
  }
}

provider "google" {
  credentials = var.GCP_CREDENTIALS
  project     = var.GCP_PROJECT_ID
  region      = var.region_prj
  zone        = var.zone_prj
}

resource "google_compute_instance" "weatherbotserver" {
  machine_type = "f1-micro"
  name         = "weatherbotserver"


  network_interface {
    network = "default"

    access_config {
      nat_ip = "35.209.100.225"
      network_tier = "STANDART"
    }
  }

  boot_disk {
    initialize_params {
      image = "ubuntu-2204-jammy-v20230630"
    }
  }
}

output "external_ip" {
  value = google_compute_instance.weatherbotserver.network_interface.0.access_config.0.nat_ip
}