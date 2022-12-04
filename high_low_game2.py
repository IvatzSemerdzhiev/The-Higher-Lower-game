
logo = """
    .                  .-.    .  _   *     _   .
           *          /   \     ((       _/ \       *    .
         _    .   .--'\/\_ \     `      /    \  *    ___
     *  / \_    _/ ^      \/\'__        /\/\  /\  __/   \ *
       /    \  /    .'   _/  /  \  *' /    \/  \/ .`'\_/\   .
  .   /\/\  /\/ :' __  ^/  ^/    `--./.'  ^  `-.\ _    _:\ _
     /    \/  \  _/  \-' __/.' ^ _   \_   .'\   _/ \ .  __/ \

 `::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.'
 """
peaks = {
"Mount Everest":8848.86,
"Aconcagua"	:	6960.8,
"Denali"	:	6191,
"Mount Kilimanjaro"	:	5895,
"Pico Cristóbal Colón"	:	5700,
"Mount Logan"	:	5959,
"Pico de Orizaba"	:	5636,
"Vinson Massif"	:	4892,
"Puncak Jaya":	4884,
"Mount Elbrus"	:	5642,
"Mont Blanc"	:	4808,
"Mount Damavand"	:	5610,
"Klyuchevskaya Sopka"	:	4750,
"Nanga Parbat"	:	8125,
"Mauna Kea"	:	4205,
"Jengish Chokusu"	:	7439,
"Bogda Peak"	:	5445,
"Chimborazo"	:	6263,
"Namcha Barwa"	:	7782,
"Mount Kinabalu"	:	4095,
"Mount Rainier"	:	4393,
"K2"	:	8611,
"Ras Dashen"	:	4550,
"Volcán Tajumulco"	:	4220,
"Pico Bolívar"	:	4981,
"Mount Fairweather"	:	4671,
"Yushan"	:	3952,
"Mount Stanley"	:	5109,
"Kanchenjunga"	:	8586,
"Tirich Mir"	:	7708,
"Mount Cameroon"	:	4040,
"Mount Kenya"	:	5199,
"Mount Kerinci"	:	3805,
"Mount Erebus"	:	3794,
"Mount Fuji"	:	3776,
"Toubkal"	:	4167,
"Cerro Chirripó"	:	3820,
"Mount Rinjani"	:	3726,
"Aoraki/Mount Cook"	:	3724,
"Teide"	:	3715,
"Mount Boising"	:	4150,
"Monte San Valentin"	:	4058,
"Gunnbjørn Fjeld"	:	3694,
"Ojos del Salado"	:	6893,
"Semeru"	:	3676,
"Ritacuba Blanco"	:	5410,
"Mount Gongga"	:	7556,
"Mount Ararat"	:	5137,
"Kongur Tagh"	:	7649,
"Mount Blackburn"	:	4996,
"Mount Hayes"	:	4216,
"Mount Latimojong"	:	3478,
"Mount Saint Elias"	:	5489,
"Ismoil Somoni Peak"	:	7495,
"Dhaulagiri"	:	8167,
"Mercedario"	:	6720,
"Lautaro"	:	3623,
"Belukha Mountain"	:	4506,
"Mount Etna"	:	3329,
"Monte San Lorenzo"	:	3706,
"Mount Karisimbi"	:	4507,
"Jabal an Nabi Shu'ayb"	:	3666,
"Mount Waddington"	:	4019,
"Mulhacén"	:	3479,
"Mount Slamet"	:	3428,
"Sabalan"	:	4811,
"Mount Marcus Baker"	:	3991,
"Sauyr Zhotasy"	:	3840,
"Cerro del Bolsón"	:	5552,
"Tomort"	:	4886,
"Jade Dragon Snow Mountain"	:	5596,
"Mount Meru"	:	4565,
"Shiveluch"	:	3307,
"Nanda Devi"	:	7816,
"Ichinsky"	:	3607,
"Mount Lawu"	:	3265,
"Batura Sar"	:	7795,
"Mount Siple"	:	3110,
"Pico Duarte"	:	3098,
"Manaslu"	:	8163,
"Mount Whitney"	:	4418,
"Piton des Neiges"	:	3069,
"Raung"	:	3332,
"Xuelian Feng"	:	6627,
"Maromokotro"	:	2876,
"Mount Shishaldin"	:	2869,
"Moncong Lompotabang"	:	2874,
"Buni Zom"	:	6542,
"Kuh-e Bandaka"	:	6812,
"Mount Robson"	:	3959,
"Mount Fogo"	:	2829,
"Kamet"	:	7756,
"Rakaposhi"	:	7788,
"Aneto"	:	3404,
"Arjuno-Welirang"	:	3339,
"Jiuding Shan"	:	4969
}

import random
list = []

game_is_on = True
points = 0
while game_is_on:

    for x in peaks:
        list.append(x)

    def pick_random_peak():
        peak_random = random.choice(list)
        return peak_random

    peak1 = pick_random_peak()
    peak2 = pick_random_peak()
    if peak1 == peak2:
        continue

    for peak in peaks:
        height1 = peaks[peak1]
    for peak in peaks:
        height2 = peaks[peak2]
    print(logo)
    print(peak1, end=" : ")
    print(f"{height1}m")
    print(peak2)


    user_choice = input("Higher h or lower l ->")
    if user_choice == 'l' and height1 < height2:
        game_is_on = False

        print("Wrong Answer")
        print(f"{peak2} : {height2}")
        print(f"Your highest score {points}")
        points = 0
        break
    elif user_choice == 'h' and height1 > height2:
        game_is_on = False

        print("Wrong Answer")
        print(f"{peak2} : {height2}")
        print(f"Your highest score {points}")
        points = 0
        break
    else:
        game_is_on = True
        print(f"{height2}m")

    points +=1
    print(f"Your score :{points}")





