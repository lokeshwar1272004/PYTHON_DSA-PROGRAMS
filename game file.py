import random
class cricket:
    def game(self):
        g1 = input("do you want play any game to make you happy").lower()
        if g1 == "yes":
            cricket = int(input("""
            we have cricket game at_ 1"""))

    def cricket_game(self):
        for nu in range(1):
            print("TEAM REGISTER"
                  "EACH TEAM HAVE ONE CAP(BATSMAN) AND ONE BOWLER")
            TEAM_1 = input("TEAM NAME: ").lower()
            cap = input("TEAM CAP BATSMAN").lower()
            BOWLER = input("BOWLER NAME :").lower()
            print("*****_____REGISTER COMPLETED______****")
            print("TEAM_", nu + 1, "INFORMATION")
            TABLE = {"TEAM_NAME": TEAM_1,
                     "CAP": cap,
                     "Bowler": BOWLER}
            for i in TABLE:
                print(i, ":", TABLE[i])
            file.game_play()


    def game_play(self):
        toss = ['HEAD', 'TAIL']
        toss_input = input("HEAD,TAIL").upper()
        t = random.choice(toss)
        print(t)
        if toss_input == t:
            t_i = input("you won the toss now say bating or bowling: ")
            print(f'you say {t_i} right but I say no match was cancel due to your attitude')

        else:
            print("oops! you lose the toss go cry more and ")
            print("match is cancel due to rain 🤣")

file = cricket()
file.cricket_game()