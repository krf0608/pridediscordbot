import discord
import random
from discord.ext import commands


client = commands.Bot(command_prefix = '/')
#client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity = discord.Game('/help'))
    print('Bot is Online')






@client.command()
async def ping(ctx):
    await ctx.send(f'Ping {round(client.latency * 1000)}ms')


@client.command()
@commands.has_permissions(manage_messages = True)
async def purge(ctx, amount = 5):
    await ctx.channel.purge(limit = amount)


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)
    await ctx.send(f'{member.mention} has been kicked')


@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f'{member.mention} has been banned')



@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} has been unbanned')
            return


@client.command(aliases = ['8ball', '8Ball', 'Eightball'])
async def eightBall(ctx, *, question):
    responses = ['As I see it, yes.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 'Don’t count on it.',
                 'It is certain.',
                 'It is decidedly so.',
                 'Most likely.',
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Outlook good.',
                 'Reply hazy, try again.',
                 'Signs point to yes.',
                 'Very doubtful.',
                 'Without a doubt.',
                 'Yes.',
                 'Yes – definitely.',
                 'You may rely on it.',
                 'Nope',
                 'Boring question ask another.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


client.run('NzUxMDA2MTEzNjA3OTc0OTEz.X1Cy8g.dlCWJeXGw8WJu4XZ0wpOZZ1TmaA')
#NzU1Nzk2NjQ5MDcwMDM1MDA1.X2Igew.CxLRTiQmOU2SBc0skiy79n9VF6c
#NzUxMDA2MTEzNjA3OTc0OTEz.X1Cy8g.dlCWJeXGw8WJu4XZ0wpOZZ1TmaA
