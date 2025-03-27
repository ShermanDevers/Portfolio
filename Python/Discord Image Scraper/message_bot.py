from discord.ext import commands
import discord
import config
import requests
import json
import logging


def create_channel(interaction):
    guild = interaction.guild

    return guild


def get_guild_name(guild_id):
    headers = {"authorization": config.DISCORD_API_AUTH}
    guild = requests.get(
        f"https://discord.com/api/v10/guilds/{guild_id}", headers=headers
    )
    try:
        guild_name = json.loads(guild.text)["name"]
    except KeyError:
        logging.error("Channel isn't availiable to user")

    return guild_name


def main():
    intents = discord.Intents.default()
    intents.message_content = True
    client = commands.Bot(command_prefix="/", intents=intents)
    logging.basicConfig(level=logging.INFO)

    @client.event
    async def on_ready():
        logging.info("Ready")
        await client.tree.sync()

    @client.tree.command(
        name="crawl", description="Crawl a discord channel for its images"
    )
    async def imagecrawl(interaction, channelid: str, limit: int = 100):
        headers = {"authorization": config.DISCORD_API_AUTH}
        messages = requests.get(
            f"https://discord.com/api/v10/channels/{channelid}/messages?limit={limit}",
            headers=headers,
        )
        channel = requests.get(
            f"https://discord.com/api/v10/channels/{channelid}", headers=headers
        )

        mess_json = json.loads(messages.text)
        channel_name = json.loads(channel.text)["name"]
        guild_id = json.loads(channel.text)["guild_id"]
        guild_name = get_guild_name(guild_id)

        image_amount = 0
        links = []
        for value in mess_json:
            try:
                message_attachments = value["attachments"]
                message_embeds = value["embeds"]
                message_attachments.reverse()
                for attachment in message_attachments:
                    if "https://tenor.com" in attachment["url"]:
                        continue
                    else:
                        links.append(f"{attachment['url']}")

                for embed in message_embeds:
                    try:

                        if "https://tenor.com" in embed["url"]:
                            continue
                        else:
                            links.append(f"{embed['url']}")

                    except KeyError:
                        print("Doesn't have embed")

            except IndexError:
                logging.error("Didn't have attachments and/or embeds")
            except TypeError:
                logging.info("Problem with message")
                print(mess_json)

        links = list(dict.fromkeys(links))
        links.reverse()
        guild_name = guild_name.replace("'", "")
        guild_name = guild_name.replace(" ", "-")

        new_name = f"{guild_name.lower()}_{channel_name}"
        guild = interaction.guild
        channel = discord.utils.get(guild.channels, name=new_name)
        if channel is None:
            await guild.create_text_channel(new_name)
            channel = discord.utils.get(guild.channels, name=new_name)

        await channel.send("---------Attachments---------")
        for link in links:
            await channel.send(link)
            image_amount += 1

        logging.info(
            f"{image_amount} attachments/embeds retrieved from messages in {guild_name}:{channel_name}"
        )

    client.run(config.BOT_API_TOKEN)


if __name__ == "__main__":
    main()
