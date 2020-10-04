terraform {
  required_providers {
    digitalocean = {
      source = "digitalocean/digitalocean"
      version = "~> 1.22.2"
    }
    null = {
      source = "hashicorp/null"
      version = "~> 2.1.2"
    }
    random = {
      source = "hashicorp/random"
      version = "~> 2.3.0"
    }
  }
  required_version = ">= 0.13"
}
