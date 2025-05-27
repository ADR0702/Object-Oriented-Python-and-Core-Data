traduceri={
    "ro":{
        "no1":"introuduceti primul numar", 
        "numeric":"introduceti doar numere!!", 
        "no2": "introuduceti al 2-lea numar", 
        "op":"alegeti operatia (+,-,*,/)", 
        "reop": "alegeti doar din +.-.*,/",
        "rez":"rezultatul este:"
    },
    "en":{
       "no1": "insert first number",
       "numeric":"insert only numbers!!", 
       "no2":"insert second number", 
       "op":"choose operation (+,-,*,/)", 
       "reop": "choose from +.-.*,/",
       "rez":"the result is"
    },
    "de":{
        "no1":"erste Ziffer eingeben",
     "numerisch": "nur Zahlen eingeben!!",
        "no2": "Geben Sie die 2. Nummer ein",
        "op":"Operation auswählen (+,-,*,/)",
        "reop": "nur aus +.-.*,/ auswählen",
        "rez": "Das Ergebnis ist:"
    },
    "it":{
        "no1":"Inserire primo numero", 
        "numeric":"inserisci solo numeri", 
        "no2":"Inserire il secundo numero", 
        "op":"scegli l'operazione (+,-,*,/)", 
        "reop": "scegli solo tra +.-.*,/",
        "rez":"il resultato e"
    },
    "fr":{
        "no1": "entrez le premier numéro",
        "numeric": "entrez uniquement des chiffres !!",
        "no2": "entrez le 2ème numéro",
        "op": "choisir l'opération (+,-,*,/)",
        "reop": "choisir uniquement parmi +.-.*,/",
        "rez": "le résultat est:"
    }
}

lang = input(f"choose your language {list(traduceri.keys())}")

while lang not in traduceri.keys():
    lang=input(f"please choose from {list(traduceri.keys())}")

no1=(input(traduceri[lang]["no1"]))
while not no1.isnumeric():
    no1=(input(traduceri[lang]["numeric"]))

no1=int(no1)
print(no1)

no2=(input(traduceri[lang]["no2"]))
while not no2.isnumeric():
    no2=(input(traduceri[lang]["numeric"]))
no2=int(no2)
print(no2)

op=input(traduceri[lang]["op"])
while op not in ("+", "-", "*", "/"):
    op=input(traduceri[lang]["reop"])
if op=="+":
    rezultat=no1+no2
elif op=="-":
    rezultat=no1-no2
elif op=="*":
    rezultat=no1*no2
elif op=="/":
    rezultat=no1/no2

print(traduceri[lang]["rez"], rezultat)