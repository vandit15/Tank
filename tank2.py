#imports
import pygame
import time
import random


#frame initialisation
pygame.init()

#colours
white = (255,255,255)
black = (0,0,0)
red = (150,0,0)
medium_red = (200,0,0)
light_red = (255,0,0)
green = (0,150,0)
light_green = (0,255,0)
blue = (0,0,255)
yellow = (175,175,0)
light_yellow=(255,255,0)
brown = (205,133,63)

#sounds
sound = pygame.mixer.Sound("bomb.wav")

#vriables
display_width = 700
display_height = 500
fps = 20
clock = pygame.time.Clock()
mainTankX = random.randrange(int(display_width*0.7),int(display_width*1))
mainTankY = display_height*0.9
enemy_tankX = display_width*0.1
enemy_tankY = display_height*0.9
tankWidth = 40
tankBaseHeight = 20
turretWidth=5
block_size = 5

#main screen display variable
gamedisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Tanks')
#icon = pygame.image.load('apple.png')
#pygame.display.set_icon(icon)

#fonts
smallFont = pygame.font.Font("angrybirds.ttf",20)
mediumFont = pygame.font.Font("angrybirds.ttf",25) 
largeFont = pygame.font.Font("angrybirds.ttf",30)

#images
img = pygame.image.load('backgrnd.jpg')
#imgapple = pygame.image.load('apple.png')

		
def score(score):
	text = smallFont.render("Score: "+str(score),True,black)
	gamedisplay.blit(text,[10,10])

def text_objects(text,color,size):
	if size == "small":
		textSurface = smallFont.render(text,True,color)
	if size == "medium":
		textSurface = mediumFont.render(text,True,color)
	if size == "large":
		textSurface = largeFont.render(text,True,color)
	return textSurface, textSurface.get_rect()
	
def text_to_button(msg,color,buttonx,buttony,button_width,button_height,size="small"):
	textSurf, textRect = text_objects(msg,color,size)
	textRect.center = buttonx+button_width/2,buttony+button_height/2
	gamedisplay.blit(textSurf,textRect)
		
		
def text_on_screen(msg,color,y_displace=0,size = "small"):
	textSurf, textRect = text_objects(msg,color,size)
	#screen_text = font.render(msg,True,color)
	#gamedisplay.blit(screen_text,[display_width/2-150,display_height/2])
	textRect.center = (display_width/2),(display_height/2)+y_displace
	gamedisplay.blit(textSurf,textRect)
	
def button(text,x,y,width,height,active_color,inactive_color,action = "none"):
	cur = pygame.mouse.get_pos()
	click =pygame.mouse.get_pressed()
	flag=0
	if x+width > cur[0] > x and y + height > cur[1] > y:
		pygame.draw.rect(gamedisplay,active_color,(x,y,width,height))
		if click[0] == 1 and action!="none":
			if action == "play":
				flag=1
			if action == "controls":
				flag=1
			if action == "quit":
				quit()
		
	else:
		pygame.draw.rect(gamedisplay,inactive_color,(x,y,width,height))
	text_to_button(text,black,x,y,width,height)
	return flag

#draws tank
def tank(x,y,turpos):

	possibleTurrets = [
						(x-24,y-4),
						(x-23,y-6),
						(x-22,y-8),
						(x-20,y-10),
						(x-18,y-12),
						(x-16,y-14),
						(x-15,y-15),
						(x-13,y-17),
						(x-12,y-18),
						]
	
	x = int(x)
	y = int(y)
	pygame.draw.circle(gamedisplay,black,(x,y),12)
	pygame.draw.rect(gamedisplay,black,(int(x-tankWidth/2),y,tankWidth,tankBaseHeight))
	pygame.draw.line(gamedisplay,black,(x,y),possibleTurrets[turpos],turretWidth)
	for i in range(7):
		pygame.draw.circle(gamedisplay,black,(x-tankWidth/2+5*i+5,y+tankBaseHeight),5)
	
	return possibleTurrets[turpos] 

