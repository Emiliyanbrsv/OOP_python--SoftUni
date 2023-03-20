from guild_project.player import Player


class Guild:

    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):

        if self.name == player.guild:
            return f"Player {player.name} is already in the guild."
        else:
            if player.guild == 'Unaffiliated':
                self.players.append(player)
                player.guild = self.name
                return f"Welcome player {player.name} to the guild {self.name}"
            else:
                return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):

        if player_name not in [x.name for x in self.players]:
            return f"Player {player_name} is not in the guild."

        for player in self.players:
            if player.name == player_name:
                player.guild = 'Unaffiliated'
                self.players.remove(player)

                return f"Player {player_name} has been removed from the guild."

    def guild_info(self):

        info = ''
        for player in self.players:
            info += player.player_info()
        result = f"Guild: {self.name}\n{info}"

        return result


# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())
