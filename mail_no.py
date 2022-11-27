import re


i = str(input("\nAssi :- Before I answer your query, Can I know your 'Email' ? [yes/no]\nUser :- "))
if i == "yes":
    pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"
    user_input = input("Assi :- Enter your Gmail :- ")
    if re.search(pattern, user_input):
        print("Assi :- Thanks for subscribing,\n---------------------------------------------------------------------------------------\nAssi :- Now tell me how can i 'Help' you")
    else:
        print("Assi :- invalid Gmail")
elif i == "no":
    j = str(input("Assi :- Ok,Can I know your 'Contact Number' ? [yes/no]\nUser :- "))
    if j == "yes":
        pattern = "(\d\d\d)-(\d\d\d)-(\d\d\d\d)"
        new_pattern = r"\1\2\3"
        user_input = input("Assi :- Enter your number :- ")
        new_user_input = re.sub(pattern, new_pattern, user_input)
        print(
            "Assi :- Thanks for subscribing,\n---------------------------------------------------------------------------------------\nAssi :- Now tell me how can i 'Help' you"
        )
    elif j == "no":
        print("---------------You missed your 'subscription'---------------\n")
    else:
        print("---------------You missed your 'subscription'---------------\n")
else:
    print("Assi :- You missed your subscription\n---------------------------------------------------------------------------------------\nAssi :- BY the way, How can i 'Help' you")
