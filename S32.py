import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "Sorry content dose not exist,'Contact with college' other wise If I were you, I would go to the internet and type exactly what you wrote there!"
R_NAME = "I don't have any name but you call mi 'GOSE_Assistant'"
R_ABOUT = "click the given link and get all the information about college :-\n      https://www.gsck.ac.in/aboutus.php"

R_TEACHER = "Teacher contact given below :-\n     Pravin sir :- 9876362301\n     Navi sir :- 5752841076\n     Mahesh sir :- 9955463021"
R_BSCTEACHER = "BSc teacher contact given below :-\n     solanki sir :- 5752841076  im.show()\n     Kolte sir :- 9955463021\n     Mahes sir :- 9955463021\n     Om sir :- 5752841076"
R_CONTACTUS = "college contac no :- 5752841076\n     Gmail :- gscollege120@gmail.com"
R_ADMINISTRATIONS = (
    "click the given link :-\n     https://www.gsck.ac.in/adminstc.php#govb"
)
R_PROSPECT = "Downlode college 'prospect' given link.\n     link curently not avaleble"
R_LTIMETABLE = "Enter your 'Group' :- "



def unknown():
    response = [
        "Could you please cheak your quation? ",
        "Not found...",
        "Somthing wants wrong.",
        "What does that mean?",
        "I don't know what you looking for plz ask me again!"
    ][random.randrange(5)]
    # Vijay-chopade
    return response
