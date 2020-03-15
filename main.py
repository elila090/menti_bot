from menti_bot import MentiBot
from data import votes_per_option


# will vote for all options
def auto_voting(bot):
    for option_nr in range(bot.nr_of_options):
        bot.open_menti()
        bot.submit_menti_code()
        bot.vote(option_nr)


def main():
    for i in range(votes_per_option):
        bot = MentiBot()
        bot.open_menti()
        bot.submit_menti_code()
        bot.get_voting_options()
        auto_voting(bot)
        bot.close_driver()


main()

