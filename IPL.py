# IPL Management System using OOP Concepts in Python

# ------------------------------
# Player Class with Encapsulation
# ------------------------------
class Player:
    def __init__(self, jn, nm, r, w, tn):
        # Private attributes using double underscore
        self.__jersey_no = jn
        self.__name = nm
        self.__runs = r
        self.__wickets = w
        self.__team_name = tn

    # ----------- Getter Methods -----------

    def get_jersey_no(self):
        return self.__jersey_no

    def get_name(self):
        return self.__name

    def get_runs(self):
        return self.__runs

    def get_wickets(self):
        return self.__wickets

    def get_team_name(self):
        return self.__team_name

    # ----------- Setter Methods -----------

    def set_jersey_no(self, jn):
        self.__jersey_no = jn

    def set_name(self, nm):
        self.__name = nm

    def set_runs(self, r):
        self.__runs = r

    def set_wickets(self, w):
        self.__wickets = w

    def set_team_name(self, tn):
        self.__team_name = tn

    # ----------- Display Player Info -----------
    def display_info(self):
        print("\n-------------------------------")
        print(f"Jersey No   : {self.__jersey_no}")
        print(f"Name        : {self.__name}")
        print(f"Team        : {self.__team_name}")
        print(f"Runs Scored : {self.__runs}")
        print(f"Wickets     : {self.__wickets}")
        print("-------------------------------")


# ------------------------------
# Creating Teams (11 Players Each)
# ------------------------------

# Team: Mumbai Indians
MumbaiIndians = []

MI1 = Player(45, "Rohit Sharma", 418, 0, "MI")
MI2 = Player(63, "Suryakumar Yadav", 717, 0, "MI")
MI3 = Player(9, "Tilak Varma", 343, 0, "MI")
MI4 = Player(19, "Hardik Pandya", 224, 14, "MI")
MI5 = Player(74, "Mitchell Santner", 40, 10, "MI")
MI6 = Player(18, "Trent Boult", 2, 22, "MI")
MI7 = Player(56, "Deepak Chahar", 37, 1, "MI")
MI8 = Player(93, "Jasprit Bumrah", 0, 18, "MI")
MI9 = Player(12, "Piyush Chawla", 9, 17, "MI")
MI10 = Player(22, "Shreyas Gopal", 65, 12, "MI")
MI11 = Player(4, "Vignesh Puthur", 0, 6, "MI")

MumbaiIndians.extend([MI1, MI2, MI3, MI4, MI5, MI6, MI7, MI8, MI9, MI10, MI11])

# Team: Royal Challengers Bangalore
RoyalChallengersBangalore = []

RCB1 = Player(18, "Virat Kohli", 657, 0, "RCB")
RCB2 = Player(28, "Faf du Plessis", 600, 0, "RCB")
RCB3 = Player(97, "Rajat Patidar", 312, 0, "RCB")
RCB4 = Player(37, "Devdutt Padikkal", 247, 0, "RCB")
RCB5 = Player(25, "Krunal Pandya", 109, 8, "RCB")
RCB6 = Player(38, "Josh Hazlewood", 0, 22, "RCB")
RCB7 = Player(15, "Bhuvneshwar Kumar", 0, 6, "RCB")
RCB8 = Player(23, "Liam Livingstone", 112, 2, "RCB")
RCB9 = Player(77, "Mohammed Siraj", 4, 13, "RCB")
RCB10 = Player(31, "Riyan Parag", 320, 1, "RCB")
RCB11 = Player(88, "Harshal Patel", 21, 17, "RCB")

RoyalChallengersBangalore.extend([RCB1, RCB2, RCB3, RCB4, RCB5, RCB6, RCB7, RCB8, RCB9, RCB10, RCB11])

# Team: Chennai Super Kings
ChennaiSuperKings = []

