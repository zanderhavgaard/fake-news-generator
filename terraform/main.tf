provider "digitalocean" {
  token = var.digitalocean_token
  # version = "~> 1.14"
}

provider "null" {
  # version = "~> 2.1"
}

provider "random" {
  # version = "~> 2.2"
}
