from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 22, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.file = "a"
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        # int(self.file)
        self.color("palegreen")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    
    
    #def game_over(self):
    #    self.goto(0, 0)
    #    self.color("tomato")
    #    self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
        
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
        
        