# Engeto_projekt_3

The third project at the Python Academy from Engeto.

# Project description

This project scrapes election data for individual districts, from the official Czech election [website](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ) and saves the retrieved data in a CSV file. 
The program accepts the URL of the page containing links to specific towns' voting results as input and generates a CSV file that lists the number of voters, attendance, valid votes, and votes per party for each town.

# Libraries used

The libraries used in the code are stored in the requirements.txt file. 

> beautifulsoup4==4.12.2
> requests==2.31.0
> bs4==0.0.1

For installation, I recommend creating a new virtual environment and Install required libraries from requirements.txt :

> $ pip install -r requirements.txt

# Usage
The election_scraper.py file is run from the command line and requires two arguments.

###Run the script with the following command:

> election_scraper.py <URL> <output_filename>

> <URL>: The URL of the page containing links to specific towns' voting results. 
> Example: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6207
> <output_filename>: The name of the CSV file where the results will be saved. 
> Example: vysledek_znojmo.csv


# Example

Voting results for Znojmo district

> 1. Argument --> https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6207
> 2. Argument --> vysledek_znojmo.csv 

### Run the following command:

> python election_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6207" „vysledek_znojmo.csv“

# Download process

> I am downloading data from URL https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6207
> I am saving data to file vysledek_znojmo.csv

# Partial output

Code,Location,Voters,Envelopes,Valid votes,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů,Národ Sobě
593729,Bantice,228,153,151,"5,29 %","0,00 %","0,00 %","8,60 %","0,00 %","2,64 %","7,94 %","2,64 %","2,64 %","2,64 %","0,00 %","0,00 %","5,96 %","0,00 %","0,66 %","22,51 %","0,00 %","0,00 %","21,19 %","0,00 %","0,00 %","0,00 %","0,66 %","15,23 %","0,66 %","0,66 %"
593737,Běhařovice,318,209,208,"2,40 %","0,00 %","0,00 %","9,61 %","0,48 %","1,44 %","7,69 %","0,48 %","0,96 %","0,00 %","0,00 %","0,48 %","5,76 %","0,00 %","0,00 %","48,55 %","0,00 %","0,00 %","13,46 %","0,00 %","0,00 %","0,00 %","0,48 %","8,17 %","0,00 %","0,00 %"
