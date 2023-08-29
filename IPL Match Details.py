reverse_outcome = {"win": "loss", "loss": "win", "draw": "draw"}


def get_points(team_stats, team):
    return team_stats[team]["win"] * 3 + team_stats[team]["draw"] * 1


def print_final_result(point_list, team_stats):
    result_format = "Team: {}, Matches Played: {}, Won: {}, Lost: {}, Draw: {}, Points: {}"
    for points, team_name in point_list:
        win, loss, draw = team_stats[team_name]["win"], team_stats[team_name]["loss"], team_stats[team_name]["draw"]
        total = win + loss + draw
        print(result_format.format(team_name, total, win, loss, draw, points))


def update_match(team_stats, team, result):
    outcomes = ["win", "loss", "draw"]
    if not team_stats.get(team):
        team_stats[team] = {"win": 0, "loss": 0, "draw": 0}
    for possible_outcome in outcomes:
        if result == possible_outcome:
            team_stats[team][result] += 1
        else:
            team_stats[team][result] += 0


def store_game_results(team_stats):
    t1, t2, result = input().split(";")
    update_match(team_stats, t1, result)
    update_match(team_stats, t2, reverse_outcome[result])


def main():
    n = int(input())
    team_stats = dict()
    for i in range(n):
        store_game_results(team_stats)
    point_list = []
    for team in team_stats:
        point_list.append((get_points(team_stats, team), team))
    point_list = sorted(point_list, reverse=True)
    print_final_result(team_stats, point_list)


main()

#test case

# 6
# CSK;RR;loss
# RR;DD;draw
# MI;KKR;win
# KKR;RR;loss
# CSK;DD;draw
# MI;DD;draw