def enemy_tank(x,y,turpos):

	possibleTurrets = [
						(x+24,y-4),
						(x+23,y-6),
						(x+22,y-8),
						(x+20,y-10),
						(x+18,y-12),
						(x+16,y-14),
						(x+15,y-15),
						(x+13,y-17),
						(x+12,y-18),
						]
	
	x = int(x)
	y = int(y)
	pygame.draw.circle(gamedisplay,black,(x,y),12)
	pygame.draw.rect(gamedisplay,black,(int(x-tankWidth/2),y,tankWidth,tankBaseHeight))
	pygame.draw.line(gamedisplay,black,(x,y),possibleTurrets[turpos],turretWidth)
	for i in range(7):
		pygame.draw.circle(gamedisplay,black,(x-tankWidth/2+5*i+5,y+tankBaseHeight),5)
	
	return possibleTurrets[turpos] 
		
def showcontrols():
	flag1=0
	gcontrol = True
	while gcontrol:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		#gamedisplay.blit(img,(0,0))
		gamedisplay.fill(white)
		text_on_screen("Fire:						Spacebar",black,-30,size = "small")
		text_on_screen("Move Turret:				UP and DOWN arrow keys",black,0,size = "small")
		text_on_screen("Move Tank:					LEFT nd RIGHT arrow keys",black,30,size = "small")
		text_on_screen("Increase Power:				A",black,60,size = "small")
		text_on_screen("Decrease Power: 			S ",black,90,size="small")
		#text_on_screen("Press SpaceBar to start playing or Q to quit",red,100,size = "medium")
		
		flag1 =button("play",500/3,400,75,50,green,light_green,"play")
		button("quit",100+500*2/3,400,75,50,red,light_red,"quit")
		pygame.display.update()
		if flag1!=0:
			break
	
	if flag1 == 1:
		return
		
def barrierRandomfuction(barrierHeight):
	upperHeight = random.randrange(int(barrierHeight*0.2),int(barrierHeight*0.6))
	

def barrier(barrierXLocation,barrierHeight,upperHeight):
	pygame.draw.rect(gamedisplay,black,(barrierXLocation,barrierHeight,50,barrierHeight))
	#pygame.draw.rect(gamedisplay,black,(barrierXLocation,0,50,upperHeight))
		
def explosion(x,y):
	explode = True
	sound.play()
	while explode:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
		startPoint = x,y
		
		colourChoices = [red,light_yellow,light_red,yellow]
		
		magnitude = 10
		while magnitude < 20:
			exploding_bit_x = x + random.randrange(-1*magnitude,magnitude)
			exploding_bit_y = y + random.randrange(-1*magnitude,magnitude)
			pygame.draw.circle(gamedisplay,colourChoices[random.randrange(0,4)],(exploding_bit_x,exploding_bit_y),5)
			magnitude+=1
			
			pygame.display.update()
			clock.tick(100)
		explode = False	
			
def fireShell(xy,tankx,tanky,turpos,gunpower,etankx):
	damage=0
	startingShell = []
	startingShell.append(xy[0])
	startingShell.append(xy[1])
	fire = True
	while fire == True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		pygame.draw.circle(gamedisplay,medium_red,(int(startingShell[0]),int(startingShell[1])),5)
		startingShell[0] -= (10 - turpos)*2
		startingShell[1] += int((((startingShell[0]-xy[0])*0.015/float((float(gunpower)/50)))**2)-(turpos+turpos/12))
		
		
		if startingShell[1] > display_height-ground_height:
			hit_x = int(startingShell[0]*(display_height-ground_height)/float(startingShell[1]))
			hit_y = display_height-ground_height
			if etankx-10 < hit_x < etankx + 10:
				damage = 25
			if etankx - 20 < hit_x < etankx-10 or etankx+10 <hit_x < etankx+20:
				damage = 15
			if etankx - 30 < hit_x < etankx-20 or etankx+20 <hit_x < etankx+30:
				damage = 5
			explosion(hit_x,hit_y)
			fire = False
		if startingShell[0] <= barrierXLocation + 50 and startingShell[0] > barrierXLocation:
			if startingShell[1] >= display_height - barrierHeight:
				explosion(int(startingShell[0]),int(startingShell[1]))
				fire = False
		pygame.display.update()
		clock.tick(100)
	return damage

