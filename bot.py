import discord
import settings
import requests
from discord.ext import commands


def run():

    intents = discord.Intents.default()
    intents.message_content= True

    cilent = commands.Bot(command_prefix="!", intents=intents)

    @cilent.event
    async def on_ready():
    
        print("The bot is now ready for use")
        print("----------------------------")
        print(cilent.user.id)
    
    
    @cilent.command()
    async def ping(ctx):    

        await ctx.send("HELLO THERE MASTER");
    
    @cilent.command()
    async def user(ctx, input):
        await ctx.send(input)

    @cilent.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Handled Error Locally")
            
    @cilent.group()
    async def math(ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send(f"The {ctx.subcommand_passed} is not a math command")
            
    @math.command()
    async def subtraction(ctx, a : int, b : int):
        await ctx.send(a - b)
        
    @math.command()
    async def addition(ctx, a : int, b : int):
        await ctx.send(a + b)
        
    @cilent.command()
    async def getquote(ctx, categories):
        
        if isinstance(categories, commands.MissingRequiredArgument):
            await ctx.send("Here are the possible options for categories")
        else:
            
            url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(categories)
            response = requests.get(url, headers={'X-api-key' : settings.API_KEY})
            if response.status_code == requests.codes.ok:
                print(200)
                print(response.text)
                
                results = response.text[0]
                print(results)
                # await ctx.send(results['quote'])                
            else:
                print('Error')
                print(404)

    cilent.run(settings.DISCORD_TOKEN);
    
    
if __name__ == "__main__":
    run();