BOT_KEY = 'ENTER YOUR KEY'
TIMEOUT = 60 # [s]
REFRESHTIME = .1 #[s]
# Down for a cross stuff
DOWN_API = 'https://api.foracross.com/api/puzzle_list?page=0&pageSize=50&filter%5BnameOrTitleFilter%5D=&filter%5BsizeFilter%5D%5BMini%5D=true&filter%5BsizeFilter%5D%5BStandard%5D=true'
REQUEST = 'https://downforacross.com/beta/play/'

WELCOME = 'Please select type of puzzle and date: \n\n**PUZZLES**\nnyt: New York Times\nla : LA Times\ntc : The Crossword \nr : Random crossword\n\n**DATES**\ntoday: Today\nmon: Monday\ntues: Tuesday\nwed: Wednesday\nthurs: Thuesday \nfri: Friday\nsat: Saturday\nsun: Sunday\n\n\n For example:\n/down nyt\n/down la tues\n/down r'
GENERATING = 'Generating game, please wait...'
NO_GAMES = 'Sorry there are no available games for selected game type and dates...'
INVALID_GAME = 'Sorry that is not a valid number, please select again'
MAPPING = {
    'nyt'   : 'NY Times',
    'la'    : 'LA Times',
    'tc'    : 'The Crossword',
    'mon'   : 'Mon',
    'tues'  : 'Tue',
    'wed'   : 'Wed',
    'thurs' : 'Thu',
    'fri'   : 'Fri',
    'sat'   : 'Sat',
    'sun'   : 'Sun',
    'today' :  None,
    'r'     :  None
}