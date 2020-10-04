variable "digitalocean_token" {}

variable "pub_key" {
  type = string
  default = "ssh_key/droplet.pub"
}
variable "pvt_key" {
  type = string
  default = "ssh_key/droplet"
}

# username for new vm user
variable "username" {
  type = string
  default = "ubuntu"
}
