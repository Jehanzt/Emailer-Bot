# Emailer Bot (Prototype)

This is a prototype email automation bot for Discord, built with `discord.py`.  
It allows the owner to send emails through a Discord command.

## Setup

1. **Install the required Python packages**  
   *(see `requirements.txt` for details)*  
   ```
   pip install -r requirements.txt
   ```
2. **Edit your credentials in `main.py`:**
   ```
   TOKEN = "YOUR_BOT_TOKEN_HERE"          # Your Discord bot token
   EMAIL_ADDRESS = "your_email@gmail.com"  # Gmail sender address
   EMAIL_PASSWORD = "your_app_password_here"  # Gmail app password
   ```
3. **Run the bot:**  
   ```
   python main.py
   ```

## Variables

The main variables you need to set in `main.py` are:
```
TOKEN          # Your Discord bot token
EMAIL_ADDRESS  # The Gmail address the bot will use to send emails
EMAIL_PASSWORD # The Gmail app password (not your normal password; generate one for your Gmail account)
```

## How to Use

- The bot currently supports **one command**:
  ```
  /sendemail
  ```
- **Usage:**  
  Use the `/sendemail` command in any server where the bot is present.

- **Parameters:**  
  ```
  to       # Recipient email address
  subject  # Email subject
  message  # Email body
  ```
- The bot will send a confirmation message to your Discord DMs if the email is sent successfully.
- Only the configured sender email will be used.

## Note

This code is for **testing/learning purposes only**.  
Do not plagiarize or claim this code as your own.
       ``README.md made with copilot``
