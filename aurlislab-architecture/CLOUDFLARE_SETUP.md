# Cloudflare Zero Trust + SSH Tunnel Setup
Project: aulab.in
Environment: Home Production Server

---

## 1️⃣ Domain Setup

1. Buy domain (aulab.in) from GoDaddy
2. Add domain to Cloudflare
3. Change nameservers in GoDaddy → Cloudflare nameservers
4. Wait until Cloudflare shows **Active**

---

## 2️⃣ Install Cloudflared on Server

```bash
curl -fsSL https://pkg.cloudflare.com/install.sh | sudo bash
sudo apt install cloudflared



Login tunnel:

cloudflared tunnel login

Create tunnel:

cloudflared tunnel create auralislabs
3️⃣ Configure Tunnel

Zero Trust → Access → Applications → Add Application → Self-hosted

Application domain:
ssh.aulab.in

Session type:
SSH

Policy:
Allow → Emails → add developer emails

5️⃣ Enable Authentication

Zero Trust → Access control → Access settings → manage -> add policies and login methods
Application --> set sub domain --> domain --> browser rendering to SSH

Enable:
✔ One-time PIN
OR
✔ Google login (recommended)





6️⃣ SSH Client Config (Mac)

Edit:

nano ~/.ssh/config

Add:

Host aulab
  HostName ssh.aulab.in
  User devakshay
  ProxyCommand /opt/homebrew/bin/cloudflared access ssh --hostname %h

Connect using:

ssh aulab

Architecture:

Developer
→ Cloudflare Access
→ Cloudflare Tunnel
→ localhost:4999
→ SSH daemon