# Deep_Cast
DeepCast is a program that simulates phisihing attacks and monitors the vulnerability of the victims and the success rate of phishing emails

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
