
def game_board():
	print("   0  1  2")
	for count,row in enumerate(p):
		print(count,row)

game=[[0,0,1],[0,1,1],[1,0,1]]
game_board()
def win(current_game):
	for col in range(len(p)):
		check=[]
		for row in p:
			check.append(row[col])
		if check.count(check[0]) == len(check) and check[0] != 0:
			print(f"Player {check[0]} Verticle winner")

	for row in p:
		if row.count(row[0]) == len(row) and row[0] != 0:
			print(f"Player {row[0]} Horizontal winner")

	diag = []
	for i in range(len(p)):
		diag.append(p[i][i])
	if diag.count(diag[0]) == len(diag) and diag[0] != 0:
		print(f"Player {diag[0]} Diagonal winner \\")

	diag = []
	for idx ,rev_idx in enumerate(reversed(range(len(p)))):
		diag.append(p[idx][rev_idx])
	if diag.count(diag[0]) == len(diag) and diag[0] != 0:
		print(f"Player {diag[0]} Diagonal winner /")



