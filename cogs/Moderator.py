import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='a!')

class Moderator:

    def __init__(self,bot):
        self.bot = bot

    @commands.has_permissions(manage_guild=True)
    @commands.command()
    async def promote(self,ctx, member: discord.Member, xrole: discord.Role):
        await member.add_roles(xrole)

    @commands.has_permissions(manage_guild=True)
    @commands.command()
    async def demote(self,ctx, member: discord.Member, xrole: discord.Role):
        await member.remove_roles(xrole)

    @commands.has_permissions(manage_guild=True)
    @commands.command()
    async def move(self,ctx,xrole: discord.Role,posx:int):
        newpos = await xrole.edit(position=posx)
        await ctx.author.send(newpos)
    
    @commands.has_permissions(kick_members=True)
    @bot.command()
    async def kick(self,ctx, member: discord.Member):
        await ctx.guild.kick(
            member
            )

        await ctx.send(
            embed = discord.Embed(
                title="Kick",
                description="{0.name} got kicked from the server".format(
                    member
                    )
                )
            )

    @commands.has_permissions(ban_members=True)
    @bot.command()
    async def ban(self,ctx, user:int):
        await ctx.guild.ban(user)


        await ctx.send(
            embed = discord.Embed(
                title="Ban",
                description=f"{user.mention} got banned from the server"
                )
            )
    
    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def unban(self,ctx,user: int):
        userid = discord.Object(user)
        await ctx.guild.unban(user=userid)


    @commands.has_permissions(manage_messages=True)
    @commands.command(brief = "deletes multiple messages at once", aliases=['prune'])
    async def purge(self,ctx, number: int = None):
        await ctx.channel.prune(limit = number + 1)
        if number == 1:
            await ctx.send(f'Deleted {number} message', delete_after=5)
        else:
            await ctx.send(f'Deleted {number} message(s)', delete_after=5)
    

def setup(bot):
    bot.add_cog(Moderator(bot))