def e_fireShell(xy,tankx,tanky,turpos,currentPower,ptankx,ptanky):
	damage=0
	currentPower = 1
	power_found = False
	while not power_found:
		if currentPower > 100:
			power_found = True
		currentPower +=1
		startingShell = []
		startingShell.append(xy[0])
		startingShell.append(xy[1])
		fire = True
		while fire == True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			#pygame.draw.circle(gamedisplay,medium_red,(int(startingShell[0]),int(startingShell[1])),5)
			startingShell[0] += (10 - turpos)*2
			startingShell[1] += int((((startingShell[0]-xy[0])*0.015/float((float(currentPower)/50)))**2)-(turpos+turpos/12))
			
			
			if startingShell[1] > display_height-ground_height:
				hit_x = int(startingShell[0]*(display_height-ground_height)/float(startingShell[1]))
				hit_y = display_height-ground_height
				if ptankx-30<hit_x < ptankx+30:
					power_found = True
				#explosion(hit_x,hit_y)
				fire = False
			if startingShell[0] <= barrierXLocation + 50 and startingShell[0] > barrierXLocation:
				if startingShell[1] >= display_height - barrierHeight:
					#explosion(int(startingShell[0]),int(startingShell[1]))
					fire = False
	
	
	randomPower = random.randrange(currentPower,int(currentPower*1.1))
	currentPower=randomPower
	startingShell = []
	startingShell.append(xy[0])
	startingShell.append(xy[1])
	fire = True
	while fire == True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		pygame.draw.circle(gamedisplay,medium_red,(int(startingShell[0]),int(startingShell[1])),5)
		startingShell[0] += (10 - turpos)*2
		startingShell[1] += int((((startingShell[0]-xy[0])*0.015/float((float(currentPower)/50)))**2)-(turpos+turpos/12))
		
		
		if startingShell[1] > display_height-ground_height:
			hit_x = int(startingShell[0]*(display_height-ground_height)/float(startingShell[1]))
			hit_y = display_height-ground_height
			#hit_x = hit_x  + random.randrange(0,40)
			explosion(hit_x,hit_y)
			if ptankx-10 < hit_x < ptankx + 10:
				damage = 25
			if ptankx -20 < hit_x < ptankx-10 or ptankx+10 <hit_x < ptankx+20:
				damage = 15
			if ptankx -30 < hit_x < ptankx-20 or ptankx+20 <hit_x < ptankx+30:
				damage = 5
			fire = False
		if startingShell[0] <= barrierXLocation + 50 and startingShell[0] > barrierXLocation:
			if startingShell[1] >= display_height - barrierHeight:
				explosion(int(startingShell[0]),int(startingShell[1]))
				fire = False
		pygame.display.update()
		clock.tick(100)
	return damage
		
def powerDisplay(firepower):
	text_on_screen("Power:"+str(firepower)+"%",black,-225,size = "small")

def health_bar(phealth,ehealth):
	if phealth>=75:
		phealth_colour = green
	elif phealth>=50:
		phealth_colour = yellow
	elif phealth>0:
		phealth_colour = red
	else:
		return
	
	if ehealth>=75:
		ehealth_colour = green
	elif ehealth>=50:
		ehealth_colour = yellow
	elif ehealth>0:
		ehealth_colour = red
	else:
		return
	pygame.draw.rect(gamedisplay,phealth_colour,(display_width-150,50,phealth,25))
	pygame.draw.rect(gamedisplay,ehealth_colour,(50,50,ehealth,25))
	pygame.draw.rect(gamedisplay,red,(45,45,110,35),4)
	pygame.draw.rect(gamedisplay,red,(display_width-155,45,110,35),4)
	
def intro():
	flag1=0
	flag2=0
	intro = True
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gamedisplay.blit(img,(0,0))
		#text_on_screen("Welcome To Tanks :) ",red,-100,size="large")
		#text_on_screen("the objective of the game is to eat the apples",black,-30,size = "small")
		#text_on_screen("The more you eat the more you lengthen",black,-5,size = "small")
		#text_on_screen("Do not eat yourself or hit the walls :D",black,20,size = "small")
		#text_on_screen("Press SpaceBar to start playing or Q to quit",red,100,size = "medium")
		
		flag1 =button("play",100,400,100,50,green,light_green,"play")
		flag2=button("controls",300,400,100,50,yellow,light_yellow,"controls")
		button("quit",500,400,100,50,red,light_red,"quit")
		pygame.display.update()
		if flag1!=0 or flag2!=0:
			break
	if flag2==1:
		showcontrols()
	if flag1 == 1:
		return
	
intro()	
gameLoop = True
line = 1;