CSK1 = Player(22, "Shivam Dube", 357, 0, "CSK")
CSK2 = Player(8, "Ravindra Jadeja", 301, 10, "CSK")
CSK3 = Player(66, "MS Dhoni", 196, 0, "CSK")
CSK4 = Player(17, "Rachin Ravindra", 191, 0, "CSK")
CSK5 = Player(18, "Devon Conway", 156, 0, "CSK")
CSK6 = Player(14, "Sam Curran", 114, 6, "CSK")
CSK7 = Player(12, "Noor Ahmad", 7, 24, "CSK")
CSK8 = Player(55, "Matheesha Pathirana", 2, 15, "CSK")
CSK9 = Player(7, "Maheesh Theekshana", 13, 10, "CSK")
CSK10 = Player(32, "Ben Stokes", 225, 5, "CSK")
CSK11 = Player(10, "Mukesh Choudhary", 0, 11, "CSK")

ChennaiSuperKings.extend([CSK1, CSK2, CSK3, CSK4, CSK5, CSK6, CSK7, CSK8, CSK9, CSK10, CSK11])

# Team: Gujarat Titans
GujaratTitans = []

GT1 = Player(10, "Shubman Gill", 426, 0, "GT")
GT2 = Player(77, "David Miller", 316, 0, "GT")
GT3 = Player(24, "Rahul Tewatia", 230, 4, "GT")
GT4 = Player(13, "Rashid Khan", 89, 16, "GT")
GT5 = Player(11, "Mohit Sharma", 8, 19, "GT")
GT6 = Player(15, "Alzarri Joseph", 3, 14, "GT")
GT7 = Player(29, "Sai Sudharsan", 362, 0, "GT")
GT8 = Player(99, "Abhinav Manohar", 214, 0, "GT")
GT9 = Player(50, "Wriddhiman Saha", 202, 0, "GT")
GT10 = Player(90, "Vijay Shankar", 275, 1, "GT")
GT11 = Player(8, "Yash Dayal", 5, 7, "GT")

GujaratTitans.extend([GT1, GT2, GT3, GT4, GT5, GT6, GT7, GT8, GT9, GT10, GT11])

# Combine all players from all teams
all_players = MumbaiIndians + RoyalChallengersBangalore + ChennaiSuperKings + GujaratTitans


# ------------------------------
# Function to Display Good Batsmen
# ------------------------------
def display_good_batsmen(players):
    print("\n*** Good Batsmen (Runs > 400) ***")
    found = False
    for player in players:
        if player.get_runs() > 400:
            found = True
            print(f"\nJersey No: {player.get_jersey_no()}")
            print(f"Name     : {player.get_name()}")
            print(f"Team     : {player.get_team_name()}")
            print(f"Runs     : {player.get_runs()}")
    if not found:
        print("No such player found.")

# ------------------------------
# Function to Display Good Bowlers
# ------------------------------
def display_good_bowlers(players):
    print("\n*** Good Bowlers (Wickets > 10) ***")
    found = False
    for player in players:
        if player.get_wickets() > 10:
            found = True
            print(f"\nJersey No : {player.get_jersey_no()}")
            print(f"Name      : {player.get_name()}")
            print(f"Team      : {player.get_team_name()}")
            print(f"Wickets   : {player.get_wickets()}")
    if not found:
        print("No such player found.")

# ------------------------------
# Function to Display All-Rounders
# ------------------------------
def display_all_rounders(players):
    print("\n*** All-Rounders (Runs > 200 and Wickets > 5) ***")
    found = False
    for player in players:
        if player.get_runs() > 200 and player.get_wickets() > 5:
            found = True
            player.display_info()
    if not found:
        print("No such player found.")

# ------------------------------
# Call All Functions
# ------------------------------
display_good_batsmen(all_players)
display_good_bowlers(all_players)
display_all_rounders(all_players)

# # Short version of display_good_batsmen() using filter and lambda:
# good_batsmen = list(filter(lambda p: p.get_runs() > 400, all_players))
# # This filters all players who have more than 400 runs

# # Short version of display_good_bowlers() using filter and lambda:
# good_bowlers = list(filter(lambda p: p.get_wickets() > 10, all_players))
# # This filters all players who have taken more than 10 wickets

# # Short version of display_all_rounders() using filter and lambda:
# all_rounders = list(filter(lambda p: p.get_runs() > 200 and p.get_wickets() > 5, all_players))
# # This filters all players who have both runs > 200 and wickets > 5
