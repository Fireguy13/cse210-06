class Display:
    def __init__(self,rock,paper,scissors):
        self.rock=rock#["  ___  ","/     \ ",'\     /',' \ _ /',]
        self.paper=paper#["    _______","   /      /,","  /      //"," /______//","(______(/"]
        self.scissors=scissors#["0   0","  X   "," / \ "]
        self.message="Welcome to Rock Paper Scissors, The rules are simple:\n\nSelect one of three options, rock (r), paper (p) or scissors (s) at the start of the game.\nRock beats scissors, paper beats rock, and scissors beats paper\nIf you win more matches than the computer, You win"
    
    def start_game(self):
        print()
        print(self.message)
        print()

    # def return_guesser(self,guess):
    #     return guess

    def print_guess(self,guess):
        if guess=="r" :
            for i in self.rock:
                print(i)      
        elif guess== "p":
            for i in self.paper:
                print(i)              
        elif guess=="s" :
            for i in self.scissors:
                print(i) 
        print()     
