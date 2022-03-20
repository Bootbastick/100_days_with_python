import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States game")
image = "blank_states_image.gif"
screen.addshape(image)
turtle.shape(image)

file = pandas.read_csv("us_states.csv")
state_names = file.state

score = 0
correct_answers = []

while score < 50:
    answer_state = turtle.textinput(title=f"{score}/50 Guess the state", prompt="What's another state's name?")
    answer_state = answer_state.title()

    num = 0
    for i in state_names:
        if answer_state == "Exit":
            # Make a list with the states that user didn't named.
            missing_states = []
            for state in state_names:
                if state not in state_names:
                    missing_states.append(state)
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")
            exit()
        if i == answer_state:
            correct_answers.append(answer_state)
            diction = file.to_dict()
            x = diction["x"][num]
            y = diction["y"][num]

            writer = turtle.clone()
            writer.penup()
            writer.hideturtle()
            writer.goto(int(x), int(y))
            writer.write(i, align="center",  font=('Arial', 8, 'normal'))

            score += 1
        else:
            num += 1
