from menti_bot import MentiBot
from data import total_votes
import threading


# will vote for all options
def auto_equal_vote():
    bot = MentiBot()
    bot.open_menti()
    bot.submit_menti_code()
    bot.get_voting_options()

    for i in range(total_votes):
        for option_nr in range(bot.nr_of_options):
            bot.reopen_menti()
            bot.vote(option_nr)
        bot.close_driver()


def vote_for_option(option_nr):
    bot = MentiBot()
    # needs to open for real once
    bot.open_menti()
    bot.submit_menti_code()
    bot.vote(option_nr)
    bot.close_driver()

    for i in range(total_votes - 1):
        bot.reopen_menti()
        bot.vote(option_nr)
        bot.close_driver()


def thread_function(function_name, arguments):
    if function_name == 'vote_for_option':
        option_nr = arguments
        for _ in range(9):
            new_thread = threading.Thread(target=vote_for_option, args=(option_nr,))
            new_thread.start()
        vote_for_option(option_nr)

    elif function_name == 'auto_equal_vote':
        auto_equal_vote()


