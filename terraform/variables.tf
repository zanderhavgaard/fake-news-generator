variable "digitalocean_token" {}
variable "pub_key" {}
variable "pvt_key" {}

# username for new vm user
variable "username" {
  type = string
  default = "ubuntu"
}
