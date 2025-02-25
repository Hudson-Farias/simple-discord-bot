from discord.ext.commands.bot import Bot
from discord.ext.commands import Cog, command, slash_command, has_guild_permissions
from discord import Option, Member

from discord.ext.commands.context import Context
from discord.commands.context import ApplicationContext
class Rename(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot


    @command(name = 'rename')
    @has_guild_permissions(change_nickname = True)
    async def rename_message(self, ctx: Context, member: Member, nick: str = None):
        await member.edit(nick = nick)
        await ctx.reply(f'{member.mention} name changed')


    @slash_command(name = 'rename')
    @has_guild_permissions(change_nickname = True)
    async def rename_slash(self, inter: ApplicationContext, member: Member, nick: Option(str, default = None)):
        await member.edit(nick = nick)
        await inter.response.send_message(f'{member.mention} name changed')


def setup(bot: Bot):
    bot.add_cog(Rename(bot))
