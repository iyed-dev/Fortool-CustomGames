import discord
from discord.ext import commands

class Roles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='setup',
        description='Commande pour créer des salons. Pour effectuer cette commande il vous faudra les permissions administrateur !'
    )
    @commands.has_permissions(administrator=True)
    async def setup(self, ctx):
        await ctx.guild.create_role(name="✅ valid")
        await ctx.channel.send('Configuration terminée ! Vous pouvez exécuter la commande "*register" pour pouvoir vous inscrire !')
        guild = ctx.guild
        setup = await guild.create_category("CUSTOM GAMES SYSTEME")
        await guild.create_text_channel("📢┆annonces", category=setup)
        await guild.create_text_channel("✅┆bot-1", category=setup)
        await guild.create_text_channel("✅┆bot-2", category=setup)

async def setup(bot):
    await bot.add_cog(Roles(bot))
