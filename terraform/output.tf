# output ip address
output "ip_address" {
  value = digitalocean_droplet.droplet.ipv4_address
}

output "static_ip" {
  value = digitalocean_floating_ip.static-droplet-ip.ip_address
}
