tari=["ro", "en" ,"de", "ar","it", "hu" "es", "pt","gr", "fr","is"]
vorbe=['salut','hello','hallo', "Marhaba", 'ciao', "szia" 'ola','ola',"kalimera", 'bonjour','Shalom',]

tari_vorbe={}

for i in range (len(tari)):
    tari_vorbe[tari[i]]=vorbe[i]

print(tari_vorbe)

