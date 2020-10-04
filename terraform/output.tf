# output ip address
output "ip_address" {
  value = digitalocean_droplet.droplet.ipv4_address
}
