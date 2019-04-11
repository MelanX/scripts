import calendar
import csv
import datetime
import json
import os
import shutil
import urllib.parse
import urllib.request
import zipfile

import telegram_send
from matplotlib import pyplot as plt

global regionpart_names

regionpart_names = ['Inseln und Marschen', 'Geest, Schleswig-Holstein und Hamburg', 'Mecklenburg-Vorpommern',
                    'Westl. Niedersachsen/Bremen', 'Östl. Niedersachsen', 'Rhein.-Westfäl. Tiefland', 'Ostwestfalen',
                    'Mittelgebirge NRW', 'Brandenburg und Berlin', 'Tiefland Sachsen-Anhalt', 'Harz',
                    'Tiefland Thüringen', 'Mittelgebirge Thüringen', 'Tiefland Sachsen', 'Mittelgebirge Sachsen',
                    'Nordhessen und hess. Mittelgebirge', 'Rhein-Main', 'Rhein, Pfalz, Nahe und Mosel',
                    'Mittelgebirgsbereich Rheinland-Pfalz', 'Saarland', 'Oberrhein und unteres Neckartal',
                    'Hohenlohe/mittlerer Neckar/Oberschwaben', 'Mittelgebirge Baden-Württemberg',
                    'Allgäu/Oberbayern/Bay. Wald', 'Donauniederungen',
                    'Bayern nördl. der Donau, o. Bayr. Wald, o. Mainfranken', 'Mainfranken']


def main():
    global regionpart_names

    while True:  # loop for no internet
        try:
            req = urllib.request.Request("https://opendata.dwd.de/climate_environment/health/alerts/s31fg.json")
            opener = urllib.request.build_opener()
            f = opener.open(req)
            data = json.loads(f.read())
            break
        except Exception as e:
            import time

            print(e)
            time.sleep(10)

    start_data = ['Datum', 'Erle', 'Beifuss', 'Ambrosia', 'Roggen', 'Esche', 'Birke', 'Graeser', 'Hasel']
    pollen = ['Erle', 'Beifuss', 'Ambrosia', 'Roggen', 'Esche', 'Birke', 'Graeser', 'Hasel']
    days = ['today', 'tomorrow', 'dayafter_to']
    regionpart_ids = [11, 12, -1, 31, 32, 41, 42, 43, -1, 61, 62, 71, 72, 81, 82, 91, 92, 101, 102, 103, 111, 112, 113,
                      121, 122, 123, 124]

    # just for sending todays values to my smartphone via Telegram
    # if you have your own Telegram Bot you can use this as well
    # just delete if not needed (ends in line 89)
    i = 0
    while i <= 26:
        partregion_data = data["content"][i]["partregion_id"]
        if partregion_data == 11:  # here you can set your region; for more information see README.md
            my_region = i
            break
        i += 1

    for j in days:
        for i in pollen:
            json_weight = data["content"][my_region]["Pollen"][i][j]
            if not json_weight == "-1":
                if json_weight == "0":
                    weight = "keine Belastung"
                elif json_weight == "0-1":
                    weight = "keine bis geringe Belastung"
                elif json_weight == "1":
                    weight = "geringe Belastung"
                elif json_weight == "1-2":
                    weight = "geringe bis mittlere Belastung"
                elif json_weight == "2":
                    weight = "mittlere Belastung"
                elif json_weight == "2-3":
                    weight = "mittlere bis hohe Belastung"
                elif json_weight == "3":
                    weight = "hohe Belastung"
                flight = f"{i} - {j}: {weight}"

                if json_weight != "-1" and json_weight != "0":
                    if j == days[0]:
                        telegram_send.send(messages=[flight])
                    if j == days[1]:
                        telegram_send.send(messages=[flight])
                    if j == days[2]:
                        telegram_send.send(messages=[flight])
                    # print(val)
    # ends here

    now = datetime.datetime.now()
    today = now.strftime('%d.%m.%Y')
    ids = 0
    doubled = False
    for k in regionpart_ids:
        x = 0
        while x <= 26:
            partregion_data = data["content"][x]["partregion_id"]
            if partregion_data == k:
                if partregion_data == -1:
                    if not doubled:
                        if data["content"][x]["region_id"] == 20:
                            this_id = x
                            doubled = True
                            break
                    else:
                        if data["content"][x]["region_id"] == 50:
                            this_id = x
                            break
                else:
                    this_id = x
                    break
            x += 1

        pollen_val = [today]
        for i in pollen:
            json_weight = data["content"][this_id]["Pollen"][i]["today"]
            if not json_weight == "-1":
                if json_weight == "0":
                    val = 0
                elif json_weight == "0-1":
                    val = 0.5
                elif json_weight == "1":
                    val = 1
                elif json_weight == "1-2":
                    val = 1.5
                elif json_weight == "2":
                    val = 2
                elif json_weight == "2-3":
                    val = 2.5
                elif json_weight == "3":
                    val = 3
            else:
                val = ""
            pollen_val.append(val)

        if not os.path.isfile(f'data/{regionpart_names[ids].replace("/", "_")}.csv'):
            with open(f'data/{regionpart_names[ids].replace("/", "_")}.csv', 'a+', newline='',
                      encoding='utf-8') as file:
                csv_writer = csv.writer(file, delimiter=",")
                csv_writer.writerow(start_data)
                csv_writer.writerow(pollen_val)
        else:
            with open(f'data/{regionpart_names[ids].replace("/", "_")}.csv', 'a+', newline='',
                      encoding='utf-8') as file:
                csv_writer = csv.writer(file, delimiter=",")
                csv_writer.writerow(pollen_val)
        ids += 1


