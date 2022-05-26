import random


class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ''

    def choose(self):
        if self.name == 'AI':
            self.choice = random.choice(['rock', 'paper', 'scissor', 'lizard', 'spock'])
        else:
            self.choice = input(f'{self.name}, select rock, paper, scissors, lizard or spock: \n')
        print(f'{self.name} selects {self.choice}')

    def to_numerical_choice(self):
        switcher = {"rock": 0, "paper": 1, "scissor": 2, 'lizard': 3, 'spock': 4}
        return switcher[self.choice]

    def increment_point(self):
        self.points += 1


class GameRound:
    def __init__(self, p1, p2):
        self.rules = [
            [0, -1, 1, 1, -1],
            [1, 0, -1, -1, 1],
            [-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],
            [1, -1, 1, -1, 0]
        ]
        p1.choose()
        p2.choose()
        result = self.compare_choises(p1, p2)
        print(f"Round resulted in a {self.get_result_as_string(result)}")
        if result > 0:
            p1.increment_point()
        elif result < 0:
            p2.increment_point()

    def compare_choises(self, p1, p2):
        return self.rules[p1.to_numerical_choice()][p2.to_numerical_choice()]

    def award_point(self):
        print('implement')

    def get_result_as_string(self, result):
        res = {0: "draw", 1: "win", -1: "loss"}
        return res[result]


class Game:
    def __init__(self, p1, p2):
        self.end_game = False
        self.participant = Participant(p1)
        self.second_participant = Participant(p2)

    def start(self):
        while not self.end_game:
            GameRound(self.participant, self.second_participant)
            self.check_end_condition()

    def check_end_condition(self):
        answer = input('Continue game y/n:\n ')
        if answer == 'y':
            GameRound(self.participant, self.second_participant)
            self.check_end_condition()
        else:
            print(f"Game ended!\n{self.participant.name} has {self.participant.points}\n"
                  f"{self.second_participant.name} has {self.second_participant.points}")
            self.determine_winner()
            self.end_game = True

    def determine_winner(self):
        result_string = "It's a Draw"
        if self.participant.points > self.second_participant.points:
            result_string = f"Winner is {self.participant.name}"
        elif self.second_participant.points > self.participant.points:
            result_string = f"Winner is {self.second_participant.name}"
        print(result_string)


game = Game('Spock', 'Chen')
game.start()
