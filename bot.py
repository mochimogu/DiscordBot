import discord
import settings
from discord.ext import commands


def run():

    intents = discord.Intents.default()

    cilent = commands.Bot(command_prefix="!", intents=intents)

    @cilent.event
    async def on_ready():
    
        print("The bot is now ready for use")
        print("----------------------------")
        print(cilent.user.id)
    
    
    # @cilent.command()
    # async def botCommand(ctx):    

    #     await ctx.send("HELLO THERE MASTER");

    cilent.run(settings.DISCORD_TOKEN);
    
    
if __name__ == "__main__":
    run();