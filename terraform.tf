# main.tf

provider "google" {
  credentials = file("<YOUR-CREDENTIALS-FILE>.json")
  project     = "<YOUR-PROJECT-ID>"
  region      = "us-central1"
}

# GKE Cluster
resource "google_container_cluster" "primary" {
  name     = "my-gke-cluster"
  location = "us-central1"

  node_pool {
    name       = "my-node-pool"
    node_count = 3

    node_config {
      preemptible  = false
      machine_type = "e2-medium"
    }
  }
}

# Cloud SQL Database Instance
resource "google_sql_database_instance" "default" {
  name     = "my-database-instance"
  region   = "us-central1"
  database_version = "POSTGRES_13"

  settings {
    tier = "db-f1-micro"
    # Additional settings to harden the database
  }

  # Set up replicas for horizontal scaling
  replica_configuration {
    # Configuration for replicas
  }
}

# Outputs for connection strings and other details
output "gke_cluster_endpoint" {
  value = google_container_cluster.primary.endpoint
}

output "gke_cluster_name" {
  value = google_container_cluster.primary.name
}

output "sql_instance_connection_name" {
  value = google_sql_database_instance.default.connection_name
}
