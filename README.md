# Deep_Cast
DeepCast is a program that simulates phisihing attacks and monitors the vulnerability of the targets and the success rate of phishing emails.

<br>
<br>

# Getting started

Prerequisites:
- Linux based OS
- Latest version of Python
- [Pipx (recommended)](#installing-pipx-on-linux)


Installing Deep Cast:
Once all prerequisites have been met to install Deep Cast go to your terminal and run the
following commands:

```bash
pipx install git+https://github.com/Imaad-Daniels2903/Deep_Cast
pipx ensurepath
```

Once all dependencies are downloaded and install is complete just run deep_cast to start application

```bash
deep_cast
```

<br>
<br>


# Setup Wizard
Once application is run you will be walked through the setup wizard and will required to setup:
- [App Password](#gmail-app-password-setup-guide)
- [API url](#sendgrid-api-setup-guide)

Once complete you will have all you need to use the application. Happy Phishing!!


<br>
<br>

# Installing pipx on Linux

Quick links:

- [Ubuntu / Debian](#ubuntu--debian)
- [Fedora](#fedora)
- [Arch / Manjaro](#arch--manjaro)
- [openSUSE](#opensuse)
- [Other distributions (via pip)](#other-distributions-via-pip)
- [Verifying the install](#verifying-the-install)
- [Troubleshooting](#troubleshooting)

---

## Ubuntu / Debian

Ubuntu 23.04+ and Debian 12+ ship `pipx` in the official repos:

```bash
sudo apt update
sudo apt install pipx
pipx ensurepath
```

Older Ubuntu/Debian releases may not have `pipx` packaged — use the [pip method](#other-distributions-via-pip) below instead.

---

## Fedora

Fedora ships `pipx` in the official repos:

```bash
sudo dnf install pipx
pipx ensurepath
```

Optional — allow pipx actions in global scope (installs for all users):

```bash
sudo pipx ensurepath --global
```

---

## Arch / Manjaro

Available in the official Arch repos:

```bash
sudo pacman -S python-pipx
pipx ensurepath
```

---

## openSUSE

```bash
sudo zypper install python3-pipx
pipx ensurepath
```

---

## Other distributions (via pip)

If your distro doesn't package `pipx`, install it with `pip`:

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

> **Note:** Distributions that follow [PEP 668](https://peps.python.org/pep-0668/) (Ubuntu 23.04+, Debian 12+, Fedora 38+) mark the system Python as "externally managed," so `pip install --user` will fail with an `externally-managed-environment` error on those systems. Use the distro package manager instead (`apt install pipx`, `dnf install pipx`, etc.).
>
> If no distro package exists and you hit this error, install pipx into its own isolated virtual environment instead:
>
> ```bash
> python3 -m venv ~/.local/share/pipx-venv
> ~/.local/share/pipx-venv/bin/pip install pipx
> ln -s ~/.local/share/pipx-venv/bin/pipx ~/.local/bin/pipx
> pipx ensurepath
> ```

---

## Verifying the install

After installing and running `pipx ensurepath`, **restart your terminal** (or `source ~/.bashrc` / `source ~/.zshrc`), then confirm:

```bash
pipx --version
```

---

## Troubleshooting

**`pipx: command not found` after install**
`pipx ensurepath` updates your shell config file, but it only takes effect in *new* terminal sessions. Restart the terminal or manually re-source your shell config.

**Installed tool's command not found (e.g. `myproject: command not found`)**
pipx exposes installed app commands on `PATH` via `~/.local/bin`. Confirm that directory is on your `PATH`:

```bash
echo $PATH
```

If it's missing, re-run `pipx ensurepath` and restart your terminal.

**`externally-managed-environment` error**
See the note under [Other distributions (via pip)](#other-distributions-via-pip) — use your distro's package manager, or install pipx into its own virtual environment.

<br>
<br>


# Gmail App Password Setup Guide
 
## Prerequisites
- A Google account
- 2-Factor Authentication (2FA) must be enabled
---
 
## Steps
 
### 1. Enable 2-Factor Authentication
Go to [myaccount.google.com](https://myaccount.google.com) → **Security** → **2-Step Verification**.
If it's not already on, enable it — App Passwords won't appear in your account until 2FA is active.
 
---
 
### 2. Go to App Passwords
Go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords) — or search **"App Passwords"** in the Google Account search bar.
You must be logged in to the account you want to send from.
 
---
 
### 3. Create a New App Password
Click **"Create"** (or the dropdown if on an older UI).
Give it a name like `Python Email Script` so you can identify it later.
The name doesn't affect anything — it's just a label for your reference.
 
---
 
### 4. Copy the Generated Password
Google generates a 16-character password in the format:
```
xxxx xxxx xxxx xxxx
```
Copy it immediately — you won't be able to see it again after closing the dialog.
If you lose it, just delete it and generate a new one.

<br>
<br>

# SendGrid API Setup Guide
 
## Prerequisites
- A SendGrid account (free at [sendgrid.com](https://sendgrid.com))
- Python installed
- `sendgrid` library installed (`pip install sendgrid`)
---
 
## Steps
 
### 1. Create a SendGrid Account
Go to [sendgrid.com](https://sendgrid.com) and sign up for a free account.
The free tier allows **100 emails/day** at no cost.
 
---
 
### 2. Generate an API Key
1. Log in to your SendGrid dashboard
2. Go to **Settings** → **API Keys**
3. Click **"Create API Key"**
4. Give it a name e.g. `Python Email Script`
5. Select **"Restricted Access"** and enable **Mail Send** permissions
6. Click **"Create & View"**
7. Copy the key immediately — you won't be able to see it again
Your API key will look like this:
```
SG.xxxxxxxxxxxxxxxxxxxxxxxx.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
 
---
 
### 3. Verify a Sender
SendGrid requires you to verify who you're sending from before you can send emails.
You have two options:
 
#### Option A: Single Sender Verification (quickest)
1. Go to **Settings** → **Sender Authentication**
2. Click **"Verify a Single Sender"**
3. Fill in your sender details and click **"Create"**
4. Check your email for a verification link and click it
#### Option B: Domain Authentication (recommended for production)
1. Go to **Settings** → **Sender Authentication**
2. Click **"Authenticate Your Domain"**
3. Select your DNS provider and follow the steps
4. Add the provided SPF, DKIM and DMARC records to your domain's DNS
5. Click **"Verify"** once DNS records are saved

WTC-AUE6UK4D
