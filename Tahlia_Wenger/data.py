
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
    'items':[]
}

mail = {
    
}

puzzle = {
    'message':'<<You have a puzzle to complete>>',
    'command':'    + Type "puzzle" to complete it',
    'warning': '    + WARNING: if you leave the room the crime scene forensics will sweep your clues and the puzzle will no longer exist'
}

commands = {
    'head': '<<Useful Commands>>',
    'all': '  *To move = Type location name (e.g. "The Church) \n   help me || commands || map || mail || puzzle || quit'
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
        'name': '              The Precinct',
        'description': 'Buzzing with men in uniform, the precinct is the home of all detectives & police, their watching you.',
        'first':'Your boss has given you a new case. A young girl has been murdered in a back alley way coming out of a gym. The worst part, you recognise the way she has been killed. He is back. For your first clue complete the puzzle.',
        'exits': '<<Available exits>>',
        'exits1': ' > the church \n > the beach \n > the back alley'
    },
   'beach': {
        'name': '              The Beach',
        'description': "Running through a crowd of little kids and sweaty gym bros was not your idea of a good day, but you'll do anything so save the next victim, who you now know is Rebecca Sanders. The stares of people make you uncomfortably aware of the office clothes you have on. Let's just hope you can get to her before time is up.  ",
        'exits': '<<Available exits>>',
        'exits1': ' > the church \n > the precinct \n > the back alley'
    },
    'church': {
        'name': '              The Church',
        'description': 'As you enter the church, you instantly get the feeling that something is wrong. Your suspitions are confirmed when you look at the altar and instead of candles or a cross, you find an engraved knife and a letter addresses to you. Your only question, who is BOBBI?',
        'exits': '<<Available exits>>',
        'exits1': ' > the precinct \n > the beach \n > the back alley'
    },
    'alley' : {
        'name':'              The Back Alley',
        'description': 'With black painted brick walls, the alley was where the first victim was found. It leads to a gym with a boxing ring, which police suspect runs illegal fights but has never been proven.',
        'exits': '<<Available exits>>',
        'exits1': '> the church \n > the beach \n > the precinct'
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
alex1 = map['alley']['exits1']

#puzzles
puzzle1 = {
    'opening': 'The killers back, he has sent you a letter, the letter reads: ',
    'where': 'You have been left a clue, where is the killer trying to direct you to?',
    'locations':'   1. the beach \n   2. the church \n   3. the back alley'
}

puzzle2 = {
    'opening':'Using the knife to open the letter, you read the letter. The familiar handwriting reads:',
    'where': 'The killers clue clearly leads you to the last crime scene, but what are you looking for?',
    'items': '   1. a jacket \n   2. a wallet \n   3. a backpack'
    }

puzzle3 = {
    'opening':'After searching through the last victims backpack, you find a poster for a workout event called BOBBI (Builing Our Beach Bro Influence), a map where a section of the beach has a cross over it and a letter addressed you. How the killer got into the crime scene is beyond you but anyway, the letter reads:',
    'where':'The killer has left you a lot of useful clues in the letter. What is BOBBI? Who are you looking for?',
    'options':'   1. BOBBI is a man. I am looking for a brown eyed, blonde haired man. \n   2. BOBBI is a workout group called Builing Our Beach Bro Influence. I am looking for a brown haired, blue eyed girl.\n   3. BOBBI is a type of food. I am looking for a chef with brown eyes and blonde hair.\n   4. BOBBI is a workot group Builing Our Beach Bro Influence. I am looking for a brown eyed, blonde haired girl.',
    'afterread':'After reading the letter and doing a quick google, you find out that there is only one female attending the event, Rebecca Sanders. She must be the next victim.'
}

puzzle4 = {
    'opening':'You are struggling to find Rebecca through the crowd gathering for the event. You are worried about gain the killers attention.',
    'what':'What are you going to do?',
    'options':'   1. Scream \n   2. Fire your gun to gain attention \n   3. Do nothing a find her calmly \n   4. Ask people where she is \n   5. Call a task force and look for her individually',
    'after':'Now you know what to do lets go find Rebecca!'
}

fight = {
    'description': 'On your way to the back alley you notice some men dressed in dark colours following you. You attempt to get a good look at them but as you round the corner to the alley way you are hit on the head.',
    'options': 'Will you: \n 1. Fight Back \n 2. Run \n \n Please enter either 1 or 2 bellow'
}