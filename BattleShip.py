## Mengqi Li (ID: 92059150)
## ICS 31

import os.path

## Global Variables
P1_OCEAN_VIEW = [[' ',' ','0',' ','1',' ','2',' ','3',' ','4',' ','5',' ','6',' ','7',' ','8',' ','9'],
                  ['A',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['B',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['C',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['D',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['E',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['F',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['G',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['H',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['I',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['J',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_']]
P1_BOARD = [[' ',' ','0',' ','1',' ','2',' ','3',' ','4',' ','5',' ','6',' ','7',' ','8',' ','9'],
                  ['A',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['B',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['C',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['D',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['E',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['F',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['G',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['H',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['I',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['J',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_']]
P2_OCEAN_VIEW = [[' ',' ','0',' ','1',' ','2',' ','3',' ','4',' ','5',' ','6',' ','7',' ','8',' ','9'],
                  ['A',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['B',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['C',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['D',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['E',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['F',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['G',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['H',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['I',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['J',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_']]
P2_BOARD = [[' ',' ','0',' ','1',' ','2',' ','3',' ','4',' ','5',' ','6',' ','7',' ','8',' ','9'],
                  ['A',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['B',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['C',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['D',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['E',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['F',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['G',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['H',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['I',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_'],
                  ['J',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_',' ','_']]

LETTER_TO_INT = {"A":1,
				 "B":2,
				 "C":3,
				 "D":4,
				 "E":5,
				 "F":6,
				 "G":7,
				 "H":8,
				 "I":9,
				 "J":10}

SHIPS_CODE = {"CAR":"Carrier",
			  "BAT":"Battleship",
			  "CRU":"Cruiser",
			  "SUB":"Submarine",
			  "DES":"Destroyer"}
				 
board = [P1_OCEAN_VIEW, P1_BOARD, P2_OCEAN_VIEW, P2_BOARD] # [player 1 Ocean View, player 1 board, player 2 Ocean View, Player 2 board]
Player_OCEAN_VIEW = 0
Player_BOARD = 1
player = 1
P1_data = {}
P2_data = {}
P1_HP = {}
P2_HP = {}
hit_list = [[],[]]
miss_list = [[],[]]
getDamage_list = [[],[]]
survive_coor = [[],[]]
statistics = [[0,0,0],[0,0,0]]
P1_ship_inf = {}
P2_ship_inf = {}


def select_player_boards(player):
	global Player_OCEAN_VIEW, Player_BOARD
	if player == 1:
		Player_OCEAN_VIEW = 0
		Player_BOARD = 1
	else:
		Player_OCEAN_VIEW = 2
		Player_BOARD = 3
		
def print_board(player,board):
    p = "Player 1"
    if player == 2:
        p = "Player 2"
    for row in board:
        temp_str =""
        for position in row:
            temp_str += position
        print(temp_str)
	
def get_PlayerData(file_name):
	player_data = {}
	file = open(file_name, 'r')
	ships = file.read().split()
	for ship in ships:
		new_coor = []
		coor = ship.split(',')
		ship_name = coor[0]
		del coor[0]
		for c in coor:
			new_coor.append(list(c))
		player_data[ship_name] = new_coor
	return player_data

def init_board(player_data, board):
	for ship, coordinates in player_data.items():
		for c in coordinates:
			board[LETTER_TO_INT[c[0]]][(int(c[1])+1)*2] = "*"

def change_player():
	global player
	if player == 1:
		player = 2
	else:
		player = 1

def game_initial():
	global board, player, P1_HP, P2_HP, P1_data, P2_data, survive_coor
	
	# get data from txt files
	P1_data = get_PlayerData("p1.txt")
	P2_data = get_PlayerData("p2.txt")
	
	# initial survive list
	temp_list = []
	for ship, coordinates in P1_data.items():
		for coor in coordinates:
			temp_list.append(coor[0]+coor[1])
	temp_list.sort()
	survive_coor[0] = temp_list
	temp_list = []
	for ship, coordinates in P2_data.items():
		for coor in coordinates:
			temp_list.append(coor[0]+coor[1])
	temp_list.sort()
	survive_coor[1] = temp_list
	
	# initial ship HP
	for ship, coordinates in P1_data.items():
		P1_HP[ship] = len(coordinates)

	for ship, coordinates in P2_data.items():
		P2_HP[ship] = len(coordinates)
	
	# P1 initial board
	init_board(P1_data, board[1])
	# P2 initial board
	change_player()
	init_board(P2_data, board[3])

	# change back to P1 for start game
	change_player()

def input_validate(COMMAND):
	l = list(COMMAND)
	if len(l) == 2:
		if (l[0].isalpha()) and (l[0].upper() in "ABCDEFGHIJ") and (l[1].isdigit()):
			return True
		else:
			return False
	else:
		return False

def coordinate_validate(player, target):
	opponent_board = 3
	if player == 2:
		opponent_board = 1
	if board[opponent_board][LETTER_TO_INT[target[0]]][(int(target[1])+1)*2] == "X":
		return False
	else:
		return True
	
	
def call_shot():
	COMMAND = input("Enter target's coordinate [A-J][0-9] to fire at:")
	while True:
		if input_validate(COMMAND):
			target = list(COMMAND)
			target[0] = target[0].upper()
			if coordinate_validate(player, target):
				return target
			else:
				COMMAND = input("Please enter another coordinate [A-J][0-9]: ")
		else:
			COMMAND = input("Invalid coordinate. Please enter coordinate [A-J][0-9]: ")

def get_ship(target, opponent):
	if opponent == 1:
		for ship, coor in P1_data.items():
			if target in coor:
				return ship
	else:
		for ship, coor in P2_data.items():
			if target in coor:
				return ship

def lose_HP(s, opponent):
	global P1_HP, P2_HP
	if opponent == 1:
		for ship, HP in P1_HP.items():
			if s == ship:
				P1_HP[s] = HP - 1
	else:
		for ship, HP in P2_HP.items():
			if s == ship:
				P2_HP[s] = HP - 1

def target_to_cmd(target):
	return target[0]+target[1]
				
def hit_validate_process(player, target):
	global hit_list, miss_list, getDamage_list
	opponent = 2
	opponent_board = 3
	if player == 2:
		opponent = 1
		opponent_board = 1
	if board[opponent_board][LETTER_TO_INT[target[0]]][(int(target[1])+1)*2] == "*":
		select_player_boards(player)
		board[Player_OCEAN_VIEW][LETTER_TO_INT[target[0]]][(int(target[1])+1)*2] = "H"
		board[opponent_board][LETTER_TO_INT[target[0]]][(int(target[1])+1)*2] = "X"
		ship = get_ship(target, opponent)
		print(SHIPS_CODE[ship],"hit!")
		lose_HP(ship, opponent)
		if opponent == 2:
			if P2_HP[ship] == 0:
				print("You have sunk the enemey's",SHIPS_CODE[ship])
		else:
			if P1_HP[ship] == 0:
				print("You have sunk the enemey's",SHIPS_CODE[ship])
		
		# data update
		hit_list[player-1].append(target_to_cmd(target))
		getDamage_list[opponent-1].append(target_to_cmd(target))
		survive_coor[opponent-1].remove(target_to_cmd(target))
		statistics[player-1][0] += 1
		statistics[player-1][1] += 1
	else:
		board[Player_OCEAN_VIEW][LETTER_TO_INT[target[0]]][(int(target[1])+1)*2] = "M"
		print("MISS!")
		
		# data update
		miss_list[player-1].append(target_to_cmd(target))
		statistics[player-1][0] += 1
		statistics[player-1][2] += 1
		
def isWinner():
	opponent = 2
	if player == 2:
		opponent = 1
	
	win = True
	if opponent == 1:
		for ship, HP in P1_HP.items():
			if HP != 0:
				win = False
	else:
		for ship, HP in P2_HP.items():
			if HP != 0:
				win = False
	return win

def list_to_str(li):
	if len(li) == 0:
		string = ""
	else:
		string = li[0]
		del li[0]
		if len(li) != 0:
			for item in li:
				string +=(","+item)
	return string
	
def save_game():
	global P1_ship_inf, P2_ship_inf
	
	if player == 1:
		current_player = "P1"
	else:
		current_player = "P2"

	# get ship information
	temp_list = []
	for ship, data in P1_data.items():
		temp_list.append(P1_HP[ship])
		for coor in data:
			temp_list.append(coor[0]+coor[1])
		P1_ship_inf[ship] = temp_list
		temp_list = []
		
	temp_list = []
	for ship, data in P2_data.items():
		temp_list.append(P2_HP[ship])
		for coor in data:
			temp_list.append(coor[0]+coor[1])
		P2_ship_inf[ship] = temp_list
		temp_list = []
		
		
	file = open("game.txt","w")
	file.write("----- # start of file (not actually part of file content) ----\n")
	# P1 data 
	file.write(list_to_str(hit_list[0])+"\n")
	file.write(list_to_str(miss_list[0])+"\n")
	file.write(list_to_str(getDamage_list[0])+"\n")
	file.write(list_to_str(survive_coor[0])+"\n")
	string = ""
	for ship, data in P1_ship_inf.items():
		string += (ship+","+str(data[0]))
		for i in range(1,len(data)):
			string += (","+data[i])
		string += "\n"
	file.write(string)
	string = str(statistics[0][0])
	for i in range(1, len(statistics[0])):
		string += ","+str(statistics[0][i])
	file.write(string+"\n")
	
	# P2 data
	file.write(list_to_str(hit_list[1])+"\n")
	file.write(list_to_str(miss_list[1])+"\n")
	file.write(list_to_str(getDamage_list[1])+"\n")
	file.write(list_to_str(survive_coor[1])+"\n")
	string = ""
	for ship, data in P2_ship_inf.items():
		string += (ship+","+str(data[0]))
		for i in range(1,len(data)):
			string += (","+data[i])
		string += "\n"
	file.write(string)
	string = str(statistics[1][0])
	for i in range(1, len(statistics[1])):
		string += ","+str(statistics[1][i])
	file.write(string+"\n")
	
	file.write(current_player+"\n")
	file.write("---- # end of file (not actually part of file content) ----")
	file.close()
	
def game_process():
	global board, P1_HP, P2_HP, player
	game_saved = False
	while True:
		print("\nPlayer "+str(player)+"'s Turn")
		select_player_boards(player)
		print_board(player, board[Player_OCEAN_VIEW])
		print("\nPlayer 1 Ships HP   Player 2 Ships HP")
		print("CAR - {HP1}             CAR - {HP2}".format(HP1=str(P1_HP["CAR"]),HP2=str(P2_HP["CAR"])))
		print("BAT - {HP1}             BAT - {HP2}".format(HP1=str(P1_HP["BAT"]),HP2=str(P2_HP["BAT"])))
		print("CRU - {HP1}             CRU - {HP2}".format(HP1=str(P1_HP["CRU"]),HP2=str(P2_HP["CRU"])))
		print("SUB - {HP1}             SUB - {HP2}".format(HP1=str(P1_HP["SUB"]),HP2=str(P2_HP["SUB"])))
		print("DES - {HP1}             DES - {HP2}".format(HP1=str(P1_HP["DES"]),HP2=str(P2_HP["DES"])))
		COMMAND = input("\nO: Print Ocean View\nF: Fire at player\nS: Save Game\nEnter command:").upper()
		while True:
			if COMMAND == "O":
				print_board(player, board[Player_BOARD])
				COMMAND = input("\nO: Print Ocean View\nF: Fire at player\nEnter command:").upper()
			elif COMMAND == "F":
				target = call_shot()
				break
			elif COMMAND == "S":
				save_game()
				game_saved = True
				break
			else:
				COMMAND = input("Invalid command: Please re-enter command. ").upper()
		if game_saved:
			break
		else:
			hit_validate_process(player, target)
			if isWinner():
				print("\n\nPlayer "+str(player)+" WINS!")
				HPer1 = statistics[0][1]*100 / statistics[0][0]
				HPer2 = statistics[1][1]*100 / statistics[1][0]
				MPer1 = statistics[0][2]*100 / statistics[0][0]
				MPer2 = statistics[1][2]*100 / statistics[1][0]
				print("\n\nPlayer "+str(player)+" WINS!")
				print('{:<9}'.format('')+'{:<16}'.format('Player 1 Stats')+'{:<16}'.format('Player 2 Stats'))
				print('{:<9}'.format('Moves:')+'{:<16}'.format(str(statistics[0][0]))+'{:<16}'.format(str(statistics[1][0])))
				print('{:<9}'.format('Misses:')+'{:<16}'.format(str(statistics[0][2]))+'{:<16}'.format(str(statistics[1][2])))
				print('{:<9}'.format('Hits:')+'{:<16}'.format(str(statistics[0][1]))+'{:<16}'.format(str(statistics[1][1])))
				print('{:<9}'.format('Hit%:')+'{:<16}'.format("%.3f" % round(HPer1,3))+'{:<16}'.format("%.3f" % round(HPer2,3)))
				print('{:<9}'.format('Miss%:')+'{:<16}'.format("%.3f" % round(MPer1,3))+'{:<16}'.format("%.3f" % round(MPer2,3)))
				break
			else:
				change_player()


				
def game_load(path):
	global player, board, P1_data, P2_data, P1_HP, P2_HP, hit_list, miss_list, getDamage_list, survive_coor, statistics
	
	file = open(path, "r")
	# skip first line
	file.readline()
	
	# P1 data:
	hit_list[0] = file.readline().rstrip('\n').split(',')
	miss_list[0] = file.readline().rstrip('\n').split(',')
	getDamage_list[0] = file.readline().rstrip('\n').split(',')
	survive_coor[0] = file.readline().rstrip('\n').split(',')
	
	for i in range(5):
		temp = file.readline().rstrip('\n').split(',')
		
		P1_HP[temp[0]] = int(temp[1])
		temp_list = []
		for i in range(2,len(temp)):
			temp_list.append(list(temp[i]))
		P1_data[temp[0]] = temp_list
		
	data = file.readline().rstrip('\n').split(',')
	for i in range(3):
		statistics[0][i] = int(data[i])
		
	# P2 data
	hit_list[1] = file.readline().rstrip('\n').split(',')
	miss_list[1] = file.readline().rstrip('\n').split(',')
	getDamage_list[1] = file.readline().rstrip('\n').split(',')
	survive_coor[1] = file.readline().rstrip('\n').split(',')
	
	for i in range(5):
		temp = file.readline().rstrip('\n').split(',')
		
		P2_HP[temp[0]] = int(temp[1])
		temp_list = []
		for i in range(2,len(temp)):
			temp_list.append(list(temp[i]))
		P2_data[temp[0]] = temp_list
		
	data = file.readline().rstrip('\n').split(',')
	
	for i in range(3):
		statistics[1][i] = int(data[i])
	
	if "P1" in file.readline():
		player = 1
	else:
		player = 2
	
	# P1 load board
	if hit_list[0][0] != '':
		for coor in hit_list[0]:
			board[0][LETTER_TO_INT[list(coor)[0]]][(int(list(coor)[1])+1)*2] = "H"
	if miss_list[0][0] != '':
		for coor in miss_list[0]:	
			board[0][LETTER_TO_INT[list(coor)[0]]][(int(list(coor)[1])+1)*2] = "M"
	if getDamage_list[0][0] != '':
		for coor in getDamage_list[0]:
			board[1][LETTER_TO_INT[list(coor)[0]]][(int(list(coor)[1])+1)*2] = "X"
	if survive_coor[0][0] != '':
		for coor in survive_coor[0]:
			board[1][LETTER_TO_INT[list(coor)[0]]][(int(list(coor)[1])+1)*2] = "*"
	# P2 load board
	if hit_list[1][0] != '':
		for coor in hit_list[1]:
			board[2][LETTER_TO_INT[list(coor)[0]]][(int(list(coor)[1])+1)*2] = "H"
	if miss_list[1][0] != '':
		for coor in miss_list[1]:	
			board[2][LETTER_TO_INT[list(coor)[0]]][(int(list(coor)[1])+1)*2] = "M"
	if getDamage_list[1][0] != '':
		for coor in getDamage_list[1]:
			board[3][LETTER_TO_INT[list(coor)[0]]][(int(list(coor)[1])+1)*2] = "X"
	if survive_coor[1][0] != '':
		for coor in survive_coor[1]:
			board[3][LETTER_TO_INT[list(coor)[0]]][(int(list(coor)[1])+1)*2] = "*"
	
def main():
	global board, player
	print("--------- BATTLESHIP! ---------")
	COMMAND = input("L:    Load Game (game.txt)\nN:    New Game\nQ:    Quit\nEnter command: ").upper()
	while True:
		if COMMAND == "Q":
			break
		elif COMMAND == "N":
			game_initial()
			game_process()
			break
		elif COMMAND == "L":
			if os.path.isfile("game.txt"):
				game_load("game.txt")
				game_process()
				break
			else:
				COMMAND = input("game.txt file not exists: Please try another command. ").upper()
		else:
			COMMAND = input("Invalid command: Please re-enter command. ").upper()
		
		
	
main()
