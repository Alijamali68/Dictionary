#persian to english
dictionaryF2E=dict()
#english to persian
dictionaryE2F=dict()

def main():
	usertext=input('enter your praise: ').strip().lower().split()
	translated_text=' '
	for everyword in usertext:
		if(everyword in dictionaryE2F):
			translated_text+=' %s '%dictionaryE2F[everyword]
		elif(everyword in dictionaryF2E):
			translated_text+=' %s '%dictionaryF2E[everyword]
		else:
			language=input('%s marbot be kodam zabane:(persian/enlish)' %everyword).strip().lower()
			if(language=='persian'):
				dictionaryF2E[everyword]=input('manie %s  chi mishe: ' %everyword).strip().lower()
			elif(language=='english'):	
				dictionaryE2F[everyword]=input('what does %s mean? : ' %everyword).strip().lower()
	print(translated_text)			
main()	