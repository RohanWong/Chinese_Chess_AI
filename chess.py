# -*- coding: utf-8 -*-
import sys, time			
from PyQt5 import QtGui, QtWidgets

board =[]
red_alive = []
black_alive = []



class Chess(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()      
        self.initUI()
        self.start = True
        self.human_move_done = True
        self.turn_color = 'F'
 
    def initUI(self):             
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('images/board.png')))
        self.setPalette(palette1)
        self.load_in_pngs()  

        gameAction = QtWidgets.QAction('Start a new game', self)
        gameAction.setShortcut('Ctrl+N')
        gameAction.setStatusTip('Start a new game')
        gameAction.triggered.connect(self.start)
 
        self.statusBar()
        self.statusBar().showMessage('Ready')
 
        menubar = self.menuBar()
        gameMenu = menubar.addMenu('&Game')
        gameMenu.addAction(gameAction)    
 
        self.init_board()

        self.resize(800, 880)
        self.center()
        self.setWindowTitle('Chinese Chess AI')
        self.setMinimumSize(800, 880)
        self.setMaximumSize(800, 880)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def load_in_pngs(self):
    	#todo : 把所有棋子图像都读进来
    	##black
    	png = QtGui.QPixmap('images/zu.png')
    	self.zu_0 = QtWidgets.QLabel(self)   	
    	self.zu_0.setPixmap(png)
    	self.zu_0.resize(60, 60)
    	self.zu_1 = QtWidgets.QLabel(self)
    	self.zu_1.setPixmap(png)
    	self.zu_1.resize(60, 60)
    	self.zu_2 = QtWidgets.QLabel(self)
    	self.zu_2.setPixmap(png)
    	self.zu_2.resize(60, 60)
    	self.zu_3 = QtWidgets.QLabel(self)
    	self.zu_3.setPixmap(png)
    	self.zu_3.resize(60, 60)
    	self.zu_4 = QtWidgets.QLabel(self)
    	self.zu_4.setPixmap(png)
    	self.zu_4.resize(60, 60)
    	png = QtGui.QPixmap('images/heipao.png')
    	self.heipao_0 = QtWidgets.QLabel(self)
    	self.heipao_0.setPixmap(png)
    	self.heipao_0.resize(60, 60)
    	self.heipao_1 = QtWidgets.QLabel(self)
    	self.heipao_1.setPixmap(png)
    	self.heipao_1.resize(60, 60)
    	png = QtGui.QPixmap('images/heiche.png')
    	self.heiche_0 = QtWidgets.QLabel(self)
    	self.heiche_0.setPixmap(png)
    	self.heiche_0.resize(60, 60)
    	self.heiche_1 = QtWidgets.QLabel(self)
    	self.heiche_1.setPixmap(png)
    	self.heiche_1.resize(60, 60)
    	png = QtGui.QPixmap('images/heima.png')
    	self.heima_0 = QtWidgets.QLabel(self)
    	self.heima_0.setPixmap(png)
    	self.heima_0.resize(60, 60)
    	self.heima_1 = QtWidgets.QLabel(self)
    	self.heima_1.setPixmap(png)
    	self.heima_1.resize(60, 60)
    	png = QtGui.QPixmap('images/heixiang.png')
    	self.heixiang_0 = QtWidgets.QLabel(self)
    	self.heixiang_0.setPixmap(png)
    	self.heixiang_0.resize(60, 60)
    	self.heixiang_1 = QtWidgets.QLabel(self)
    	self.heixiang_1.setPixmap(png)
    	self.heixiang_1.resize(60, 60)
    	png = QtGui.QPixmap('images/heishi.png')
    	self.heishi_0 = QtWidgets.QLabel(self)
    	self.heishi_0.setPixmap(png)
    	self.heishi_0.resize(60, 60)
    	self.heishi_1 = QtWidgets.QLabel(self)
    	self.heishi_1.setPixmap(png)
    	self.heishi_1.resize(60, 60)
    	png = QtGui.QPixmap('images/jiang.png')
    	self.jiang = QtWidgets.QLabel(self)
    	self.jiang.setPixmap(png)
    	self.jiang.resize(60, 60)
    	##red
    	png = QtGui.QPixmap('images/bing.png')
    	self.bing_0 = QtWidgets.QLabel(self)   	
    	self.bing_0.setPixmap(png)
    	self.bing_0.resize(60, 60)
    	self.bing_1 = QtWidgets.QLabel(self)
    	self.bing_1.setPixmap(png)
    	self.bing_1.resize(60, 60)
    	self.bing_2 = QtWidgets.QLabel(self)
    	self.bing_2.setPixmap(png)
    	self.bing_2.resize(60, 60)
    	self.bing_3 = QtWidgets.QLabel(self)
    	self.bing_3.setPixmap(png)
    	self.bing_3.resize(60, 60)
    	self.bing_4 = QtWidgets.QLabel(self)
    	self.bing_4.setPixmap(png)
    	self.bing_4.resize(60, 60)
    	png = QtGui.QPixmap('images/hongpao.png')
    	self.hongpao_0 = QtWidgets.QLabel(self)
    	self.hongpao_0.setPixmap(png)
    	self.hongpao_0.resize(60, 60)
    	self.hongpao_1 = QtWidgets.QLabel(self)
    	self.hongpao_1.setPixmap(png)
    	self.hongpao_1.resize(60, 60)
    	png = QtGui.QPixmap('images/hongche.png')
    	self.hongche_0 = QtWidgets.QLabel(self)
    	self.hongche_0.setPixmap(png)
    	self.hongche_0.resize(60, 60)
    	self.hongche_1 = QtWidgets.QLabel(self)
    	self.hongche_1.setPixmap(png)
    	self.hongche_1.resize(60, 60)
    	png = QtGui.QPixmap('images/hongma.png')
    	self.hongma_0 = QtWidgets.QLabel(self)
    	self.hongma_0.setPixmap(png)
    	self.hongma_0.resize(60, 60)
    	self.hongma_1 = QtWidgets.QLabel(self)
    	self.hongma_1.setPixmap(png)
    	self.hongma_1.resize(60, 60)
    	png = QtGui.QPixmap('images/hongxiang.png')
    	self.hongxiang_0 = QtWidgets.QLabel(self)
    	self.hongxiang_0.setPixmap(png)
    	self.hongxiang_0.resize(60, 60)
    	self.hongxiang_1 = QtWidgets.QLabel(self)
    	self.hongxiang_1.setPixmap(png)
    	self.hongxiang_1.resize(60, 60)
    	png = QtGui.QPixmap('images/hongshi.png')
    	self.hongshi_0 = QtWidgets.QLabel(self)
    	self.hongshi_0.setPixmap(png)
    	self.hongshi_0.resize(60, 60)
    	self.hongshi_1 = QtWidgets.QLabel(self)
    	self.hongshi_1.setPixmap(png)
    	self.hongshi_1.resize(60, 60)
    	png = QtGui.QPixmap('images/shuai.png')
    	self.shuai = QtWidgets.QLabel(self)
    	self.shuai.setPixmap(png)
    	self.shuai.resize(60, 60)

    def init_board(self):
    	#todo : 把所有棋子都放到初始位置
    	global board 
    	global red_alive
    	global black_alive
    	##black
    	self.zu_0.move(1*80 - 30, 4 * 80 - 30)
    	self.zu_1.move(3*80 - 30, 4 * 80 - 30)
    	self.zu_2.move(5*80 - 30, 4 * 80 - 30)
    	self.zu_3.move(7*80 - 30, 4 * 80 - 30)
    	self.zu_4.move(9*80 - 30, 4 * 80 - 30)
    	self.heipao_0.move(2*80 - 30, 3 * 80 - 30)
    	self.heipao_1.move(8*80 - 30, 3 * 80 - 30)
    	self.heiche_0.move(1*80 - 30, 1 * 80 - 30)
    	self.heiche_1.move(9*80 - 30, 1 * 80 - 30)
    	self.heima_0.move(2*80 - 30, 1 * 80 - 30)
    	self.heima_1.move(8*80 - 30, 1 * 80 - 30)
    	self.heixiang_0.move(3*80 - 30, 1 * 80 - 30)
    	self.heixiang_1.move(7*80 - 30, 1 * 80 - 30)
    	self.heishi_0.move(4*80 - 30, 1 * 80 - 30)
    	self.heishi_1.move(6*80 - 30, 1 * 80 - 30)
    	self.jiang.move(5*80 - 30, 1 * 80 - 30)
    	##red
    	self.bing_0.move(1*80 - 30, 7 * 80 - 30)
    	self.bing_1.move(3*80 - 30, 7 * 80 - 30)
    	self.bing_2.move(5*80 - 30, 7 * 80 - 30)
    	self.bing_3.move(7*80 - 30, 7 * 80 - 30)
    	self.bing_4.move(9*80 - 30, 7 * 80 - 30)
    	self.hongpao_0.move(2*80 - 30, 8 * 80 - 30)
    	self.hongpao_1.move(8*80 - 30, 8 * 80 - 30)
    	self.hongche_0.move(1*80 - 30, 10 * 80 - 30)
    	self.hongche_1.move(9*80 - 30, 10 * 80 - 30)
    	self.hongma_0.move(2*80 - 30, 10 * 80 - 30)
    	self.hongma_1.move(8*80 - 30, 10 * 80 - 30)
    	self.hongxiang_0.move(3*80 - 30, 10 * 80 - 30)
    	self.hongxiang_1.move(7*80 - 30, 10 * 80 - 30)
    	self.hongshi_0.move(4*80 - 30, 10 * 80 - 30)
    	self.hongshi_1.move(6*80 - 30, 10 * 80 - 30)
    	self.shuai.move(5*80 - 30, 10 * 80 - 30)

    	self.select = ''
    	self.select_pos = [0,0]

    	board =[['0','0','0','0','0','0','0','0','0','0','0'],
    			['0','heiche_0','heima_0','heixiang_0','heishi_0','jiang','heishi_1','heixiang_1','heima_1','heiche_1','0'],
				['0','0','0','0','0','0','0','0','0','0','0'],
				['0','0','heipao_0','0','0','0','0','0','heipao_1','0','0'],
				['0','zu_0','0','zu_1','0','zu_2','0','zu_3','0','zu_4','0'],
				['0','0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0','0'],
				['0','bing_0','0','bing_1','0','bing_2','0','bing_3','0','bing_4','0'],
				['0','0','hongpao_0','0','0','0','0','0','hongpao_1','0','0'],
				['0','0','0','0','0','0','0','0','0','0','0'],
				['0','hongche_0','hongma_0','hongxiang_0','hongshi_0','shuai','hongshi_1','hongxiang_1','hongma_1','hongche_1','0'],
				['0','0','0','0','0','0','0','0','0','0','0'],]
    	
    	red_alive = ['bing_0','bing_1','bing_2','bing_3','bing_4','hongpao_0','hongpao_1','hongche_0','hongma_0','hongxiang_0','hongshi_0','shuai','hongshi_1','hongxiang_1','hongma_1','hongche_1']
    	black_alive = ['zu_0','zu_1','zu_2','zu_3','zu_4','heipao_0','heipao_1','heiche_0','heima_0','heixiang_0','heishi_0','jiang','heishi_1','heixiang_1','heima_1','heiche_1']

    def start(self):
	    self.init_board()
	    self.turn = 'H' #human 
	    self.turn_color = 'R' #red
	    self.start = False
	    self.vs_AI()
    
    def vs_AI(self):
    	if self.turn == 'H':
    		self.human_go()
    	elif self.turn == 'A': #AI
    		self.ai_go()




    def end_check(self):
    	global red_alive
    	global black_alive
    	if 'shuai' not in red_alive or 'jiang' not in  black_alive:
    		return True
    	else:
    		return False
    
    def celebrate(self):
    	reply = QtWidgets.QMessageBox.information(self," ", self.tr("游戏结束!"))  

   
    def human_go(self):
    	self.select = ''
    	self.select_pos = [0,0]
    	self.human_move_done = False
    	self.statusBar().showMessage("Your turn!")
    
    def ai_go(self):
    	self.statusBar().showMessage("AI turn!")
    	self.sol = [0,0]
    	self.AlphaBeta(4, -1000000, 1000000)
    	self.piece_move(self.sol[0], self.sol[1])
    	if self.end_check():
    		self.celebrate()
    	else:
    		self.turn = 'H'
    		if self.turn_color == 'R':
    			self.turn_color = 'B'
    		else:
    			self.turn_color = 'R'
    		self.vs_AI()

    def AlphaBeta(self, depth, alpha, beta):
    	global board 
    	global red_alive
    	global black_alive 
    	moves = []
    	des = [0,0]
    	ori = [0,0]
    	tmp =  [['0','0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0','0'],
				['0','0','0','0','0','0','0','0','0','0','0'],]
    	if depth == 0:
    		return self.evaluate()
    	self.gen_moves(moves, depth)
    	val = 0
    	while moves:
    		[ori[0], ori[1], des[0], des[1]] = moves[0]
    		del moves[0]
    		for xx in range(1, 11):
    			for yy in range(1,10):
    				tmp[xx][yy] = board[xx][yy]
    		tmp_red = red_alive[:]
    		tmp_black = black_alive[:]
    		self.make_a_move(ori[0], ori[1], des[0], des[1])
    		val = -1 * self.AlphaBeta(depth-1, -1*beta, -1*alpha)
    		for xx in range(1, 11):
    			for yy in range(1,10):
    				board[xx][yy] = tmp[xx][yy]
    		red_alive = tmp_red[:]
    		black_alive = tmp_black[:]
    		if val >= beta:
    			return beta
    		if val > alpha:
    			alpha = val
    			if depth == 4:
    				self.select_pos[0] = ori[0]
    				self.select_pos[1] = ori[1]
    				self.select = board[ori[0]][ori[1]]
    				self.sol[0] = des[0]
    				self.sol[1] = des[1]
    	return alpha

    def evaluate(self):
    	global board
    	global red_alive
    	global black_alive
    	count = 0
    	for x in range(1, 11):
    		for y in range(1, 10):
    			if board[x][y] == '0':
    				continue
    			elif board[x][y].find('shuai') != -1:
    				count = count - 100000
    			elif board[x][y].find('jiang') != -1:
    				count = count + 100000
    			elif board[x][y].find('bing') != -1:
    				if x > 5:
    					count = count - (11 - x) - 100
    				else:
    					count = count - (11 - x) - 200
    			elif board[x][y].find('zu') != -1:
    				if x <= 5:
    					count = count + x + 100
    				else:
    					count = count + x + 200
    			elif board[x][y].find('hongpao') != -1:
    				count = count - (11-x) - 450
    			elif board[x][y].find('hongche') != -1:
    				count = count - (11-x) - 900
    			elif board[x][y].find('hongma') != -1:
    				count = count - (11-x) - 400
    			elif board[x][y].find('hongxiang') != -1:
    				count = count - (11-x) - 200
    			elif board[x][y].find('hongshi') != -1:
    				count = count - (11-x) - 200
    			elif board[x][y].find('heishi') != -1:
    				count = count + x + 200
    			elif board[x][y].find('heixiang') != -1:
    				count = count + x + 200
    			elif board[x][y].find('heima') != -1:
    				count = count + x + 400
    			elif board[x][y].find('heiche') != -1:
    				count = count + x + 900
    			elif board[x][y].find('heipao') != -1:
    				count = count + x + 450

    	return count

    def gen_moves(self, moves, depth):
    	global board 
    	red_go = False
    	if depth % 2 == 0:
    		red_go = False
    	else:
    		red_go = True

    	color = self.turn_color
    	select = self.select 
    	pos = self.select_pos[:]

    	if red_go:
    		self.turn_color = 'R'
    		for x in range(1, 11):
    			for y in range(1, 10):
    				if board[x][y] != '0':
    					self.select = board[x][y]
    					self.select_pos[0] = x
    					self.select_pos[1] = y
    					if self.select.find('bing') != -1:
    						if self.moveable(x-1, y):
    							moves.append([x,y,x-1,y])
    						if self.moveable(x, y-1):
    							moves.append([x,y,x,y-1])
    						if self.moveable(x, y+1):
    							moves.append([x,y,x,y+1])
    					if self.select.find('hongpao') != -1:
    						for i in range(1, 11):
    							if self.moveable(i,y):
    								moves.append([x,y,i,y])
    						for i in range(1, 10):
    							if self.moveable(x,i):
    								moves.append([x,y,x,i])
    					if self.select.find('hongche') != -1:
    						for i in range(1, 11):
    							if self.moveable(i,y):
    								moves.append([x,y,i,y])
    						for i in range(1, 10):
    							if self.moveable(x,i):
    								moves.append([x,y,x,i])
    					if self.select.find('hongma') != -1:
    						if self.moveable(x+1,y-2):
    							moves.append([x,y,x+1,y-2])
    						if self.moveable(x-1,y-2):
    							moves.append([x,y,x-1,y-2])
    						if self.moveable(x-1,y+2):
    							moves.append([x,y,x-1,y+2])
    						if self.moveable(x+1,y+2):
    							moves.append([x,y,x+1,y+2])
    						if self.moveable(x-2,y+1):
    							moves.append([x,y,x-2,y+1])
    						if self.moveable(x-2,y-1):
    							moves.append([x,y,x-2,y-1])
    						if self.moveable(x+2,y-1):
    							moves.append([x,y,x+2,y-1])
    						if self.moveable(x+2,y+1):
    							moves.append([x,y,x+2,y+1])
    					if self.select.find('hongxiang') != -1:
    						if self.moveable(x+2,y+2):
    							moves.append([x,y,x+2,y+2])
    						if self.moveable(x+2,y-2):
    							moves.append([x,y,x+2,y-2])
    						if self.moveable(x-2,y-2):
    							moves.append([x,y,x-2,y-2])
    						if self.moveable(x-2,y+2):
    							moves.append([x,y,x-2,y+2])
    					if self.select.find('hongshi') != -1:
    						if self.moveable(x+1,y+1):
    							moves.append([x,y,x+1,y+1])
    						if self.moveable(x+1,y-1):
    							moves.append([x,y,x+1,y-1])
    						if self.moveable(x-1,y-1):
    							moves.append([x,y,x-1,y-1])
    						if self.moveable(x-1,y+1):
    							moves.append([x,y,x-1,y+1])
    					if self.select.find('shuai') != -1:
    						if self.moveable(x+1,y):
    							moves.append([x,y,x+1,y])
    						if self.moveable(x,y-1):
    							moves.append([x,y,x,y-1])
    						if self.moveable(x-1,y):
    							moves.append([x,y,x-1,y])
    						if self.moveable(x,y+1):
    							moves.append([x,y,x,y+1])
    	else:
    		self.turn_color = 'B'
    		for x in range(1, 11):
    			for y in range(1, 10):
    				if board[x][y] != '0':
    					self.select = board[x][y]
    					print(self.select)
    					self.select_pos[0] = x
    					self.select_pos[1] = y
    					if self.select.find('zu') != -1:
    						if self.moveable(x+1, y):
    							moves.append([x,y,x+1,y])
    						if self.moveable(x, y-1):
    							moves.append([x,y,x,y-1])
    						if self.moveable(x, y+1):
    							moves.append([x,y,x,y+1])
    					if self.select.find('heipao') != -1:
    						for i in range(1, 11):
    							if self.moveable(i,y):
    								moves.append([x,y,i,y])
    						for i in range(1, 10):
    							if self.moveable(x,i):
    								moves.append([x,y,x,i])
    					if self.select.find('heiche') != -1:
    						for i in range(1, 11):
    							if self.moveable(i,y):
    								moves.append([x,y,i,y])
    						for i in range(1, 10):
    							if self.moveable(x,i):
    								moves.append([x,y,x,i])
    					if self.select.find('heima') != -1:
    						if self.moveable(x+1,y-2):
    							moves.append([x,y,x+1,y-2])
    						if self.moveable(x-1,y-2):
    							moves.append([x,y,x-1,y-2])
    						if self.moveable(x-1,y+2):
    							moves.append([x,y,x-1,y+2])
    						if self.moveable(x+1,y+2):
    							moves.append([x,y,x+1,y+2])
    						if self.moveable(x-2,y+1):
    							moves.append([x,y,x-2,y+1])
    						if self.moveable(x-2,y-1):
    							moves.append([x,y,x-2,y-1])
    						if self.moveable(x+2,y-1):
    							moves.append([x,y,x+2,y-1])
    						if self.moveable(x+2,y+1):
    							moves.append([x,y,x+2,y+1])
    					if self.select.find('heixiang') != -1:
    						if self.moveable(x+2,y+2):
    							moves.append([x,y,x+2,y+2])
    						if self.moveable(x+2,y-2):
    							moves.append([x,y,x+2,y-2])
    						if self.moveable(x-2,y-2):
    							moves.append([x,y,x-2,y-2])
    						if self.moveable(x-2,y+2):
    							moves.append([x,y,x-2,y+2])
    					if self.select.find('heishi') != -1:
    						if self.moveable(x+1,y+1):
    							moves.append([x,y,x+1,y+1])
    						if self.moveable(x+1,y-1):
    							moves.append([x,y,x+1,y-1])
    						if self.moveable(x-1,y-1):
    							moves.append([x,y,x-1,y-1])
    						if self.moveable(x-1,y+1):
    							moves.append([x,y,x-1,y+1])
    					if self.select.find('jiang') != -1:
    						if self.moveable(x+1,y):
    							moves.append([x,y,x+1,y])
    						if self.moveable(x,y-1):
    							moves.append([x,y,x,y-1])
    						if self.moveable(x-1,y):
    							moves.append([x,y,x-1,y])
    						if self.moveable(x,y+1):
    							moves.append([x,y,x,y+1])
    	self.turn_color = color
    	self.select = select
    	self.select_pos = pos[:]

    def make_a_move(self, ox, oy, dx, dy):
    	global board 
    	global red_alive
    	global black_alive 
    	if board[dx][dy] != '0':
    		if board[dx][dy] in red_alive:
    			red_alive.remove(board[dx][dy])
    		elif board[dx][dy] in black_alive:
    			black_alive.remove(board[dx][dy])
    	board[dx][dy] = board[ox][oy]
    	board[ox][oy] = '0'


    def mousePressEvent(self, e):
    	global board 
    	global red_alive
    	global black_alive
    	x = e.x() / 80.0
    	y = e.y() / 80.0
    	if (x - int(x) / 1 >= 0.5):
    		x = int(x) + 1
    	else:
    		x = int(x)
    	if (y - int(y) / 1 >= 0.5):
    		y = int(y) + 1
    	else:
    		y = int(y)
    	x = x + y
    	y = x - y
    	x = x - y
    	if self.human_move_done == False and  not(x == 0 or x == 11 or y == 0 or y == 10) :
	    	if self.select == '' and board[x][y] != '0':
	    		self.select = board[x][y]
	    		self.select_pos = [x,y]
	    		self.statusBar().showMessage(self.select)
	    	elif self.select != '':
	    		if self.moveable(x,y):
	    			self.piece_move(x, y)
	    			self.human_move_done = True
	    		else:
	    			self.select = ''
	    			self.select_pos = [0,0]
	    			self.statusBar().showMessage(" ")
		
    	if self.human_move_done and self.start == False:
    		self.statusBar().showMessage(" ")
	    	if self.end_check():
	    		self.celebrate()
	    	else:
	    		self.turn = 'A'
		    	if self.turn_color == 'R':
		    		self.turn_color = 'B'
		    	else:
		    		self.turn_color = 'R'
		    	self.vs_AI()


    def moveable(self, x, y):
    	global board 
    	global red_alive
    	global black_alive
    	if x <= 0 or y <= 0 or x >= 11 or y >= 10:
    		return False
    	if self.select_pos == [x,y]:
    		return False
    	if self.turn_color == 'B':
    		if board[x][y] in black_alive:
    			return False
    		if self.select == 'zu_0' or self.select == 'zu_1' or self.select == 'zu_2' or self.select == 'zu_3' or self.select == 'zu_4':
    			if self.select_pos[0] > x:
    				return False
    			elif self.select_pos[0] <= 5 and y != self.select_pos[1]:
    				return False
    			elif abs(y - self.select_pos[1]) + abs(x - self.select_pos[0]) > 1:
    				return False
    			else:
    				return True
    		if self.select == 'heipao_1' or self.select == 'heipao_0':
    			if board[x][y] in red_alive and self.hmn_between(self.select_pos[0], self.select_pos[1], x, y) == 1:
    				return True
    			elif board[x][y] == '0' and self.hmn_between(self.select_pos[0], self.select_pos[1], x, y) == 0:
    				return True
    			else:
    				return False
    		if self.select == 'heiche_1' or self.select == 'heiche_0':
    			if self.hmn_between(self.select_pos[0], self.select_pos[1], x, y) == 0:
    				return True
    			else:
    				return False
    		if self.select == 'heima_1' or self.select == 'heima_0':
    			if abs(y - self.select_pos[1]) == 2:
    				if abs(x - self.select_pos[0]) == 1 and board[self.select_pos[0]][int((y + self.select_pos[1])/2)] == '0':
    					return True
    			elif abs(y - self.select_pos[1]) == 1:
    				if abs(x - self.select_pos[0]) == 2 and board[int((x + self.select_pos[0])/2)][self.select_pos[1]] == '0':
    					return True
    			else:
    				return False
    		if self.select == 'heixiang_1' or self.select == 'heixiang_0':
    			if x > 5 :
    				return False
    			if abs(y - self.select_pos[1]) == 2 and abs(x - self.select_pos[0]) == 2:
    				if board[int((x + self.select_pos[0])/2)][int((y + self.select_pos[1])/2)] == '0':
    					return True
    			else:
    				return False
    		if self.select == 'heishi_1' or self.select == 'heishi_0':
    			if self.select_pos[0] == 1 or self.select_pos[0] == 3:
    				if x != 2:
    					return False
    			if self.select_pos[1] == 4 or self.select_pos[1] == 6:
    				if y != 5:
    					return False
    			if self.select_pos[0] == 2 and self.select_pos[1] == 5:
    				if x != 1 and x != 3:
    					return False
    				if y != 4 and y != 6:
    					return False
    			return True
    		if self.select == 'jiang':
    			if x > 3 or y < 4 or y > 6:
    				return False
    			else:
    				return True
    	elif self.turn_color == 'R':
    		if board[x][y] in red_alive:
    			return False
    		if self.select == 'bing_0' or self.select == 'bing_1' or self.select == 'bing_2' or self.select == 'bing_3' or self.select == 'bing_4':
    			if self.select_pos[0] < x:
    				return False
    			elif self.select_pos[0] >= 6 and y != self.select_pos[1]:
    				return False
    			elif abs(y - self.select_pos[1]) + abs(x - self.select_pos[0]) > 1:
    				return False
    			else:
    				return True
    		if self.select == 'hongpao_1' or self.select == 'hongpao_0':
    			if board[x][y] in black_alive and self.hmn_between(self.select_pos[0], self.select_pos[1], x, y) == 1:
    				return True
    			elif board[x][y] == '0' and self.hmn_between(self.select_pos[0], self.select_pos[1], x, y) == 0:
    				return True
    			else:
    				return False
    		if self.select == 'hongche_1' or self.select == 'hongche_0':
    			if self.hmn_between(self.select_pos[0], self.select_pos[1], x, y) == 0:
    				return True
    			else:
    				return False
    		if self.select == 'hongma_1' or self.select == 'hongma_0':
    			if abs(y - self.select_pos[1]) == 2:
    				if abs(x - self.select_pos[0]) == 1 and board[self.select_pos[0]][int((y + self.select_pos[1])/2)] == '0':
    					return True
    			elif abs(y - self.select_pos[1]) == 1:
    				if abs(x - self.select_pos[0]) == 2 and board[int((x + self.select_pos[0])/2)][self.select_pos[1]] == '0':
    					return True
    			else:
    				return False
    		if self.select == 'hongxiang_1' or self.select == 'hongxiang_0':
    			if x < 6 :
    				return False
    			if abs(y - self.select_pos[1]) == 2 and abs(x - self.select_pos[0]) == 2:
    				if board[int((x + self.select_pos[0])/2)][int((y + self.select_pos[1])/2)] == '0':
    					return True
    			else:
    				return False
    		if self.select == 'hongshi_1' or self.select == 'hongshi_0':
    			if self.select_pos[0] == 8 or self.select_pos[0] == 10:
    				if x != 9:
    					return False
    			if self.select_pos[1] == 4 or self.select_pos[1] == 6:
    				if y != 5:
    					return False
    			if self.select_pos[0] == 9 and self.select_pos[1] == 5:
    				if x != 8 and x != 10:
    					return False
    				if y != 4 and y != 6:
    					return False
    			return True
    		if self.select == 'shuai':
    			if x < 8 or y < 4 or y > 6:
    				return False
    			else:
    				return True


    def hmn_between(self,x,y,dx,dy):
    	global board 
    	global red_alive
    	global black_alive
    	count = 0
    	if x != dx:
    		if x > dx:
    			x = x + dx
    			dx = x - dx
    			x = x - dx
    		for num in range(x+1, dx):
    			if board[num][y] != '0':
    				count = count + 1
    		return count
    	elif y != dy:
    		if y > dy:
    			y = y + dy
    			dy = y - dy
    			y = y - dy
    		for num in range(y+1, dy):
    			if board[x][num] != '0':
    				count = count + 1
    		return count


    def piece_move(self, x, y):
    	global board 
    	global red_alive
    	global black_alive
    	if not board[x][y] == '0':
    		if board[x][y] in red_alive:
    			red_alive.remove(board[x][y])
    		else:
    			black_alive.remove(board[x][y])
    		eval('self.'+ board[x][y]).move(-1*80-30, -1*80-30)
    	board[x][y] = self.select 
    	board[self.select_pos[0]][self.select_pos[1]] = '0'
    	eval('self.'+ self.select).move(y*80-30, x*80-30)

         
if __name__ == '__main__':
     
    app = QtWidgets.QApplication(sys.argv)
    ex = Chess()
    sys.exit(app.exec_())