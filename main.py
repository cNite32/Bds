import discord
from discord.ext import commands
import datetime
import statics.STATICS as STATICS

client = commands.Bot(command_prefix=STATICS.Prefix)
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("!help"))
    print ("Bot is ready")

@client.event
async def on_member_join(member):
    channel = member.guild.get_channel(611144070068305936)
    embed= discord.Embed (description=f"{member.mention}\nWillkommen bei DBS", title="=====DBS=====", colour=discord.Colour.dark_gold())

    avatar = member.avatar_url_as(size=512)
    embed.set_thumbnail(url=avatar)
    embed.add_field(name="========================================", value=f"Ließ bitte die Regeln bei <#611151973873614848>, \ndamit du dich ordentlich benimmst")
    embed.timestamp = datetime.datetime.utcnow()
    await channel.send(embed=embed)



@client.command()
async def buy(ctx):
    emoji = client.get_emoji(id=612233705041166367)


    embed = discord.Embed(color=discord.Color.dark_blue(), description="**Discord Bot Bestellung**")
    embed.timestamp = datetime.datetime.utcnow()
    embed.add_field(name="Bestellung", value="Die Bestellung geht sehr schnell und ist nicht wirklich kompliziert! \nMan reagiert einfach nur mit dem :buy: Emote auf diese Nachricht, danach wird man von mir angeschrieben. \nDort geht dann die eigentliche Bestellung los!")

    await ctx.send(embed=embed)
    await ctx.message.add_reaction(emoji)

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 612243130883768331:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
        if payload.emoji.name == "buy":
            print("Detected reaction")

            embed = discord.Embed(color=discord.Color.blue(), description="**Discord Service Bot**")
            embed.timestamp = datetime.datetime.utcnow()
            embed.add_field(name="Warenkorb", value=f"Schreibe bitte hier in den Chat, was der Bot, den du kaufen möchtest, haben soll. \nVerfügbar: \n- Custom Welcome Message \n- Custom Help Command \n- Fun Commands \n- Bewerbungssystem \n- MusikBot \n- Support ")

            await member.send(embed=embed)


            msg = await client.wait_for("message", timeout=None, check=lambda message: message.author == member)

            embed2 = discord.Embed(color=discord.Color.green(), description="**Discord Service Bot**")
            embed2.timestamp = datetime.datetime.utcnow()
            embed2.add_field(name="Bestellen?", value="Wenn sie wollen das ihre Bestellung bei uns eingeht, schreiben sie 'Ja' in den Chat, wenn nicht dann 'Nein'.")

            await member.send(embed=embed2)

            msg2 = await client.wait_for("message", timeout=None, check=lambda message: message.author == member)

            if msg2.content == "Ja":

                embed3 = discord.Embed(color=discord.Color.orange(), description="**Discord Service Bot**")
                embed3.timestamp = datetime.datetime.utcnow()
                embed3.add_field(name="Danke für ihre Bestellung", value="Danke das sie bei uns bestellt haben.")

                await member.send(embed=embed3)

                embed5 = discord.Embed(color=discord.Color.purple(), description=f"**Bestellung** - {member.mention}")
                embed5.timestamp = datetime.datetime.utcnow()
                embed5.add_field(name="Funktionen:", value=msg.content)


                await client.get_guild(611144070068305932).get_channel(612236313328091162).send(embed=embed5)

            else:
                embed4 = discord.Embed(color=discord.Color.red(), description="**Discord Service Bot**")
                embed4.timestamp = datetime.datetime.utcnow()
                embed4.add_field(name="Bestellung abgebrochen", value="Ihre Bestellung wurde erfolgreich abgebrochen!")

                await member.send(embed=embed4)

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


    embed.set_footer(text="Made by cNite", icon_url="https://media.discordapp.net/attachments/603921998313291786/611301931763367947/PicsArt_08-14-10.55.11.jpg?width=429&height=451")
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(author, embed=embed)


client.run(STATICS.Token)
