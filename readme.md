This is a custom readme file

so klik na kopcheto "Clear Data" preku ajax povik so 
metodot get se povikuva rutata clear_data i dokolku povikot 
e uspeshen se izvrshuva funkcijata.
vo funkcijata se konektirame so bazata semos_companies_data.db
vrz konektiranata baza se izvrshuva  SELECT * FROM companies 
vrz name kolonata se izvrshuva funkcijata transformString vo 
koja se izvrshuvaat slednite prochistuvanja na stringovite:

Прoчистување на имињата на компаниите од несакани 
карактери: запирки и цел текст по запирките, загради и текстот 
во нив, наводници, тире кога не е дел од името на компанијата 
и сл.
Прочистување за имињата на компаниите да бидат без нивниот 
легален ентитет: LIMITED, LTD., ltd. Limited, limited и сл.
Името да биде самo со пoчетни големи букви: пр. AGILE BUSINESS 
CONSULTANTS треба да биде Agile Business Consultants

novo dobienite stringovi se zachuvuvaat vo kolonata company_name_cleaned 
po zavrshuvanje na celata funkcija ni se ispishuva "Finished transforming 
the data and writing to SQL database"



so klik na kopcheto "Insert Data" preku ajax povik so 
metodot get se povikuva rutata insert_to_mongo i dokolku povikot 
e uspeshen se izvrshuva funkcijata.
vo funkcijata se konektirame so bazata semos_companies_data.db
vrz konektiranata baza se izvrshuva "SELECT * FROM companies"
sledno se brishe kolonata 'name'
sledno go startuvame MongoDB na portata 27017
sledno ja loadirame semos_database pa od nejze ja zimame 
kolekcijata companies
sledno so for prochistenite iminja gi zimame od company_name_cleaned
kolonata i gi postavuvame kako kluchevi pa novo prochistenite redici
so kluch i vrednost gi vmetnuvame vo pomoshnata niza final_list pa 
taa niza ja skladirame vo kolekcijata 
pri zavrshuvanjeto na funkcijata se vrakja odnosno prikazhuva "Finished 
inserting into MongoDB database"


so klik na kopcheto "Show Data" ne prenesuva na rutata show_data i vo 
pozadina se izvrshuva funkcijata show_mongo_results i go startuvame 
MongoDB na portata 27017
od bazata semos_database se zima kolekcijata companies i rezultatot go
limitirame na 20 prikazi 
vo forot vo pomoshnata niza lst gi doddavame podatocite koi se pretvoreni
vo dictionary



