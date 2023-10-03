from puzzler import Puzzler
import utils
import telebot

bot = telebot.TeleBot(utils.BOT_KEY)
puzzles = Puzzler()


def prompt_list(puzzles: list):
    return_str = 'Please select from the following :\n'
    for id in range(len(puzzles)):
        return_str = return_str+str(id+1)+') '+puzzles[id][0]+'\n'
    return return_str

@bot.message_handler(commands=['down'])
def echo_all(message):
    puzzle_list = None
    str_split = message.text.split(' ')
    
    if len(str_split) >= 2 and str_split[1] in utils.MAPPING:
        # TODO: Currently, there is no real check to confirm if type is real type or date is real date
        if len(str_split) >= 3:
            if str_split[2] in utils.MAPPING: 
                puzzle_list = puzzles.get_puzzle(str_split[1],str_split[2])
            else:
                bot.reply_to(message, utils.WELCOME,parse_mode="Markdown")
        else:
            puzzle_list = puzzles.get_puzzle(str_split[1],None)
        
        if puzzle_list and puzzle_list != []:
            if len(puzzle_list) <= 1:
                bot.reply_to(message,utils.GENERATING ,parse_mode="Markdown")
                bot.reply_to(message,puzzle_list[0][0]+': '+puzzles.create_puzzle(puzzle_list[0][1]),parse_mode="Markdown")
            else:
                reply = bot.reply_to(message,prompt_list(puzzle_list),parse_mode="Markdown")
                bot.register_next_step_handler(reply, reply_to_list,puzzle_list)
        elif puzzle_list == []:
            reply = bot.reply_to(message,utils.NO_GAMES,parse_mode="Markdown")
    else:
        bot.reply_to(message, utils.WELCOME,parse_mode="Markdown")
    
    puzzle_list = None

def reply_to_list(message,puzzle_list):
    num = int(message.text)-1

    if num < len(puzzle_list):
        puzzle = puzzle_list[num]
        bot.reply_to(message,utils.GENERATING,parse_mode="Markdown")
        bot.reply_to(message,puzzle[0]+': '+puzzles.create_puzzle(puzzle[1]),parse_mode="Markdown")
    else:
        bot.reply_to(message,utils.INVALID_GAME,parse_mode="Markdown")
        reply = bot.reply_to(message,prompt_list(puzzle_list),parse_mode="Markdown")
        bot.register_next_step_handler(reply, reply_to_list,puzzle_list)




bot.infinity_polling()