
---

# 📄 FILE 2 — `SERVER_LIVE_COMMANDS.md`

```markdown
# Production Server Commands
Server: Ubuntu
Port: 4999
User: devakshay

---

## 🔐 SSH Configuration

Edit SSH config:

```bash
sudo nano /etc/ssh/sshd_config




Ensure:

Port 4999
PasswordAuthentication no
PermitRootLogin no

Restart:

sudo systemctl restart ssh
👤 Create New User
sudo adduser rahul
sudo usermod -aG sudo rahul
🔑 Add SSH Public Key

Switch to user:

su - rahul

Create SSH folder:

mkdir ~/.ssh
chmod 700 ~/.ssh

Add public key:

nano ~/.ssh/authorized_keys

Fix permissions:

chmod 600 ~/.ssh/authorized_keys
🛡 Firewall (UFW)

Check status:

sudo ufw status numbered

Allow SSH port:

sudo ufw allow 4999/tcp

Delete rule example:

sudo ufw delete <rule_number>
📊 Check Tunnel Status
sudo systemctl status cloudflared
journalctl -u cloudflared -n 50
📈 Resource Monitoring

CPU & Memory:

htop

Disk:

df -h

Network:

ip a
🔁 Restart Services

SSH:

sudo systemctl restart ssh

Tunnel:

sudo systemctl restart cloudflared

Production Rules:

✔ No password login
✔ Only SSH keys
✔ Each dev has separate Linux user
✔ Each dev has separate public key
✔ Access controlled via Cloudflare policy
✔ No router port forwarding