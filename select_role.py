import nextcord
import sys
sys.path.insert(1, "C:\\Users\\posei\\OneDrive\\Документы\\BOT")
from config import roles
from config import custom_id

VIEW_NAME = "Select"

class SelectSTRP(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    options=[
            nextcord.SelectOption(label="SanTrope RolePlay #01", emoji="<:STRP_01:1042748610787414056>", description="Сервер с большим количеством возможностей для Вас.", value=custom_id(VIEW_NAME, roles['1'])),
            nextcord.SelectOption(label="SanTrope RolePlay #02", emoji="<:STRP_02:1042749361924341760>", description="Сервер с пушечными захватами территорий.", value=custom_id(VIEW_NAME, roles['2'])),
            nextcord.SelectOption(label="SanTrope RolePlay #03", emoji="<:STRP_03:1042749739130703872>", description="Сервер с интересными мероприятиями.", value=custom_id(VIEW_NAME, roles['3'])),
            nextcord.SelectOption(label="SanTrope RolePlay #04", emoji="<:STRP_04:1042749877479809026>", description="Сервер с лучшими войнами за бизнесы.", value=custom_id(VIEW_NAME, roles['4'])),
            nextcord.SelectOption(label="SanTrope RolePlay #05", emoji="<:STRP_05:1042750131637862411>", description="Сервер с лучшим уровнем ролевой игры.", value=custom_id(VIEW_NAME, roles['5'])),
            nextcord.SelectOption(label="SanTrope RolePlay #06", emoji="<:STRP_06:1042750481639931956>", description="Сервер с комфортными условиями для игры.", value=custom_id(VIEW_NAME, roles['6'])),
            ]
    @nextcord.ui.select(custom_id=custom_id(VIEW_NAME, roles['faq']), placeholder="Список доступных серверов", max_values=1, min_values=1, options=options)
    async def callback(self, select, interaction):
        for i in range(1, 7):
            role_id = int(roles[f'{str(i)}'])
            role = interaction.guild.get_role(role_id)
            assert isinstance(role, nextcord.Role)
            if role in interaction.user.roles:
                await interaction.user.remove_roles(role)
        role_id = int(select.values[0].split(":")[-1])
        role = interaction.guild.get_role(role_id)
        assert isinstance(role, nextcord.Role)
        await interaction.user.add_roles(role)
        await interaction.response.send_message(content=f"**Роль - `{role.name}` была успешно выдана!**\n**Если этого не произошло обратитесь в канал <#892018963591102504>.**", ephemeral=True)
