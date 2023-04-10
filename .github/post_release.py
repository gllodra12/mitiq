import asyncio
import discord
import os

TOKEN = os.environ["DISCORD_TOKEN"]
CHANNEL_ID = 870214750368321546 # Write Mitiq channel_id

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    with open("./VERSION.txt", "r") as file:
        version = file.readline()

    if not "dev" in version:
        channel = client.get_channel(CHANNEL_ID) 
        message = f"Check out Mitiq new release at: https://github.com/unitaryfund/mitiq/releases/tag/v{version}"
        await channel.send(message)


async def disconnect_after_delay(delay):
    await asyncio.sleep(delay)
    await client.close()


async def run_bot():
    async with client:
        client.loop.create_task(disconnect_after_delay(60)) # Disconnect after 60 seconds

        await client.start(TOKEN) 


if __name__ == "__main__":
    asyncio.run(run_bot())