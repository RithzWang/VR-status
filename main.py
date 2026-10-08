import discord
import os

# Grab the token from Railway's environment variables
TOKEN = os.environ.get("TOKEN")

class VRClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print(f"Successfully logged in as {self.user.name}!")
        print("VR Status is now active.")

# This is the crucial part that spoofs the Meta Quest (VR) device
class VROptions:
    def __init__(self):
        self.os = "linux"
        self.browser = "Discord Client"
        self.device = "Oculus"

# Apply the custom spoofed identity to the gateway connection
discord.gateway.DiscordWebSocket.IDENTIFY_OS = VROptions().os
discord.gateway.DiscordWebSocket.IDENTIFY_BROWSER = VROptions().browser
discord.gateway.DiscordWebSocket.IDENTIFY_DEVICE = VROptions().device

client = VRClient()

if __name__ == "__main__":
    if not TOKEN:
        print("Error: No TOKEN environment variable found.")
    else:
        client.run(TOKEN)
