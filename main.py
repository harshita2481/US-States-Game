import turtle as t
import pandas as pd
screen=t.Screen()
screen.title("US States Game")
image="blank_states_img.gif"
screen.addshape(image)
t.shape(image)
correct_guesses=[]
total=50
guessed=0
#For getting the coordinates
# def get_mouse_click(x,y):
#     print(x,y)
# t.onscreenclick(get_mouse_click)
# t.mainloop()
write_state=t.Turtle()
data=pd.read_csv("50_states.csv")
names=data["state"].to_list()
while guessed<50:
    ans=screen.textinput(title=f"{guessed}/50 states correct",prompt="What's another states name?").title()
    if ans=="Exit":
        missing_states=[num for num in names if num not in correct_guesses]
        new_data=pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if ans in names:
        if ans not in correct_guesses:
            guessed+=1
            correct_guesses.append(ans)
            x_cor=int(data[data.state==ans].x)
            y_cor=int(data[data.state==ans].y)
            write_state.color("black")
            write_state.hideturtle()
            write_state.penup()
            write_state.goto(x_cor,y_cor)
            write_state.write(f"{ans}",align="center",font=("Courier",10,"normal"))



screen.exitonclick()