from questions import QUESTIONS
from questions import EXTRA


def isAnswerCorrect(question, answer):
    return True if answer == question["answer"] else False


def ll_50_50(ques):
    print("\tYOUR NEW OPTIONS ARE :")
    if ques["answer"] == 1:
        print(f'\t\t\tOption 1: {ques["option1"]}')
        print(f'\t\t\tOption 2: {ques["option2"]}')
    if ques["answer"] == 2:
        print(f'\t\t\tOption 3: {ques["option3"]}')
        print(f'\t\t\tOption 2: {ques["option2"]}')
    if ques["answer"] == 3:
        print(f'\t\t\tOption 3: {ques["option3"]}')
        print(f'\t\t\tOption 4: {ques["option4"]}')
    if ques["answer"] == 4:
        print(f'\t\t\tOption 1: {ques["option1"]}')
        print(f'\t\t\tOption 4: {ques["option4"]}')


def ll_swap_ques(ques):
    from questions import EXTRA
    k = QUESTIONS.index(ques)
    if 0 <= k <= 4:
        print(f'\tQuestion {k + 1}: {EXTRA[0]["name"]}')
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {EXTRA[0]["option1"]}')
        print(f'\t\t\tOption 2: {EXTRA[0]["option2"]}')
        print(f'\t\t\tOption 3: {EXTRA[0]["option3"]}')
        print(f'\t\t\tOption 4: {EXTRA[0]["option4"]}')
    if 5 <= k <= 9:
        print(f'\tQuestion {k + 1}: {EXTRA[1]["name"]}')
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {EXTRA[1]["option1"]}')
        print(f'\t\t\tOption 2: {EXTRA[1]["option2"]}')
        print(f'\t\t\tOption 3: {EXTRA[1]["option3"]}')
        print(f'\t\t\tOption 4: {EXTRA[1]["option4"]}')
    if 10 <= k <= 14:
        print(f'\tQuestion {k + 1}: {EXTRA[2]["name"]}')
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {EXTRA[2]["option1"]}')
        print(f'\t\t\tOption 2: {EXTRA[2]["option2"]}')
        print(f'\t\t\tOption 3: {EXTRA[2]["option3"]}')
        print(f'\t\t\tOption 4: {EXTRA[2]["option4"]}')


def kbc():
    print("\t\t\t\t\t\t WELCOME TO KAUN BANEGA CROREPATI")
    price = 0
    y = 0
    x = 3
    u5, uS = 0, 0
    for i in range(15):
        if x == 1 and y != 3 and i != 14:
            print("\tYOUR LIFELINE 50-50 IS STILL AVAILABLE !!")
        elif x == 2 and y != 3 and i != 14:
            print("\tYOUR LIFELINE SWAP QUESTION IS STILL AVAILABLE !! ")
        elif x == 3 and y != 3 and i != 14:
            print("\tYOUR LIFELINE SWAP QUESTION and 50-50 BOTH ARE AVAILABLE !! ")

        else:
            if i < 14:
                print("\tYOU HAVE USED YOUR LIFELINE !!")
            else:
                print("\tYOU CANNOT USE YOUR LIFELINE IN THIS QUESTION")

        print(f'\tQuestion {i + 1}: {QUESTIONS[i]["name"]}')
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')

        if x == 3 and i != 14 and y != 3:
            print("Your choice ( 1-4 )/to use lifeline,type : 50-50 or Swap Question/if you want to quit type : QUIT")
        elif x == 2 and i != 14 and y != 3:
            print("Your choice ( 1-4 )/to use lifeline,type : Swap Question/if you want to quit type : QUIT")
        elif x == 1 and i != 14 and y != 3:
            print("")
        else:
            print("Your choice ( 1-4 )/if you want to quit type : QUIT")

        ans = input('Your choice ( 1-4 ) : ')

        if (u5 == 1 and ans == "50-50") or (uS == 1 and ans == "Swap Question"):
            while True:
                if ans == "50-50" and u5 == 1:
                    print("\tYOU ALREADY USED THIS LIFELINE, YOU ARE CHEATING DON'T REPEAT IT AGAIN !!")
                    u5 += 1
                    ans = input('Your choice ( 1-4 ) : ')
                elif ans == "Swap Question" and uS == 1:
                    print("\tYOU ALREADY USED THIS LIFELINE, YOU ARE CHEATING DON'T REPEAT IT AGAIN !!")
                    uS += 1
                    ans = input('Your choice ( 1-4 ) : ')
                else:
                    break
        if (u5 == 2 and ans == "50-50") or (uS == 2 and ans == "Swap Question"):
            print("\tYOU AGAIN REPEATED IT AFTER GETTING WARNED NOW YOU ARE OUT OF THE GAME")
            break

        print(u5)

        if ans == "50-50" and i != 14 and y != 3:
            ll_50_50(QUESTIONS[i])
            ans = input('Your choice : / Or to use your other lifeline, type: Swap Question ')
            x = 2
            y += x
            if ans == "Swap Question":
                ll_swap_ques(QUESTIONS[i])
                ans = input('Your choice : ')
                x = 1
                y += x
                uS = 1
            u5 = 1
        if ans == "Swap Question" and i != 14 and y != 3:
            ll_swap_ques(QUESTIONS[i])
            ans = input('Your choice : / Or to use your other lifeline, type: 50-50')
            x = 1
            y += x
            if ans == "50-50":
                ll_50_50(EXTRA[i])
                ans = input('Your choice :')
                x = 2
                y += x
                u5 = 1
            uS = 1
        if ans == "QUIT":
            print(f"\tYOU HAVE WON Rs{price}")
            break
        if 1 <= int(ans) <= 4:
            if isAnswerCorrect(QUESTIONS[i], int(ans)):
                price += QUESTIONS[i]["money"]
                print(f"\tYOUR ANSWER IS CORRECT AND YOU HAVE WON Rs{price}")
            else:
                if i < 5:
                    price = 0
                elif 5 <= i <= 10:
                    price = 10000
                else:
                    price = 320000
                print(f"\tYOUR ANSWER IS INCORRECT AND YOU HAVE WON Rs{price}")
                break


kbc()
