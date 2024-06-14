import discord
from discord.ext import commands
import json

class Register(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='register',
        description="Commande d'inscription",
    )
    async def register(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.blue()
        )
        embed.set_author(name='Inscription')
        embed.add_field(name='Réagis avec :envelope: et je t\'expliquerais tout en message privée !', value="Clique sur la réaction :envelope:", inline=False)
        embed.add_field(name='Développeur : Iyed A. (Polo 83#1234)', value="©Custom Games", inline=False)
        embed_send = await ctx.send(embed=embed)
        emojis = '✉'
        await embed_send.add_reaction(emojis)

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if self.bot.user.id == user.id:
            return
        test = discord.Embed(
            colour=discord.Colour.blue()
        )
        test.set_author(name="Inscription")
        test.add_field(name='Vous êtes incrit !', value='Vous pouvez nous soutenir via ce lien : https://github.com/iyed-dev/Fortool-CustomGames/ !', inline=False)
        test.add_field(name=":wink: J’espère que vous allez partager le système à vos amis !", value="©Custom Games", inline=False)
        if reaction.emoji == '✉':
            member = user
            var = discord.utils.get(user.guild.roles, name="✅ valid")
            await member.add_roles(var)
            with open('cogs/bdd.json') as json_file:
                data = json.load(json_file)
                x = {"username": user.name, "id": user.id}
            if x not in data:
                await user.send(embed=test)
                data.append(x)
                with open('cogs/bdd.json', 'w') as outfile:
                    json.dump(data, outfile)
            else:
                await user.send(":warning: Tu as déjà souscris à nos services")
                await member.add_roles(var)

async def setup(bot):
    await bot.add_cog(Register(bot))
