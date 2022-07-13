from display import Display
from computer import Computer
from guesser import Guesser
from instance import Instance

computer_win = 1
human_win = 1
Computer_total = 0
Human_total = 0

class Director():
        #The director moves the decisions of (p, r, s) from the human and the computer 
        #to other classes or to the display (where things are displayed in the terminal)

    def __init__ (self):
        """Constructs a new Director using the specified video service.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """

        display = Display()

    def close_window(self):
        #completes the game and displays the final result and then ends the session
        while Director.update_score(self) < 3: 
            return Director.start_game(self)
        if Director.update_score(Computer_total) > 2:
            winner = Computer_total 
            print('Winner of Best_of_3 is Computer')
            return

        elif Director.update_score(Human_total) > 2:
            winner = Human_total
            print('Winner of Best_of_3 is Human')
            return
            
        elif (Director.update_score(Computer_total),Director.update(Human_total)):
            winner = (2,1)
            print('Winner of Best_of_3 is Computer')
            return
            
        elif (Director.update_score(Human_total),Director.update(Computer_total)):
            winner = (2,1)
            print('Winner of Best_of_3 is Human')
            return
        exit()

    def start_game(self):
        #where Director initiates the game by asking what choice is desired from the human player
        instance = Instance()
        print(instance.message)
        instance.Best_of_3()
        instance.final_result()



