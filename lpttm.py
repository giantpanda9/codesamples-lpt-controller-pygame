# -*- coding: cp1251 -*-
import pygame, ctypes
from pygame.locals import *
from sys import exit
pygame.init()
screen = pygame.display.set_mode((640, 500), 0, 32)
pygame.display.set_caption("LPT Conrol Center")



	
def mainwindow():
	txrx=[]
	txrxR=[]
	prmR=[]
	prdR=[]
	rct1lst=[]
	aColor=[]
	bColor=[]
	paColor=[]
	pbColor=[]
	sqlaColor=[]
	sqlbColor=[]
	wRect = 100
	hRect =26
	outX=70
	n=0
	read=0
	prm=0
	prd=0
	sql=0
	prm1=0
	prd1=0
	sql1=0
	out=0
	prmON = []
	prdON = []
	clock=pygame.time.Clock()
	font = pygame.font.SysFont('Arial', 20, True, True)
	res1Color0=0
	res2Color0=0
	res3Color0=0
	res1Color1=255
	res2Color1=255
	res3Color1=255
	txrxColor = []
	prdColor=0
	prdColorBackup=[]
	prmColorBackup=[]
	prdOK1=0
	circONColor=0
	circOFFColor=255
	GoodByeColor=0
	for i in xrange(0,8):
		paColor.append(255)
		pbColor.append(255)
	for i in xrange(0,15):
		txrx.append(i+1)
		prmON.append('[]')
		prdON.append('[]')
		aColor.append(0)
		bColor.append(0)
		sqlaColor.append(0)
		sqlbColor.append(0)
		txrxColor.append(0)
		prdColorBackup.append(0)
		prmColorBackup.append(0)
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((0, 0, 0))
	pygame.key.set_repeat(1, 1)
	ctypes.windll.inpout32.Out32(0x37a, 1)
	while 1:
		scx, scy = pygame.mouse.get_pos()
		cursorRect=pygame.Rect(scx,scy, 5, 5)	
		screen.blit(background, (0,0))
		
		pttT1 = font.render(unicode('ПРМ', 'cp1251'), 1, (0, 255, 0))
		textpos = pttT1.get_rect()
		textpos.centerx=170
		textpos.centery=10
		background.blit(pttT1, textpos)
		sndT1 = font.render(unicode('ПРД', 'cp1251'), 1, (0, 255, 0))
		textpos = sndT1.get_rect()
		textpos.centerx=270
		textpos.centery=10
		background.blit(sndT1, textpos)
		sqlT1 = font.render(unicode('НЧ', 'cp1251'), 1, (0, 255, 0))
		textpos = sqlT1.get_rect()
		textpos.centerx=370
		textpos.centery=10
		background.blit(sqlT1, textpos)
		
		res1 = font.render(unicode('СбросПРМ', 'cp1251'), 1, (res1Color0, res1Color1, 0))
		textpos = res1.get_rect()
		textpos.centerx=90
		textpos.centery=480
		background.blit(res1, textpos)
		res1Rect = pygame.Rect(10, 480, res1.get_width()+30, res1.get_height()+30)
		res1Rect.normalize()
		res2 = font.render(unicode('СбросПРД', 'cp1251'), 1, (res2Color0, res2Color1, 0))
		textpos = res2.get_rect()
		textpos.centerx=300
		textpos.centery=480
		background.blit(res2, textpos)
		res2Rect = pygame.Rect(220, 480, res2.get_width()+30, res2.get_height()+30)
		
		res3 = font.render(unicode('Общий Сброс', 'cp1251'), 1, (res3Color0, res3Color1, 0))
		textpos = res3.get_rect()
		textpos.centerx=500
		textpos.centery=480
		background.blit(res3, textpos)
		
		res3Rect = pygame.Rect(420, 480, res3.get_width()+40, res3.get_height()+30)	
		
		for i in xrange (0, len(txrx)):
			
			
			
			txrxT = font.render(str(txrx[i]), 1, (txrxColor[i], 255, 0))
			textpos = txrxT.get_rect()
			textpos.centerx=outX
			textpos.centery=(i+1)*30
			background.blit(txrxT, textpos)
			txrxR.append(pygame.Rect(textpos.centerx, textpos.centery, wRect, hRect))
			
			prmT = font.render(unicode(prmON[i], 'cp1251'), 1, (aColor[i], 255, 0))
			textpos = prmT.get_rect()
			textpos.centerx=170
			textpos.centery=(i+1)*30
			background.blit(prmT, textpos)
			prmR.append(pygame.Rect(textpos.centerx, textpos.centery, wRect, hRect))
			
			prdT = font.render(unicode(prdON[i], 'cp1251'), 1, (bColor[i], 255, 0))
			textpos = prdT.get_rect()
			textpos.centerx=270
			textpos.centery=(i+1)*30
			background.blit(prdT, textpos)
			prdR.append(pygame.Rect(textpos.centerx, textpos.centery, wRect, hRect))
			
			sqlT = font.render(unicode('[]', 'cp1251'), 1, (sqlaColor[i],sqlbColor[i], 0))
			textpos = sqlT.get_rect()
			textpos.centerx=370
			textpos.centery=(i+1)*30
			background.blit(sqlT, textpos)
			
			
			
		for i in xrange (0,8):
			
			palka = font.render(unicode('I', 'cp1251'), 1, (paColor[i], pbColor[i], 0))
			textpos = palka.get_rect()
			textpos.centerx=(i*20+400)
			textpos.centery=30
			background.blit(palka, textpos)
			
		prdOK = font.render(unicode('PTT', 'cp1251'), 1, (prdColor, 255, 0))
		textpos = prdOK.get_rect()
		textpos.centerx=450
		textpos.centery=70
		background.blit(prdOK, textpos)
		prdOKRect	= pygame.Rect(440,70, prdOK.get_width()+50, prdOK.get_height()+30)
			
		circON = font.render(unicode('ЦиркулярВКЛ', 'cp1251'), 1, (circONColor, 255, 0))
		textpos = circON.get_rect()
		textpos.centerx=490
		textpos.centery=150
		background.blit(circON, textpos)
		circONRect	= pygame.Rect(420,150, circON.get_width()+10, circON.get_height()+30)
		
		circOFF = font.render(unicode('ЦиркулярВЫКЛ', 'cp1251'), 1, (circOFFColor, 255, 0))
		textpos = circOFF.get_rect()
		textpos.centerx=490
		textpos.centery=250
		background.blit(circOFF, textpos)
		circOFFRect = pygame.Rect(420,250, circOFF.get_width()+50, circON.get_height()+30)
		
		GoodBye = font.render(unicode('Выход', 'cp1251'), 1, (GoodByeColor, 255, 0))
		textpos = GoodBye.get_rect()
		textpos.centerx=490
		textpos.centery=350
		background.blit(GoodBye, textpos)
		GoodByeRect = pygame.Rect(420,350, GoodBye.get_width()+50, GoodBye.get_height()+30)
		if prdOK1==1:
	
			if bColor[n] == 255:
				prd = 32
		
			else:
				prd = 0
			
				
			
		
		if aColor[n] == 255:
			prm = 16
			sql=64
			
		else:
			prm = 0
			sql=0
	
		
	
		
		out = n + prm + prd+sql
		
		ctypes.windll.inpout32.Out32(0x378, out)		 
		read = int(ctypes.windll.inpout32.Inp32(0x378)) 
		read1 = int(ctypes.windll.inpout32.Inp32(0x378)) 
		
		read=read-prm-prd-sql
		
		prm1 = read1-read-prd-sql
		prd1= read1-read-prm-sql
		sql1= read1-read-prd-prm
		
		#print sql1
		pbColor[0]=255
		pbColor[1]=255
		pbColor[2]=255
		pbColor[3]=255
		pbColor[4]=255
		pbColor[5]=255
		pbColor[6]=255
		for i in xrange(0,15):
			sqlaColor[i]=0
			sqlbColor[i]=0
			#txrxColor[i] = 0	
		if sql1==64:
			pbColor[6]=0
			if aColor[n]==255:
				sqlaColor[n]=255
				sqlbColor[n]=0
				
				
			
		if prd1==32:
			pbColor[5]=0
			try:
				txrxColor[n] = 255
			except:
				pass
		if prm1==16:
			pbColor[4]=0
			
		if read == 1:
			pbColor[0]=0
	
		if read == 2:
			pbColor[1]=0
		
		if read == 3:
			pbColor[0]=0
			pbColor[1]=0
	
		if read == 4:
			pbColor[2]=0
	
		if read == 5:
			pbColor[0]=0
			pbColor[2]=0
	
		if read == 6:
			pbColor[1]=0
			pbColor[2]=0
		
		if read == 7:
			pbColor[0]=0
			pbColor[1]=0
			pbColor[2]=0
		
		if read == 8:
			pbColor[3]=0
		
		if read == 9:
			pbColor[0]=0
			pbColor[3]=0
		
		if read == 10:
			pbColor[1]=0
			pbColor[3]=0
		
		if read == 11:
			pbColor[0]=0
			pbColor[1]=0
			pbColor[3]=0
		
		if read == 12:
			pbColor[2]=0
			pbColor[3]=0
		
		if read == 13:
			pbColor[0]=0
			pbColor[2]=0
			pbColor[3]=0
		
		if read == 14:
			pbColor[1]=0
			pbColor[2]=0
			pbColor[3]=0
		
		if read == 15:
			pbColor[0]=0
			pbColor[1]=0
			pbColor[2]=0
			pbColor[3]=0
	
		#print read
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				ctypes.windll.inpout32.Out32(0x37a, 0)
				print unicode('Спасибо за использование программы. До Свидания!','сз1251')
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					
					prdOK1=1
					
			if event.type==pygame.KEYUP:
				#for i in xrange(0,15):
					#txrxColor[i] = 0
				prd=0
				prdOK1=0
			if event.type == pygame.MOUSEBUTTONDOWN:
				# № 1 - это Выход
				b1,b2,b3=pygame.mouse.get_pressed()
				
			
				
				if b1==1:								
					for i in xrange(0,len(txrx)):
						if cursorRect.collidelist(prmR)==i:
							aColor[i] = 255
							bColor[i] = 0
							
		
					for i in xrange(0,len(txrx)):
						if cursorRect.collidelist(prdR)==i:
							aColor[i] = 0
							bColor[i] = 255
				
					if cursorRect.colliderect(res1Rect) == 1:
						res1Color0=255
						res1Color1=0
						for i in xrange(0,14):
							aColor[i] = 0
					
					if cursorRect.colliderect(res2Rect) == 1:
						res2Color0=255
						res2Color1=0
						for i in xrange(0,14):
							bColor[i] = 0
							
					if cursorRect.colliderect(res3Rect) == 1:
						res3Color0=255
						res3Color1=0
						for i in xrange(0,14):
							aColor[i] = 0
							bColor[i] = 0
					if cursorRect.colliderect(prdOKRect) == 1:
						prdColor=255
						prdOK1=1
						
			
				
						
							
					if cursorRect.colliderect(circONRect) == 1:
						circOFFColor=0
						circONColor=255
						
						for i in xrange(0,15):
							prdColorBackup[i] = bColor[i]
							prmColorBackup[i] = aColor[i]
							bColor[i]=255
							aColor[i]=0
							
					if cursorRect.colliderect(circOFFRect) == 1:
						circOFFColor=255
						circONColor=0	
						
						for i in xrange(0,15):
								bColor[i]=prdColorBackup[i]
								aColor[i]=prmColorBackup[i]
								
							
					if cursorRect.colliderect(GoodByeRect) == 1:	
						GoodByeColor=255
						ctypes.windll.inpout32.Out32(0x37a, 0)
						#print unicode('Спасибо за использование программы. До Свидания!','сз1251')
						#exit()	
				
			
			if event.type == pygame.MOUSEBUTTONUP:
						
				res1Color0=0
				res2Color0=0
				res3Color0=0
				res1Color1=255
				res2Color1=255
				res3Color1=255
				#GoodByeColor=0
				prdColor=0
				prdOK1=0
				prd = 0
				if cursorRect.colliderect(GoodByeRect) == 1:	
					GoodByeColor=0
						
					print unicode('Спасибо за использование программы. До Свидания!','сз1251')
					exit()
				
				for i in xrange(0,15):
					txrxColor[i] = 0
						
		if n != len(txrx)-1:
			n=n+1
		else:
			n=0
				
			
		
		pygame.display.update()
		clock.tick(30)
	return 0

mainwindow()