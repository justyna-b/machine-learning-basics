import pandas as pd
from pandasgui import show
import matplotlib.pyplot as plt

col_list = ["id", "marka", "model", "rok_produkcji", "rodzaj_silnika", "pojemnosc_silnika", "przebieg", "cena", "wojewodztwo"]
dataset =  pd.read_csv("./data/samochody1tys.csv", usecols=col_list)

#wybierz wszystkie samochody marki Nissan, których rok produkcji jest młodszy niż 2008 rok a cena nie #przekracza 30 000, posortuj według ceny rosnąco
nissanCh = dataset[(dataset["marka"] == "Nissan") & (dataset["rok_produkcji"] > 2008) & (dataset["cena"] < 30000)].iloc[0:4].sort_values("cena")
#wybierz wszystkie samochody marki Nissan, których rok produkcji jest młodszy niż 2008 rok a cena jest #wyższa niż 30 000 i pokaż 5 pierwszych wyników, posortuj według ceny rosnąco
nissanEx = dataset[(dataset["marka"] == "Nissan") & (dataset["rok_produkcji"] > 2008) & (dataset["cena"] > 30000)].iloc[0:4].sort_values("cena")
#połącz wyżej opisane kolumny
# comparisionNissan = pd.concat([nissanCh[["model", "cena"]], nissanEx[["model", "cena"]]], axis=1, ignore_index=True)
comparisionNissan = pd.concat([nissanCh[["model", "cena"]], nissanEx[["model", "cena"]]], axis=0)
print(comparisionNissan)

#połącz wyżej opisane kolumny za pomocą merge
print("merge")
merge = pd.merge(nissanCh[["model", "cena", "marka"]], nissanEx[["model", "cena", "marka"]],  how='left', on='marka')
#dołącz nową kolumnę obrazującą stan samochodu
newCol = []
length = len(merge) 
for index in range(length):
    newCol.append("na stanie")

merge['stan'] = newCol
print(merge)

# zlicz liczbę samochodów w poszczególnych województwach i posortuj od województwa z ich największą liczbą
tempIII = dataset["wojewodztwo"].value_counts(ascending=False)

# pokaż smaochody w owjewództwie mazowieckim i posortuj je rosnąco weług ceny
tempIV = dataset[dataset["wojewodztwo"] == "Mazowieckie"]
#przedstaw ile samochodów danej marki występuje
tempV = tempIV.groupby("marka").count()
#pobierz listę dostępnych marek pomijając ich duplikaty
tempVII = tempIV["marka"].drop_duplicates()
tempVIII  = tempV["id"]
#pobierz wartości "przebieg" i oblicz ich średnią
tempVI = tempIV["przebieg"].mean()
print(tempIV.sort_values("cena", ascending = True))