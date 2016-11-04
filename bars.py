# -*- coding: utf-8 -*-
import json, math, sys


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as bars:
        return json.load(bars)


def get_biggest_bar(data):
    max = 0
    for bar in data:
        count = bar['Cells']['SeatsCount']
        if count > max:
            name = bar['Cells']['Name']
            max = count
    print("Самый большой бар {} вмещает {} человек".format(name, max))


def get_smallest_bar(data):
    min = sys.maxsize
    for bar in data:
        count = bar['Cells']['SeatsCount']
        if count < min:
            name = bar['Cells']['Name']
            min = count
    print("Самый маленький бар {} вмещает {} человек".format(name, min))


def get_closest_bar(data, longitude, latitude):
    min = sys.maxsize

    for bar in data:
        vx = bar['Cells']['geoData']['coordinates'][1] - longitude
        vy = bar['Cells']['geoData']['coordinates'][0] - latitude
        distance = math.sqrt(vx**2 + vy**2)
        if distance < min:
            name = bar['Cells']['Name']
            min = distance
    print("Ближайший бар {}".format(name))


if __name__ == '__main__':

    data = load_data(input("Укажите путь к файлу:"))
    get_biggest_bar(data)
    get_smallest_bar(data)

    x = float(input('Введите широту'))
    y = float(input('Введите долготу'))
    get_closest_bar(data,x, y)
