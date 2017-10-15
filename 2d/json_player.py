
import json
import main_state

Boy = main_state.Boy()

def create_team():


    player_state_table = {
        "LEFT_RUN" : Boy.LEFT_RUN,
        "RIGHT_RUN": Boy.RIGHT_RUN,
        "LEFT_STAND": Boy.LEFT_STAND,
        "LEFT_STAND": Boy.RIGHT_STAND

    }
    #team_data = json.loads(team_data_text)

    team_data_file = open('team_data.txt', 'r')
    team_data = json.load(team_data_file)
    team_data_file.close()

    team = []
    for name in team_data:
        player = Boy()
        player.name = name
        player.x = team_data[name]['x']
        player.y = team_data[name]['y']
        player.state = player_state_table[team_data[name]['StartState']]
        team.append(player)
    return team