while gameLoop == True:
	#variables across one loop
	gameExit = False
	gameOver = False
	gameWin = False
	flag1=0
	flag2=0
	lead_x_change = 0
	lead_y_change = 0
	turpos = 0
	enemyTurpos = 8
	currentX = mainTankX
	barrierXLocation = (display_width/2) + random.randint(-0.2*display_width,0.2*display_width)
	barrierHeight = display_height*0.5
	fire_power = 50
	power_change = 0
	ground_height = 25
	phealth = 100
	ehealth = 100
	upperHeight = random.randrange(int(barrierHeight*0.1),int(barrierHeight*0.3))
#main game loop
	while not gameExit:
		while gameOver == True:
			gamedisplay.fill(white)
			text_on_screen("YOU LOSE  :(",red,-50,size="large")
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			flag1 =button("Play Again",100,400,150,50,green,light_green,"play")
			button("quit",500,400,100,50,red,light_red,"quit")
			pygame.display.update()
			if flag1 == 1:
				gameOver = False
				gameWin = False
				break
		if flag1 == 1:
			break
		
		while gameWin == True:
			gamedisplay.fill(white)
			text_on_screen("YOU WIN  :(",red,-50,size="large")
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			flag2 =button("Play Again",100,400,150,50,green,light_green,"play")
			button("quit",500,400,100,50,red,light_red,"quit")
			pygame.display.update()
			if flag2 == 1:
				gameOver = False
				gameWin = False
				break
		if flag2 == 1:
			break
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					lead_x_change =-block_size
					
				elif event.key == pygame.K_RIGHT:
					lead_x_change =block_size
					
				elif event.key == pygame.K_UP:
					turpos+=1

				elif event.key == pygame.K_DOWN:
					turpos-=1

				elif event.key == pygame.K_SPACE:
					edamage=fireShell(gun,currentX,mainTankY,turpos,fire_power,enemy_tankX)
					ehealth-=edamage
					w = random.randrange(0,2)
					t = random.randrange(1,10)
					for v in range(t):
						if w == 1:
							if enemy_tankX+5 < barrierXLocation:
								enemy_tankX+=5
						if w==0:
							if enemy_tankX-5 > 0:
								enemy_tankX-=5
					gamedisplay.fill(white)
					fire_power += power_change
					powerDisplay(fire_power)
					#upperHeight = barrierRandomfuction(barrierHeight)
					barrier(barrierXLocation,barrierHeight,upperHeight)
					health_bar(phealth,ehealth)
					pygame.draw.rect(gamedisplay,green,(0,display_height-ground_height,display_width,ground_height))
					gun =tank(currentX,mainTankY,turpos)
					enemygun = enemy_tank(enemy_tankX,enemy_tankY,enemyTurpos)
					pygame.display.update()
					clock.tick(fps)	
					
					#time.sleep(2)
					if ehealth>0:
						pdamage=e_fireShell(enemygun,currentX,mainTankY,enemyTurpos,fire_power,currentX,mainTankY)
						phealth-=pdamage
				elif event.key == pygame.K_a:
					power_change = +1
				elif event.key == pygame.K_s:
					power_change = -1 
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					lead_x_change = 0
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					changeTur = 0
				if event.key == pygame.K_a or event.key == pygame.K_s:
					power_change =0
		if phealth<=0: 
			gameOver = True
			continue
		if ehealth<=0:
			gameWin = True
			continue
		currentX +=lead_x_change
		if turpos > 8:
			turpos = 8
		elif turpos <0:
			turpos = 0
		gamedisplay.fill(white)
		fire_power += power_change
		if fire_power > 100:
			fire_power = 100
		if fire_power < 0:
			fire_power = 0
		powerDisplay(fire_power)
		barrier(barrierXLocation,barrierHeight,upperHeight)
		health_bar(phealth,ehealth)
		pygame.draw.rect(gamedisplay,green,(0,display_height-ground_height,display_width,ground_height))
		if currentX - tankWidth/2 < barrierXLocation + 50:
			currentX +=5
		gun =tank(currentX,mainTankY,turpos)
		enemygun = enemy_tank(enemy_tankX,enemy_tankY,enemyTurpos)
		textSurf, textRect = text_objects("FIRE!!!",red,"medium")
		textRect.center = display_width-100,150
		gamedisplay.blit(textSurf,textRect)
		pygame.display.update()
		clock.tick(fps)	

