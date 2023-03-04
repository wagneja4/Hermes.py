import discord
from discord.ext.commands import Cog
from discord import app_commands
from src.Modals.Wireguard import WireguardModal

class WireguardCommand(Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @Cog.listener()
    async def on_ready(self):
        pass
    
    @app_commands.command(name="wireguard_setup")
    @app_commands.guilds(discord.Object(id=716803899440234506))
    async def wg_modal(self, interaction):
        await interaction.response.send_modal(WireguardModal(self.bot))

# regenerate wg conf, fail safe for corruption
#    @app_commands.command(name="wireguard_refresh")
#    @app_commands.guilds(discord.Object(id=716803899440234506))
#    async def wg_modal(self, interaction):
#        await interaction.response.send_modal(WireguardModal())
    

async def setup(bot):
    await bot.add_cog(WireguardCommand(bot))

