# scripts
A collection from all of my scripts

## Guess the Number (CPU)
A small game which let you guess which number the program generated. If you're wrong the program says higher/lower.
### How to use
1. Start `guess-the-number.py` (or `guess-the-number-CPU.py` for CPU guessing)
2. Follow the instructions

## Sendmail
A little script like my other [sendmail](https://github.com/MelanX/sendmail/) script. One difference: You can go step-by-step through each point.
### How to use
0. Edit `sendmail.py` in the `Default settings` area (optional)
1. Start `sendmail.py`
2. Follow the instructions

## Pollenflug-Logger
A script which uses open source data by DWD - Deutscher Wetterdienst. It's logging the data for each region.
### How to use
0. Select your region in line 56 in `pollenflug-logger.py` if needed (see table below)
1. Start `pollenflug-logger.py` every day after 11am (MESZ)
2. See your data in `data/` and the backups after each month in `backup/`

| Region ID | Region Name                                                      |
|:---------:|------------------------------------------------------------------|
|     11    | Insel und Marschen                                               |
|     12    | Geest, Schleswig-Holstein und Hamburg                            |
|     -1    | Mecklenburg-Vorpommern +  Brandenburg und Berlin (will be fixed) |
|     31    | Westl. Niedersachsen/Bremen                                      |
|     32    | Östl. Niedersachsen                                              |
|     41    | Rhein.-Westfäl. Tiefland                                         |
|     42    | Ostwestfalen                                                     |
|     43    | Mittelgebirge NRW                                                |
|     -1    | Brandenburg und Berlin + Mecklenburg-Vorpommern (will be fixed)  |
|     61    | Tiefland Sachsen-Anhalt                                          |
|     62    | Harz                                                             |
|     71    | Tiefland Thüringen                                               |
|     72    | Mittelgebirge Thüringen                                          |
|     81    | Tiefland Sachsen                                                 |
|     82    | Mittelgebirge Sachsen                                            |
|     91    | Nordhessen und hess. Mittelgebirge                               |
|     92    | Rhein-Main                                                       |
|    101    | Rhein, Pfalz, Nahe und Mosel                                     |
|    102    | Mittelgebirgsbereich Rheinland-Pfalz                             |
|    103    | Saarland                                                         |
|    111    | Oberrhein und unteres Neckartal                                  |
|    112    | Hohenlohe/mittlerer Neckar/Oberschwaben                          |
|    113    | Mittelgebirge Baden-Württemberg                                  |
|    121    | Allgäu/Oberbayern/Bay. Wald                                      |
|    122    | Donauniederungen                                                 |
|    123    | Bayern nördl. der Donau, o. Bayr. Wald, o. Mainfranken           |
|    124    | Mainfranken                                                      |

To find your region please follow this link to the DWD:
https://www.dwd.de/DE/leistungen/gefahrenindizespollen/Gebiete.html?nn=16102&lsbId=463856