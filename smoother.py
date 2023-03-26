#A script for banning purposes for your discord bot!
#Not my script and not made by me ⚠️

import discord #Imports the discord module.
from discord.ext import commands #Imports discord extensions.

#The below code verifies the "client".
intents = discord.Intents().all()
client = commands.Bot(command_prefix='!', intents=intents)
#The below code stores the token.
token = "BOT_TOKEN!"

'''
The below code displays if you have any errors publicly. This is useful if you don't want to display them in your output shell.
'''
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all requirements 🙄.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have all the requirements 😠")

#The below code bans player.
@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, , reason = None):
    await member.ban(reason = reason)

#The below code unbans player.
@client.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx,, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

#The below code runs the bot.
client.run(token)
