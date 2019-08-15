import discord
from discord.ext import commands

import statics.STATICS as STATICS

client = commands.Bot(command_prefix=STATICS.Prefix)
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Spielt !help"))
    print ("Bot is ready")

@client.event
async def on_member_join(member):
    channel = member.guild.get_channel(611144070068305936)
    embed= discord.Embed (description=f"{member.mention}\nWillkommen bei DBS", title="=====DBS=====", colour=discord.Colour.dark_gold())

    avatar = member.avatar_url_as(size=512)
    embed.set_thumbnail(url=avatar)

    embed.add_field(name="========================================", value=f"Ließ bitte die Regeln bei <#611151973873614848>, \ndamit du dich ordentlich benimmst")


    await channel.send(embed=embed)
    role=member.guild.get_role(611144367742124032)
    await member.add_roles(role)


@client.command()
async def clear(ctx, amount=15):
    liste = [611144116738457600, 611198940561276939]
    if any(role.id in liste for role in ctx.message.author.roles):
        await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    liste = [611144116738457600, 611198940561276939]
    if any(role.id in liste for role in ctx.message.author.roles):
        await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    liste = [611144116738457600, 611198940561276939]
    if any(role.id in liste for role in ctx.message.author.roles):
        await member.ban(reason=reason)
        await ctx.send(f"Banned from the Server")

@client.command()
async def unban(ctx, *, member):
    liste = [611144116738457600, 611198940561276939]
    if any(role.id in liste for role in ctx.message.author.roles):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
    else:
        return

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.mention}")
            return

@client.command()
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        colour = discord.Colour.gold()
    )

    embed.set_author(name="===Help===")
    embed.add_field(name="!clear", value="Cleares the chat (nur für Supporter oder höher)", inline=False)
    embed.add_field(name="!partner", value="Zeigt dir an wie man eine Partnerschaft bekommt", inline=False)
    embed.add_field(name="!ban", value="bans the member from the server (nur für Supporter oder höher)", inline=False)
    embed.add_field(name="!kick", value="kicks you from the server (nur für Supporter oder höher)", inline=False)


    await ctx.send(author, embed=embed)

@client.command()
async def partner(ctx):
    author = ctx.message.author
    embed=discord.Embed(description="Um eine Partnerschaft mit dem Discord zu haben,\n schreibe dazu bitte cNite an", title="===HowtoPartner===", colour=discord.Colour.dark_green())

    await ctx.send(author, embed=embed)


client.run(STATICS.Token)
