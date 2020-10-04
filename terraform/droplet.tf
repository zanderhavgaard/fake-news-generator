resource "digitalocean_droplet" "droplet" {
  image = "ubuntu-20-04-x64"
  name = "droplet"
  region = "fra1"
  size = "s-1vcpu-1gb"
  private_networking = true
  # ssh_keys = [var.pub_key_fingerprint]
  ssh_keys = [digitalocean_ssh_key.droplet-key.fingerprint]
}

resource "random_password" "password" {
  length = 50
}

resource "digitalocean_ssh_key" "droplet-key" {
  name = "next-gen-news"
  public_key = file(var.pub_key)
}

resource "null_resource" "root-provisioner" {
  connection {
    user = "root"
    host = digitalocean_droplet.droplet.ipv4_address
    type = "ssh"
    private_key = file(var.pvt_key)
    timeout = "2m"
  }

  provisioner "remote-exec" {
    inline = [
      # wait for cloud-init to finish
      "while [ ! -f /var/lib/cloud/instance/boot-finished ]; do echo 'Waiting for cloud-init...'; sleep 1; done",

      # configure firewall
      "ufw default deny incoming",
      "ufw default allow outgoing",
      "ufw allow ssh",
      "ufw allow 80",
      "ufw allow 443",
      "ufw --force enable",
      "systemctl enable ufw",

      # install stuff
      "apt-get update -q",
      "apt-get upgrade -qq",
      "apt-get install -qq neovim git docker-compose",

      # enbale docker
      "systemctl enbale --now docker",
      "sudo usermod -aG docker ubuntu",

      # setup non root user
      "useradd --create-home --shell /bin/bash --groups docker ${var.username}",
      "echo \"${var.username}:${random_password.password.result}\" | chpasswd",
      "mkdir /home/ubuntu/.ssh",
      "cp /root/.ssh/* /home/ubuntu/.ssh/",
      # uncomment to disallow root access
      # "rm -rf /root/.ssh",

      # clone repository
      "git clone --quiet https://github.com/zanderhavgaard/fake-news-generator /home/ubuntu/fake-news-generator",

      # pull docker image
      "docker pull zanderhavgaard/fake-news-generator",

      # make sure ubuntu owns all of it's stuff...
      "chown -R \"ubuntu:ubuntu\" /home/ubuntu",

      "echo ===========================",
      "echo = Done setting up  server =",
      "echo ===========================",
    ]
  }
}
