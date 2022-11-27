
import re
import S32
import mail_no


def message_probability(
    user_message, recognised_words, single_response=False, required_words=[]
):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(
            message, list_of_words, single_response, required_words
        )

    # Responses ------------------------------------------------------------------------------------------------------------------
    response(
        "Hello!",
        ["hello", "hi", "hey", "sup", "heyo"],
        single_response=True,
    )
    response("Yah",["ok","okay", "good"],single_response=True,)
    response("See you!\n---------------------------------------------------------------------------------------", ["bye", "goodbye"], single_response=True)
    response(
        "I'm doing fine, you say!",
        ["how", "are", "you"],
        required_words=["how"],
    )
    response("You're welcome!", ["thank", "thanks"], single_response=True)
    response(
        "sorry we are including in a same sex", ["i", "love", "you"], required_words=["i", "love", "you"]
    )

    # Longer responses
    response(S32.R_ADVICE, ["give", "advice"], required_words=["advice"])
    response(S32.R_EATING, ["what", "you", "eat"], required_words=["you", "eat"])
    response(
        S32.R_NAME, ["what", "is", "your", "name"], required_words=["your", "name"]
    )
    response(
        S32.R_ABOUT,
        ["tell", "me", "about", "college"],
        required_words=["about", "college"],
    )
    response(
        S32.R_TEACHER,
        ["show", "me", "lecturer", "name", "and", "contact"],
        required_words=["lecturer", "contact"],
    )
    response(
        S32.R_BSCTEACHER,
        ["show", "me", "BSc", "lecturer", "name"],
        required_words=["bsc", "lecturer", "contact"],
    )
    response(
        S32.R_CONTACTUS,
        ["how", "can", "i", "contact", "with", "college"],
        required_words=["contact", "college"],
    )
    response(
        S32.R_ADMINISTRATIONS,
        ["give", "me", "college", "staff", "imformation"],
        required_words=["staff", "imformation"],
    )
    response(
        S32.R_PROSPECT,
        ["i", "need", "college", "prospect"],
        required_words=["prospectus"],
    )
    response(S32.R_LTIMETABLE,["i", "need", "lecture", "timetable"],required_words=["lecture", "timetable"],)
    
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return S32.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r"\s+|[,;?!.-]\s*", user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print("Assi :- " + get_response(input("User :- ")))