def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


def save_diagram():
    global regionpart_names

    now = datetime.datetime.now()
    ids = 0
    while ids < len(regionpart_names):
        region_id = regionpart_names[ids]

        sample_data = csv.read_csv(f"data/{region_id.replace('/', '_')}.csv")

        plt.plot(sample_data.Datum, sample_data.Erle, "-o")
        plt.plot(sample_data.Datum, sample_data.Beifuss, "-o")
        plt.plot(sample_data.Datum, sample_data.Ambrosia, "-o")
        plt.plot(sample_data.Datum, sample_data.Roggen, "-o")
        plt.plot(sample_data.Datum, sample_data.Esche, "-o")
        plt.plot(sample_data.Datum, sample_data.Birke, "-o")
        plt.plot(sample_data.Datum, sample_data.Graeser, "-o")
        plt.plot(sample_data.Datum, sample_data.Hasel, "-o")
        plt.title(region_id)
        plt.xlabel("Datum")
        plt.ylabel("Belastungsstärke")
        plt.legend(["Erle", "Beifuß", "Ambrosia", "Roggen", "Esche", "Birke", "Gräser", "Hasel"])
        plt.savefig(now.strftime(f"diagrams/%Y/%B/{region_id.replace('/', '_')}.png"))
        # plt.show()
        ids += 1


def compress_diagram():
    now = datetime.datetime.now()
    zipf = zipfile.ZipFile(now.strftime("diagrams/%Y/%B.zip"), "w", zipfile.ZIP_DEFLATED)
    os.chdir(now.strftime("diagrams/%Y/"))
    zipdir(now.strftime("%B/"), zipf)
    zipf.close()
    shutil.rmtree(now.strftime("%B/"))


def backup():
    today = datetime.date.today()
    year = today.year
    month = today.month
    lenght = calendar.monthrange(year, month)
    last_day = lenght[1]

    if today.day == last_day:
        import zipfile
        zipf = zipfile.ZipFile(f"backup/{today.strftime('%B %Y')}.zip", "w", zipfile.ZIP_DEFLATED)
        zipdir('data/', zipf)
        zipf.close()

        save_diagram()
        compress_diagram()

        shutil.rmtree("data/")


def create_paths():
    now = datetime.datetime.now()

    if not os.path.exists("data"):
        os.mkdir("data")
    if not os.path.exists("backup"):
        os.mkdir("backup")
    if not os.path.exists("diagrams/"):
        os.mkdir("diagrams")
    if not os.path.exists(now.strftime("diagrams/%Y/")):
        os.mkdir(now.strftime("diagrams/%Y"))
    if not os.path.exists(now.strftime("diagrams/%Y/%B/")):
        os.mkdir(now.strftime("diagrams/%Y/%B"))


if __name__ == "__main__":
    create_paths()
    main()
    backup()
