import pytest
import discord
from collections import namedtuple


class TestCharValidation:
    PlayerData = namedtuple("PlayerData", "name is_enemy result calls message")

    @pytest.mark.parametrize(
        "test_player",
        [
            PlayerData("Mario", False, True, 0, "not existing"),
            PlayerData("Mario", True, True, 0, "not existing"),
            PlayerData("Maaaaaaaarioooooo", False, False, 1, "your"),
            PlayerData("Maaaaaaaarioooooo", True, False, 1, "enemy"),
        ],
    )
    @pytest.mark.asyncio
    async def test_char_validation(self, mocker, test_player):
        mock_interaction = mocker.patch.object(discord, "Interaction", autospec=True)
        mock_interaction.response = mocker.patch.object(
            discord, "InteractionResponse", autospec=True
        )
        mock_embed = mocker.patch.object(discord, "Embed", autospec=True)

        from main import char_validation

        test_char_result = await char_validation(
            test_player.name,
            is_enemy=test_player.is_enemy,
            interaction=mock_interaction,
        )
        assert test_char_result is test_player.result
        assert mock_interaction.response.send_message.call_count == test_player.calls
        if test_player.result is False:
            mock_interaction.response.send_message.assert_called_once_with(
                embed=mocker.ANY, ephemeral=True
            )
            mock_embed.assert_called_once_with(
                title=":stop_sign: ERROR",
                description=f"Tipfehler in {test_player.message} character!",
                color=discord.Color.red(),
            )
        mocker.resetall()
