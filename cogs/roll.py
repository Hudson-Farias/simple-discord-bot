from discord.ext.commands.bot import Bot
from discord.ext.commands import Cog
from discord import Option

from discord.ext.commands import Cog, command, slash_command

from discord.ext.commands.context import Context
from discord.commands.context import ApplicationContext

from random import randint

class Roll(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot


    def _roll(self, sides: Option(int, default = 6), amount: Option(int, default = 1)):
        result = ''
        total = 0

        for dice in range(amount):
            side = randint(1, sides)
            total += side
            if amount > 1: result += f'`#{(dice + 1):02d}` {side}\n'

        result += f'\nTotal: `{total}`'

        return result


    @command(name = 'roll')
    async def roll_message(self, ctx: Context, sides: int = 6, amount: int = 1):
        msg = self._roll(sides, amount)
        await ctx.reply(msg)


    @slash_command(name = 'roll')
    async def roll_slash(self, inter: ApplicationContext, sides: Option(int, default = 6), amount: Option(int, default = 1)):
        msg = self._roll(sides, amount)
        await inter.response.send_message(msg)



def setup(bot: Bot):
    bot.add_cog(Roll(bot))
