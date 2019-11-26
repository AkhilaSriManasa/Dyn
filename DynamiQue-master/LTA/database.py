import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE t_message (id int, m_name text, m_text text, m_keyword)"

cursor.execute(create_table)

messages = [
    (1, 'BookOfPython', '''Real–time strategy (RTS) games such as Blizzard Entertainment’s Starcraft(tm) and Warcraft(tm) series form a large and
growing part of the multi–billion dollar computer games
industry. In these games several players fight over resources, which are scattered over a terrain, by first setting up
economies, building armies, and ultimately trying to eliminate all enemy units and buildings. The current AI performance in commercial RTS games is poor. The main reasons
why the AI performance in RTS games is lagging behind developments in related areas such as classic board games are
the following:
• RTS games feature hundreds or even thousands of interacting objects, imperfect information, and fast–paced
micro–actions. By contrast, World–class game AI systems mostly exist for turn–based perfect information
games in which the majority of moves have global consequences and human planning abilities therefore can be
outsmarted by mere enumeration.
• Video games companies create titles under severe time
constraints and do not have the resources and incentive
(yet) to engage in AI research.
• Multi–player games often do not require World–class AI
performance in order to be commercially successful as
long as there are enough human players interested in playing the game on–line.
• RTS games are complex which means that it is not easy to
set up an RTS game infrastructure for conducting AI experiments. Closed commercial RTS game software without AI interfaces does not help, either. The result is a lack
of AI competition in this area which in the classic games
sector is one of the most important driving forces of AI
research. 



To get a feeling for the vast complexity of RTS games, imagine to play chess on a 512×512 board with hundreds of
slow simultaneously moving pieces, player views restricted
to small areas around their own pieces, and the ability to
gather resources and create new material.
While human players sometimes struggle with micro–
managing all their objects, it is the incremental nature of
the actions that allows them to outperform any existing RTS
game AI. The difference to classic abstract games like chess
and Othello in this respect is striking: many moves in these
games have immediate global effects. This makes it hard
for human players to consider deep variations with all their
consequences. On the other hand, computers programs conducting full–width searches with selective extensions excel
in complex combinatorial situations. A notable exception is
the game of go in which — like in RTS games — moves
often have only incremental effects and today’s best computer programs are still easily defeated by amateurs (Muller ¨
2002). It is in these domains where the human abilities to
abstract, generalize, reason, learn, and plan shine and the
current commercial RTS AI systems — which do not reason
nor adapt — fail.''', 'zero'),
    (2,'LearnToCodeInDays','JavaScript (JS) is a lightweight, interpreted, or just-in-time compiled programming language with first-class functions. While it is most well-known as the scripting language for Web pages, many non-browser environments also use it, such as Node.js, Apache CouchDB and Adobe Acrobat.','zero'),
    (3,'NoProbLem', 'Recursion is the process which comes into existence when a function calls a copy of itself to work on a smaller problem. Any function which calls itself is called recursive function, and such function calls are called recursive calls.','zero'),
    
]

insert_query = "INSERT INTO t_message VALUES (?, ?, ?, ?)"

cursor.executemany(insert_query, messages)

connection.commit()

connection.close()

