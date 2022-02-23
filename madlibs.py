"""A madlib game that compliments its users."""

from random import choice
from random import sample
from random import choices
from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliments = ", ".join(choices(AWESOMENESS, k=3))
    

    return render_template("compliment.html", person=player, compliment=compliments)

@app.route("/game")
def show_madlib_form():
    player = request.args.get("person")
    compliments = ", ".join(choices(AWESOMENESS, k=3))
    wants_to_play = request.args.get("answer")

    if wants_to_play == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html", person=player, compliment=compliments)
    
@app.route("/madlib")
def show_madlib(): 
    person = request.args.get("name")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    number = request.args.get("number")
    luck = request.args.get("luck")
    lucky_choice = ["survived", "died", "run away", "got stuck", "disapeared"]
    
    if luck == "yes":
        luck = choice(lucky_choice)
    else:
        luck = "survived"
    madlib_templates = ["madlib1.html", "madlib2.html"]
    template_number = choice(madlib_templates)
    
    return render_template(template_number, person = person, color=color, noun=noun, 
                                    adjective=adjective, number=number, luck=luck)



if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
