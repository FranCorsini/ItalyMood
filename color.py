

#tutte i points sono da considerarsi da sinistra a destra (valence) e basso alto(arousal)
#punti per la tabella
VALENCE_MIN = 5.45
VALENCE_MID_MIN = 5.5
VALENCE_MIN_WHITE = 5.54
VALENCE_MID = 5.55
VALENCE_MAX_WHITE = 5.56
VALENCE_MID_MAX = 5.6
VALENCE_MAX = 5.7

AROUSAL_MIN = 4.0
AROUSAL_MID_MIN = 4.05
AROUSAL_MIN_WHITE = 4.09
AROUSAL_MID = 4.1
AROUSAL_MAX_WHITE = 4.11
AROUSAL_MID_MAX = 4.15
AROUSAL_MAX = 4.2

WHITE_VALENCE_MIN = 5.54
WHITE_VALENCE_MAX = 5.56
WHITE_AROUSAL_MIN = 4.09
WHITE_AROUSAL_MAX = 4.11


#colori
#per vedere a quale colore corrisponde in tabella guardare file colortable.txt
ONE = [0,0,157]
TWO = [0,0,145]
THREE = [153,0,204]
FOUR = [153,0,0]
FIVE = [0,101,51]
SIX = [0,0,204]
SEVEN = [0,51,255]
EIGHT = [153,102,255]
NINE = [255,0,0]
TEN = [153,51,255]
ELEVEN = [255,204,255]
TWELVE = [153,153,255]
THIRTEEN = [255,78,217]
FOURTEEN = [255,153,153]
FIFTEEN = [51,153,204]
SIXTEEN = [153,255,255]
SEVENTEEN = [205,255,0]
EIGHTEEN = [255,204,51]
NINETEEN = [51,204,255]
TWELVE = [255,102,51]
TWENTYONE = [51,204,51]
TWENTYTWO = [102,255,51]
TWENTYTHREE = [255,255,0]
TWENTYFOUR = [255,153,51]
TWENTYFIVE = [102,153,51]
TWENTYSIX = [102,204,51]
TWENTYSEVEN = [255,255,172]
TWENTYEIGHT = [255,51,102]

WHITE = [255,255,255]


def getColor(v,a):
	
	color = [0,0,0]

	if v <= VALENCE_MIN:
		if a <= AROUSAL_MIN:
			color = ONE
		elif a <= AROUSAL_MID and a > AROUSAL_MIN:
			color = TWO
		elif a <= AROUSAL_MAX and a > AROUSAL_MID:
			color = THREE
		elif a > AROUSAL_MAX:
			color = FOUR
	elif v <= VALENCE_MID_MIN and v > VALENCE_MIN:
		if a <= AROUSAL_MIN:
			color = FIVE
		elif a <= AROUSAL_MID_MIN and a > AROUSAL_MIN:
			color = SIX
		elif a <= AROUSAL_MID and a > AROUSAL_MID_MIN:
			color = SEVEN
		elif a <= AROUSAL_MID_MAX and a > AROUSAL_MID:
			color = EIGHT
		elif a <= AROUSAL_MAX and a > AROUSAL_MID_MAX:
			color = NINE
		elif a > AROUSAL_MAX:
			color = TEN
	elif v <= VALENCE_MID and v > VALENCE_MID_MIN:
		if a <= AROUSAL_MIN:
			color = FIVE
		elif a <= AROUSAL_MID_MIN and a > AROUSAL_MIN:
			color = ELEVEN
		elif a <= AROUSAL_MID and a > AROUSAL_MID_MIN:
			if v <= WHITE_VALENCE_MAX and WHITE_VALENCE_MIN and a <= WHITE_AROUSAL_MAX and a > WHITE_AROUSAL_MIN:
				color = WHITE
			else:
				color = TWELVE
		elif a <= AROUSAL_MID_MAX and a > AROUSAL_MID:
			if v <= WHITE_VALENCE_MAX and WHITE_VALENCE_MIN and a <= WHITE_AROUSAL_MAX and a > WHITE_AROUSAL_MIN:
				color = WHITE
			else:
				color = THIRTEEN
		elif a <= AROUSAL_MAX and a > AROUSAL_MID_MAX:
			color = FOURTEEN
		elif a > AROUSAL_MAX:
			color = TEN
	elif v <= VALENCE_MID_MAX and v > VALENCE_MID:
		if a <= AROUSAL_MIN:
			color = FIFTEEN
		elif a <= AROUSAL_MID_MIN and a > AROUSAL_MIN:
			color = SIXTEEN
		elif a <= AROUSAL_MID and a > AROUSAL_MID_MIN:
			if v <= WHITE_VALENCE_MAX and WHITE_VALENCE_MIN and a <= WHITE_AROUSAL_MAX and a > WHITE_AROUSAL_MIN:
				color = WHITE
			else:
				color = SEVENTEEN
		elif a <= AROUSAL_MID_MAX and a > AROUSAL_MID:
			if v <= WHITE_VALENCE_MAX and WHITE_VALENCE_MIN and a <= WHITE_AROUSAL_MAX and a > WHITE_AROUSAL_MIN:
				color = WHITE
			else:
				color = EIGHTEEN
		elif a <= AROUSAL_MAX and a > AROUSAL_MID_MAX:
			color = NINETEEN
		elif a > AROUSAL_MAX:
			color = TWENTY
	elif v <= VALENCE_MAX and v > VALENCE_MID_MAX:
		if a <= AROUSAL_MIN:
			color = FIFTEEN
		elif a <= AROUSAL_MID_MIN and a > AROUSAL_MIN:
			color = TWENTYONE
		elif a <= AROUSAL_MID and a > AROUSAL_MID_MIN:
			color = TWENTYTWO
		elif a <= AROUSAL_MID_MAX and a > AROUSAL_MID:
			color = TWENTYTHREE
		elif a <= AROUSAL_MAX and a > AROUSAL_MID_MAX:
			color = TWENTYFOUR
		elif a > AROUSAL_MAX:
			color = TWENTY
	elif v > VALENCE_MAX:
		if a <= AROUSAL_MIN:
			color = TWENTYFIVE
		elif a <= AROUSAL_MID and a > AROUSAL_MIN:
			color = TWENTYSIX
		elif a <= AROUSAL_MAX and a > AROUSAL_MID:
			color = TWENTYSEVEN
		elif a > AROUSAL_MAX:
			color = TWENTYEIGHT

	#debug
	with open("outputcolor.txt","a") as out: 
	    out.write(str(datetime.now()))
	    out.write('\n')
	    out.write(str(v))
	    out.write('\n')
	    out.write(str(a))
	    out.write('\n')
	    out.write(str(color))

	return color


