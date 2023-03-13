from asyncio import get_event_loop
from discord import Object

"""
sync_tree docstring
"""


async def on_connect(self):
    """
    sync_tree docstring
    """
    self.logger.info("Connected")


async def on_disconnect(self):
    """
    sync_tree docstring
    """
    self.logger.info("Disconnected")


async def on_ready(self):
    """
    sync_tree docstring
    """

    if not self.ready:
        self.ready = True
        self.stdout = self.get_channel(810599224718262304)
        self.guild = self.get_guild(716803899440234506)
        self.guild_snowflake = Object(716803899440234506)
        self.setup_paramiko()
        await self.load_wg_hermes_keys()
        self.db_ready_future = self.ready_database()
        await self.db_ready_future
        self.tree.add_command(self.wireguard_command_group)
        await self.sync_tree()
        self.logger.info("Hermes ready")
        # await self.change_presence(activity=self.presence_on())

    else:
        self.logger.info("Reconnected")


async def on_message(self, message):
    """
    sync_tree docstring
    """
    if (
        not message.author.bot
    ):  # and message.author == self.get_user(309723713857650688)
        await self.process_commands(message)


#            await message.interaction.response.send_modal(WireguardModal())


async def on_error(self, err, *args, **kwargs):
    """
    sync_tree docstring
    """

    if err == "on_command_error":
        self.logger.debug("on_command_error Something went wrong.")
    else:
        raise err.original


async def on_command_error(self, context, exception):
    """
    sync_tree docstring
    """

    if isinstance(exception, CommandNotFound):
        pass
    elif hassattr(exception, "original"):
        self.logger.debug(exception.original)
        raise exception.original
    else:
        self.logger.debug(exception)
        raise exception
