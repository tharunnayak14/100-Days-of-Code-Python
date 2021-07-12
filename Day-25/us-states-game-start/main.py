import time
import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Guesser")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# def x_y_cor(x, y):
#     print(x, y)
# turtle.onscreenclick(x_y_cor)
# turtle.mainloop()

df = pd.read_csv("50_states.csv")

states = df["state"].tolist()
game_is_on = True

guessed_states = []
clock = turtle.Turtle()
clock.penup()
clock.hideturtle()
clock.goto(250, 250)


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        clock.clear()
        clock.write(timer, font=("Arial", 16, "normal"))
        time.sleep(1)
        t -= 1


countdown(300)
while len(guessed_states) < 50:

    answer = screen.textinput(title=f"{len(guessed_states) / 50}Guess the state's name",
                              prompt="What's the name of another state?").title()

    if answer == "Exit":
        # states to learn
        states_to_learn = []
        for state in states:
            if state not in guessed_states:
                states_to_learn.append(state)

        new_data = pd.DataFrame(states_to_learn)
        new_data.to_csv("missing_states.csv")
        break
    elif answer in states:
        name = turtle.Turtle()
        name.penup()
        name.hideturtle()
        state_row = df[df["state"] == answer]
        x_cor = int(state_row["x"])
        y_cor = int(state_row["y"])
        name.goto(x_cor, y_cor)
        name.write(answer)
        guessed_states.append(answer)

screen.exitonclick()
