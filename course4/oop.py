class game:
    num_players=0;
    num_matches=''
    party=0
    def __init__(self,matches,players):
        self.num_matches=matches
        self.num_players=players
    def Party(self):
        self.party+=1;
class football(game):
    teams=38
    league=10
    def goal_scored(self):
        self.Party()
        print('Parties',self.party)

foot=football(100,11)
foot.goal_scored();
print('Football Info-\n Number of matches:{0}\tPlayers:{1}'.format(foot.num_matches,foot.num_players))
