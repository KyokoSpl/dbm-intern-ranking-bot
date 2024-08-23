from typing import Optional

import discord
from discord import app_commands
import settings
import api_handlers as api
MY_GUILD = discord.Object(id=1269330178488799252)  # replace with your guild id
token = settings.TOKEN
logger = settings.logging.getLogger("bot")

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        # A CommandTree is a special type that holds all the application command
        # state required to make it work. This is a separate class because it
        # allows all the extra state to be opt-in.
        # Whenever you want to work with application commands, your tree is used
        # to store and work with them.
        # Note: When using commands.Bot instead of discord.Client, the bot will
        # maintain its own tree instead.
        self.tree = app_commands.CommandTree(self)

    # In this basic example, we just synchronize the app commands to one guild.
    # Instead of specifying a guild to every command, we copy over our global commands instead.
    # By doing so, we don't have to wait up to an hour until they are shown to the end-user.
    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


intents = discord.Intents.default()
client = MyClient(intents=intents)


@client.event
async def on_ready():
    logger.info(f'Logged in as: {client.user} (ID: {client.user.id})')




# In this example, even though we use `text_to_send` in the code, the client will use `text` instead.
# Note that other decorators will still refer to it as `text_to_send` in the code.



@client.tree.command()
@app_commands.rename(text_to_send='text')
@app_commands.describe(text_to_send='Text to send in the current channel')
async def send(interaction: discord.Interaction, text_to_send: str):
    """Sends the text into the current channel."""
    await interaction.response.send_message(text_to_send)



# To make an argument optional, you can either give it a supported default argument
# or you can mark it as Optional from the typing standard library. This example does both.





class AcceptDeclineView(discord.ui.View):
    def __init__(self, member: discord.Member, score: str, enemy: discord.Member):
        super().__init__(timeout=60)  # Die Buttons werden nach 60 Sekunden deaktiviert
        self.member = member
        self.score = score
        self.enemy = enemy
        self.accepted = None

    @discord.ui.button(label="Accept", style=discord.ButtonStyle.green)
    async def accept(self, interaction: discord.Interaction, button: discord.ui.Button):
        moderator_role_id = 1276172733700374589
        moderator_role = discord.utils.get(interaction.guild.roles, id=moderator_role_id)

        if interaction.user == self.enemy or (moderator_role and moderator_role in interaction.user.roles):
            self.accepted = True
            acceptembed = discord.Embed(
                title=":white_check_mark: ACCEPTED",
                description=f'You accepted the result!',
                color=discord.Color.green()
            )
            await interaction.response.send_message(embed=acceptembed, ephemeral=True)

            # Parse the score into wins and losses for each user
            member_score, enemy_score = map(int, self.score.split(':'))
            
            # Create the result message
            result_embed = discord.Embed(
                title=":information: MATCH RESULT",
                description=f"**{self.member.mention} won a match ({member_score}:{enemy_score}) against {self.enemy.mention}**",
                color=discord.Color.blue()
            )
            await interaction.followup.send(embed=result_embed)
            member = str(self.member)
            enemy = str(self.enemy)
            api_call_one = api.send_game_data(member, member_score, enemy_score)
            api_call_two = api.send_game_data(enemy, enemy_score, member_score)
            self.stop()
        else:
            notallowed_embed = discord.Embed(
                title=":no_entry_sign: NOT ALLOWED!",
                description="You're not allowed to do that!",
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=notallowed_embed, ephemeral=True)

    @discord.ui.button(label="Decline", style=discord.ButtonStyle.red)
    async def decline(self, interaction: discord.Interaction, button: discord.ui.Button):
        moderator_role_id = 1276172733700374589
        moderator_role = discord.utils.get(interaction.guild.roles, id=moderator_role_id)

        if interaction.user == self.enemy or (moderator_role and moderator_role in interaction.user.roles):            
            self.accepted = False

            report_embed = discord.Embed(
                title=":x: RESULT DECLINED",
                description=f'{self.enemy.mention} has declined the match result reported by {self.member.mention}. **Moderators have been notified!**',
                color=discord.Color.orange()
            )
            await interaction.response.send_message(embed=report_embed)

            self.stop()
        else:
            notallowed_embed = discord.Embed(
                title=":no_entry_sign: NOT ALLOWED!",
                description="You're not allowed to do that!",
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=notallowed_embed, ephemeral=True)


@client.tree.command()
@app_commands.describe(score='Enter the score e.g., 4:3 (First your score)', enemy='Enter the opponent')
async def result(interaction: discord.Interaction, score: str = "0", enemy: discord.Member = None):
    """Enter a result of your set"""

    member = interaction.user  # Der Benutzer, der den Befehl ausführt

    if not score.count(':') == 1 or not all(part.isdigit() for part in score.split(':')):
        scoreinvalid = discord.Embed (
            title=":stop_sign: ERROR",
            description="Invalid score format! Please use X:X where X is a number.",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=scoreinvalid, ephemeral=True)
        return

    if member == enemy:
        enemyequalsmember = discord.Embed(
            title=":stop_sign: ERROR",
            description="You cannot report a match against yourself!",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=enemyequalsmember, ephemeral=True)
        return

    view = AcceptDeclineView(member, score, enemy)
    prompt_embed = discord.Embed(
        title="Do you accept the result?",
        description=f'**{member.mention}** scored **{score}** vs **{enemy.mention}**',
        color=discord.Color.blue()
    )
    view.message = await interaction.response.send_message(f'{enemy.mention}', embed=prompt_embed, view=view)



# This context menu command only works on messages
@client.tree.context_menu(name='Report to Moderators')
async def report_message(interaction: discord.Interaction, message: discord.Message):
    # We're sending this response message with ephemeral=True, so only the command executor can see it
    await interaction.response.send_message(
        f'Thanks for reporting this message by {message.author.mention} to our moderators.', ephemeral=True
    )

    # Handle report by sending it into a log channel
    log_channel = interaction.guild.get_channel(0)  # replace with your channel id

    embed = discord.Embed(title='Reported Message')
    if message.content:
        embed.description = message.content

    embed.set_author(name=message.author.display_name, icon_url=message.author.display_avatar.url)
    embed.timestamp = message.created_at

    url_view = discord.ui.View()
    url_view.add_item(discord.ui.Button(label='Go to Message', style=discord.ButtonStyle.url, url=message.jump_url))

    await log_channel.send(embed=embed, view=url_view)


client.run(token, root_logger=True)