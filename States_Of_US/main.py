import turtle
import pandas
score = 0
guess = []


screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

"""
#returns x y coor when one clicks on screen  
def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
"""

data = pandas.read_csv("50_states.csv") 
states = data["state"].to_list()

while score < 50:
    
    title = f"{score}/50 States Correct"
    answer = screen.textinput(title, prompt= "What's another state's name?").title()
    
    if answer == "Exit":
        missing_states = [st for st in states if st not in guess]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break
    
    for e in states:    
        if answer == e:
            if answer not in guess:

                sts = turtle.Turtle()
                sts.hideturtle()
                sts.penup()
                x = int(data[data.state == answer].x)
                y = int(data[data.state == answer].y)
                sts.goto(x, y)
                sts.write(answer, font=("Arial", 8, "normal"))
                guess.append(answer)
                score += 1
    
#states to learn.csv

    

        

        
               









turtle.mainloop()


