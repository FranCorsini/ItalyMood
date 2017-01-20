

#tutte i points sono da considerarsi da sinistra a destra (valence) e basso alto(arousal)

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



def getColor(v,a):
	
	if v <= VALENCE_MIN:
		if a <= AROUSAL_MIN:
			#1
		elif a <= AROUSAL_MID and a > AROUSAL_MIN:
			#2
		elif a <= AROUSAL_MAX and a > AROUSAL_MID:
			#3
		elif a > AROUSAL_MAX:
			#4
	elif v <= VALENCE_MID_MIN and v > VALENCE_MIN:
		if a <= AROUSAL_MIN:
			#5
		elif a <= AROUSAL_MID_MIN and a > AROUSAL_MIN:
			#6
		elif a <= AROUSAL_MID and a > AROUSAL_MID_MIN:
			#7
		elif a <= AROUSAL_MID_MAX and a > AROUSAL_MID:
			#8
		elif a <= AROUSAL_MAX and a > AROUSAL_MID_MAX:
			#9
		elif a > AROUSAL_MAX:
			#10
	elif v <= VALENCE_MID and v > VALENCE_MID_MIN:
		if a <= AROUSAL_MIN:
			#5
		elif a <= AROUSAL_MID_MIN and a > AROUSAL_MIN:
			#11
		elif a <= AROUSAL_MID and a > AROUSAL_MID_MIN:
			#whitedown
			#12
		elif a <= AROUSAL_MID_MAX and a > AROUSAL_MID:
			#whiteup
			#13
		elif a <= AROUSAL_MAX and a > AROUSAL_MID_MAX:
			#14
		elif a > AROUSAL_MAX:
			#10
	elif v <= VALENCE_MID_MAX and v > VALENCE_MID:
		if a <= AROUSAL_MIN:
			#15
		elif a <= AROUSAL_MID_MIN and a > AROUSAL_MIN:
			#16
		elif a <= AROUSAL_MID and a > AROUSAL_MID_MIN:
			#whitedown
			#17
		elif a <= AROUSAL_MID_MAX and a > AROUSAL_MID:
			#whiteup
			#18
		elif a <= AROUSAL_MAX and a > AROUSAL_MID_MAX:
			#19
		elif a > AROUSAL_MAX:
			#20
	elif v <= VALENCE_MAX and v > VALENCE_MID_MAX:
		if a <= AROUSAL_MIN:
			#15
		elif a <= AROUSAL_MID_MIN and a > AROUSAL_MIN:
			#21
		elif a <= AROUSAL_MID and a > AROUSAL_MID_MIN:
			#22
		elif a <= AROUSAL_MID_MAX and a > AROUSAL_MID:
			#23
		elif a <= AROUSAL_MAX and a > AROUSAL_MID_MAX:
			#24
		elif a > AROUSAL_MAX:
			#20
	elif v > VALENCE_MAX:
		if a <= AROUSAL_MIN:
			#25
		elif a <= AROUSAL_MID and a > AROUSAL_MIN:
			#26
		elif a <= AROUSAL_MAX and a > AROUSAL_MID:
			#27
		elif a > AROUSAL_MAX:
			#28



|-|-----|-----|-----------|--|
|4|     10	  |		20	  |28|
|-|-----|-----|-----|-----|--|
| |     |	  |		|	  |  |
| |  9  |  14 |  19 |  24 |  |
| |     |	  |		|	  |  |		
|3|-----|-----|-----|-----|27|
| |		|	  |		|	  |  |
| |	 8	| 13  |  18	|  23 |  |		
| |		|	  |		|	  |	 |			
|-|-----|-----|-----|-----|--|		
| |		|	  |		|	  |	 |	
| |	 7	| 12  |  17 |  22 |	 |				
| |		|	  |		|	  |	 |	
|2|-----|-----|-----|-----|26|	
| |		|	  |		|	  |	 |		
| |	 6	| 11  |  16	|  21 |	 |					
| |		|	  |		|	  |	 |		
|-|-----|-----|-----|-----|--|
|1|	 	5	  |		15	  |25|			
|-|-----|-----|-----------|--|