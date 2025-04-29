import discord
from mappings import char_map
import api_handlers as api
import settings


class AcceptDeclineView(discord.ui.View):
    def __init__(
        self,
        member: discord.Member,
        score: str,
        enemy: discord.Member,
        charp1: str,
        charp2: str,
    ):
        super().__init__(timeout=300)  # Die Buttons werden nach 5 Minuten deaktiviert
        self.member = member
        self.score = score
        self.enemy = enemy
        self.charp1 = charp1
        self.charp2 = charp2
        self.accepted = None

    @discord.ui.button(label="Accept", style=discord.ButtonStyle.green)
    async def accept(self, interaction: discord.Interaction, button: discord.ui.Button):
        moderator_role_id = MODROLE  # replace with your moderator role id
        moderator_role = discord.utils.get(
            interaction.guild.roles, id=moderator_role_id
        )

        if interaction.user == self.enemy or (
            moderator_role and moderator_role in interaction.user.roles
        ):
            self.accepted = True
            acceptembed = discord.Embed(
                title=":white_check_mark: ACCEPTED",
                description=f"You accepted the result!",
                color=discord.Color.green(),
            )
            await interaction.response.send_message(embed=acceptembed, ephemeral=True)

            # Parse the score into wins and losses for each user
            member_score, enemy_score = map(int, self.score.split(":"))

            # Create the result message
            result_embed = discord.Embed(
                title="<:LuigiGG:1066376739443454014> MATCH RESULT",
                description=f"**{self.member.mention}** scored **({member_score}:{enemy_score})** against **{self.enemy.mention}** \n **{self.member.mention}** played **{self.charp1}** and **{self.enemy.mention}** played **{self.charp2}**",
                color=discord.Color.blue(),
            )

            await interaction.followup.send(embed=result_embed)
            # Get IDs
            member = int(self.member.id)
            enemy = int(self.enemy.id)

            # Map IDs to usernames

            print(member)
            print(enemy)
            charp1_id = char_map.get(self.charp1)
            charp2_id = char_map.get(self.charp2)
            _api_call_one = api.send_game_data(
                member, charp1_id, member_score, enemy_score
            )
            _api_call_two = api.send_game_data(
                enemy, charp2_id, enemy_score, member_score
            )
            self.stop()
        else:
            notallowed_embed = discord.Embed(
                title=":no_entry_sign: NOT ALLOWED!",
                description="You're not allowed to do that!",
                color=discord.Color.red(),
            )
            await interaction.response.send_message(
                embed=notallowed_embed, ephemeral=True
            )

    @discord.ui.button(label="Decline", style=discord.ButtonStyle.red)
    async def decline(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        moderator_role_id = settings.MODROLE
        moderator_role = discord.utils.get(
            interaction.guild.roles, id=moderator_role_id
        )

        if interaction.user == self.enemy or (
            moderator_role and moderator_role in interaction.user.roles
        ):
            self.accepted = False

            report_embed = discord.Embed(
                title=":x: RESULT DECLINED",
                description=f"{self.enemy.mention} has declined the match result reported by {self.member.mention}. **Moderators have been notified!**",
                color=discord.Color.orange(),
            )
            await interaction.response.send_message(embed=report_embed)

            self.stop()
        else:
            notallowed_embed = discord.Embed(
                title=":no_entry_sign: NOT ALLOWED!",
                description="You're not allowed to do that!",
                color=discord.Color.red(),
            )
            await interaction.response.send_message(
                embed=notallowed_embed, ephemeral=True
            )
