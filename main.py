import discord
from discord.ext import commands
from discord import app_commands
import smtplib
from email.mime.text import MIMEText

# ================= CONFIG =================
TOKEN = "YOUR_BOT_TOKEN_HERE"  # put your bot token here
EMAIL_ADDRESS = "your_email@gmail.com"  # Gmail sender
EMAIL_PASSWORD = "your_app_password_here"  # Gmail app password
# ==========================================

intents = discord.Intents.default()
intents.message_content = False  # no need for message content
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"🔗 Synced {len(synced)} commands globally")
    except Exception as e:
        print(f"❌ Sync failed: {e}")

@bot.tree.command(name="sendemail", description="Send an email")
@app_commands.describe(to="Recipient email", subject="Email subject", message="Email body")
async def sendemail(interaction: discord.Interaction, to: str, subject: str, message: str):
    # Construct email
    msg = MIMEText(f"Sent by: {interaction.user} ({interaction.user.id})\n\n{message}")
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to

    try:
        # Send email using Gmail SMTP
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, to, msg.as_string())

        # Confirmation ONLY in DMs
        try:
            await interaction.user.send(f"📧 Your email to `{to}` was sent successfully!")
        except discord.Forbidden:
            await interaction.response.send_message("⚠️ I couldn’t DM you. Please enable DMs.", ephemeral=True)

    except Exception as e:
        try:
            await interaction.user.send(f"❌ Failed to send email. Error: `{e}`")
        except discord.Forbidden:
            await interaction.response.send_message(f"❌ Failed to send email. Error: `{e}`", ephemeral=True)

bot.run(TOKEN)
