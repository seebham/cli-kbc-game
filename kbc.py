from questions import QUESTIONS
import random


def isAnswerCorrect(question: map, answer: int) -> bool:

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''
    return question["answer"] == answer

def lifeLine(ques: map) -> bool:
    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''
    answer_ind = ques["answer"]
    del_options = []
    for i in range(1, 4):
        if len(del_options) > 1: break;
        if i != answer_ind:
            del ques[f'option{i}']
            del_options.append(i)
    print('\tOHOHHO Lifeline! Now, the 50-50 options are:-')
    for i in range(1, 5):
        if i not in del_options:
            print(f'\t\t\tOption {i}: {ques[f"option{i}"]}')
    return True


def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    #  For now, the below code works for only one question without LIFE-LINE and QUIT checks
    print("\tNamaskar, main Shamitabh Bacchan aapka swagat karta hu Kaun Banega Crorepati (KBC) mein!")

    total_reward = 0
    min_reward = 0
    rounds = 0
    lifeline_used = False
    using_lifeline = False
    while rounds < 15:
        
        if not using_lifeline:
            if not lifeline_used:   print('\tYou have a spare lifeline! To avail type: \"lifeline\"')
            print(f'\tYou can quit the game and take Rs. {total_reward} home!')
            print(f'\tQuestion {rounds+1}: {QUESTIONS[rounds]["name"]}' )
            print(f'\t\tOptions:')
            for i in range(1, 5):
                print(f"\t\t\tOption {i}: {QUESTIONS[rounds][f'option{i}']}")

        # For testing
        # print(f'\tAnswer: {QUESTIONS[rounds]["answer"]}')

        ans = input('Your choice ( 1-4 ) : ')

        # check for the input validations
        if len(ans) != 1:
            if ans == "quit":
                print(f'\tThanks for playing! You won Rs. {total_reward}')
                break;
            if ans == "lifeline":
                if not lifeline_used and rounds != 14:
                    using_lifeline = lifeLine(QUESTIONS[rounds])
                    lifeline_used = True
                else:   print("\tSorry! You have already used your lifeline or you're attempting the 15th Question!")
            else:   print("\tInvalid Input. Try again")
            continue

        if isAnswerCorrect(QUESTIONS[rounds], int(ans)):
            using_lifeline = False
            total_reward = (QUESTIONS[rounds])["money"]
            # print the total money won.
            # See if the user has crossed a level, print that if yes
            if rounds == 14:
                print("\t\t     ** 1 Crore!!! PARTY 🥳 **")
                print(f'\t\tAap jeet gaye hai Rs. {total_reward}!')
                break;

            print(f'\nSahi javab! Aapka milta hai Rs. {total_reward} ka Cheque!\n')
            if rounds == 4:
                min_reward = 10000
                print("\tBohot badhiya! Aap pohoch chuke ho 1st Padav par!")
            if rounds == 10:
                min_reward = 320000
                print("\tBohot badhiya! Aap pohoch chuke ho dusre 2nd Padav par!")

        else:
            # end the game now.
            # also print the correct answer
            using_lifeline = False
            answer_ind = (QUESTIONS[rounds]["answer"])
            print(f"\n\tIncorrect! Galat javab!🙁\n\tSahi savab tha \"{QUESTIONS[rounds][f'option{answer_ind}']}\"")
            print(f"\tTotal Dhanrashi you won : {min_reward}")
            break;

        rounds += 1


kbc()
