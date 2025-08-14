health = 100
if health > 100:
    health = 100

intro = {
        'breakspace': '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~',
        'welcome': '          Unsolved: The Correspondance',
        'description': '   * Travel between (Number) crime scenes \n    * Follow clues from your killer \n    * Solve perpelexing puzzles \n    * Fight against the clock to save the next victim \n    *Discover multiple multiple endings based on your success \n Can you crack the code before its too late?'
}

start=  {
        'success': "SOME QUICK TIPS:",
        'basic':'       - All answers are case sensitive so make sure you copy comands exactly!\n        - Type "commands" to view all your options\n        - Type "help me" for some useful hints and full instructions \n        - Type "map" so see all locations \n        - Type "mail" to review all your letter and emails'
    }

#menu
inventory = {
    'message':'<<Your Current Inventory>>',
    'items':''
}

mail = {
    'your first letter': "Hello Detective, \n Its been a long time. I'm sure you remember me, just as I remember you. I spent a long time locked up because of you, my reputation is ruined. Now I'm back, I'll go back to doing what I love. And you'll go back to chasing me. Find your first clue at the place where  water meets te forehead, the sun shines in colour and you can finally find your people."
}

puzzle = {
    'message':'<<You have a puzzle to complete>>',
    'command':'    + Type "puzzle" to complete it'
}

commands = {
    'head': '<<Useful Commands>>',
    'all': '  *To move = Type location name (e.g. "The Church) \n   help me || commands || map || mail || puzzle'
}

#options
help = {
    'heading':'              Help me!!',
    'ahead': '<<Your aim>>',
    'your aim': 'Travel throught the rooms, solving the clues and puzzles, and stop the killer from harming his next victim',
    'chead': '<<Commands>>',
    'commands': '- To move to a new location, type the location name (case sensitve)\n        - Type "commands" to view all your options and extra commands\n        - Type "help me" for some useful hints and full instructions \n        - Type "map" so see all locations \n        - Type "mail" to review all your letter and emails \n        - Type "quit" to end the game',
    'lhead' : '<<Locations>>',
    'locations': '> the church \n> the beach \n> the back alley \n> the office',
    'thead': '<<Tips>>',
    'tips': '- All answers are case sensitive so make sure you answers match exactly \n- There are a lot of twists, be ready for anything \n- You are a detective, there are dangers with the job, be prepared \n- There are different endings, you choices will lead to whether you succeed or fail \n- Keepm a close eye on your health and progess, these are vital \n- Pay attention to nots, emails, desciptions and puzzles, these may help you later \n- During a puzzle, consider the question and review all the answers',
    'fail': "You've got this! Good luck!"
}

commandss = {
    'heading': '              Commands',
    'thead': '<<Travel Commands>>',
    'travel': '    - To travel to a place, type in the name of the place (e.g. "the beach"). \n    This is case sensitve make sure its the same.',
    'ghead': '<<Game Commands>>',
    'game': '    - Type "help" to view help menus and tips \n    - Type "commands" to view this page \n    - Type "map" to view locations \n    - Type "mail" to review your letter and emails \n    - Type "puzzle" to complete an available puzzle \n    - Type "quit" to end the game',
    'phead': '<<Puzzle Commands>>',
    'puzzle': '    - Most puzzles are multiple choice, type the number of you answer to complete the puzzle \n    - Consider the question and review all options before answering \n    - The "help" function has some extra help',
    'bhead': '<<Battle Commands>>',
    'battle': '    1. Attack the enemy \n    2. Run away from the enemy'
}

map = {
    'heading': '              The Correspondance Map',
    'office' : {
        'name': 'The Precinct',
        'description': 'Buzzing with men in uniform, the precinct is the home of all detectives & police, their watching you.',
        'first':'Your boss has given you a new case. A young girl has been murdered in a back alley way coming out of a gym. The worst part, you recognise the way she has been killed. He is back. For your first clue complete the puzzle.',
        'exits': '<<Available exits>>',
        'exits1': ' > the church \n > the beach \n > the back alley'
    },
   'beach': {
        'name': 'The Beach',
        'description': '',
        'exits': '<<Available exits>>',
        'exits1': ''
    },
    'church': {
        'name': 'The Church',
        'description': '',
        'exits': '<<Available exits>>',
        'exits1': ''
    },
    'alley' : {
        'name':'The Back Alley',
        'description': '',
        'exits': '<<Available exits>>',
        'exits1': ''
    }
}
offname = map['office']['name']
offdes = map['office']['description']
offfirst = map['office']['first']
offex = map['office']['exits']
offex1 = map['office']['exits1']

bena = map['beach']['name']
bedes = map['beach']['description']
beex = map['beach']['exits']
beex1 = map['beach']['exits1']

chna = map['church']['name']
chdes = map['church']['description']
chex = map['church']['exits']
chex1 = map['church']['exits1']

alna = map['alley']['name']
aldes = map['alley']['description']
alex = map['alley']['exits']
alex = map['alley']['exits1']

#puzzles
puzzle2 = {
    'opening': 'The killers back, he has sent you a letter, the letter reads: ',
    'where': 'You have been left a clue, where is the killer trying to direct you to?',
    'locations':'   1. the beach \n   2. the church \n   3. the back alley'
}