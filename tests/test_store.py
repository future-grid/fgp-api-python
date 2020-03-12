import datetime
import fgp
from fgp.controller.store import Store
import pandas


def test_store_parse_data():
    response = {
        '9000000002_9000000002': {
            'data': [
                {'currentA': 1.89, 'voltageA': 245.12, 'timestamp': 1569888000000},
                {'currentA': 3.61, 'voltageA': 244.92, 'timestamp': 1569888300000},
                {'currentA': 3.19, 'voltageA': 245.54, 'timestamp': 1569888600000},
                {'currentA': 3.42, 'voltageA': 244.44, 'timestamp': 1569888900000},
                {'currentA': 3.72, 'voltageA': 244.44, 'timestamp': 1569889200000},
                {'currentA': 3.58, 'voltageA': 244.64, 'timestamp': 1569889500000},
                {'currentA': 4.23, 'voltageA': 244.98, 'timestamp': 1569889800000},
                {'currentA': 2.25, 'voltageA': 245.33, 'timestamp': 1569890100000},
                {'currentA': 3.93, 'voltageA': 245.26, 'timestamp': 1569890400000},
                {'currentA': 3.37, 'voltageA': 245.22, 'timestamp': 1569890700000},
                {'currentA': 3.37, 'voltageA': 245.9, 'timestamp': 1569891000000},
                {'currentA': 3.72, 'voltageA': 246.12, 'timestamp': 1569891300000},
                {'currentA': 3.35, 'voltageA': 246.44, 'timestamp': 1569891600000},
                {'currentA': 3.37, 'voltageA': 246.02, 'timestamp': 1569891900000},
                {'currentA': 1.57, 'voltageA': 246.87, 'timestamp': 1569892200000},
                {'currentA': 3.91, 'voltageA': 247.18, 'timestamp': 1569892500000},
                {'currentA': 3.21, 'voltageA': 247.56, 'timestamp': 1569892800000},
                {'currentA': 2.05, 'voltageA': 247.74, 'timestamp': 1569893100000},
                {'currentA': 3.97, 'voltageA': 247.26, 'timestamp': 1569893400000},
                {'currentA': 3.69, 'voltageA': 247.57, 'timestamp': 1569893700000},
                {'currentA': 3.32, 'voltageA': 247.79, 'timestamp': 1569894000000},
                {'currentA': 3.87, 'voltageA': 246.74, 'timestamp': 1569894300000},
                {'currentA': 3.91, 'voltageA': 247.08, 'timestamp': 1569894600000},
                {'currentA': 2.54, 'voltageA': 245.53, 'timestamp': 1569894900000},
                {'currentA': 3.8, 'voltageA': 246.56, 'timestamp': 1569895200000},
                {'currentA': 3.57, 'voltageA': 246.1, 'timestamp': 1569895500000},
                {'currentA': 3.44, 'voltageA': 246.15, 'timestamp': 1569895800000},
                {'currentA': 3.36, 'voltageA': 245.78, 'timestamp': 1569896100000},
                {'currentA': 2.12, 'voltageA': 245.22, 'timestamp': 1569896400000},
                {'currentA': 4.21, 'voltageA': 244.32, 'timestamp': 1569896700000},
                {'currentA': 3.73, 'voltageA': 245.68, 'timestamp': 1569897000000},
                {'currentA': 3.32, 'voltageA': 245.0, 'timestamp': 1569897300000},
                {'currentA': 3.35, 'voltageA': 243.86, 'timestamp': 1569897600000},
                {'currentA': 1.9, 'voltageA': 244.4, 'timestamp': 1569897900000},
                {'currentA': 4.0, 'voltageA': 244.37, 'timestamp': 1569898200000},
                {'currentA': 3.35, 'voltageA': 244.93, 'timestamp': 1569898500000},
                {'currentA': 3.54, 'voltageA': 244.5, 'timestamp': 1569898800000},
                {'currentA': 1.9, 'voltageA': 244.34, 'timestamp': 1569899100000},
                {'currentA': 4.44, 'voltageA': 244.77, 'timestamp': 1569899400000},
                {'currentA': 4.39, 'voltageA': 244.74, 'timestamp': 1569899700000},
                {'currentA': 4.28, 'voltageA': 245.07, 'timestamp': 1569900000000},
                {'currentA': 4.18, 'voltageA': 245.09, 'timestamp': 1569900300000},
                {'currentA': 1.86, 'voltageA': 245.48, 'timestamp': 1569900600000},
                {'currentA': 3.82, 'voltageA': 244.88, 'timestamp': 1569900900000},
                {'currentA': 3.35, 'voltageA': 244.81, 'timestamp': 1569901200000},
                {'currentA': 3.35, 'voltageA': 244.21, 'timestamp': 1569901500000},
                {'currentA': 3.23, 'voltageA': 245.13, 'timestamp': 1569901800000},
                {'currentA': 2.48, 'voltageA': 244.7, 'timestamp': 1569902100000},
                {'currentA': 3.48, 'voltageA': 244.14, 'timestamp': 1569902400000},
                {'currentA': 3.31, 'voltageA': 245.02, 'timestamp': 1569902700000},
                {'currentA': 3.35, 'voltageA': 244.6, 'timestamp': 1569903000000},
                {'currentA': 3.57, 'voltageA': 244.36, 'timestamp': 1569903300000},
                {'currentA': 3.64, 'voltageA': 244.67, 'timestamp': 1569903600000},
                {'currentA': 3.85, 'voltageA': 244.34, 'timestamp': 1569903900000},
                {'currentA': 2.05, 'voltageA': 244.38, 'timestamp': 1569904200000},
                {'currentA': 3.99, 'voltageA': 244.33, 'timestamp': 1569904500000},
                {'currentA': 3.97, 'voltageA': 243.84, 'timestamp': 1569904800000},
                {'currentA': 3.92, 'voltageA': 243.96, 'timestamp': 1569905100000},
                {'currentA': 3.84, 'voltageA': 243.62, 'timestamp': 1569905400000},
                {'currentA': 3.7, 'voltageA': 242.58, 'timestamp': 1569905700000},
                {'currentA': 3.46, 'voltageA': 247.54, 'timestamp': 1569906000000},
                {'currentA': 3.83, 'voltageA': 246.68, 'timestamp': 1569906300000},
                {'currentA': 3.79, 'voltageA': 247.12, 'timestamp': 1569906600000},
                {'currentA': 3.54, 'voltageA': 247.45, 'timestamp': 1569906900000},
                {'currentA': 3.59, 'voltageA': 246.58, 'timestamp': 1569907200000},
                {'currentA': 1.82, 'voltageA': 248.7, 'timestamp': 1569907500000},
                {'currentA': 3.7, 'voltageA': 247.28, 'timestamp': 1569907800000},
                {'currentA': 3.19, 'voltageA': 247.26, 'timestamp': 1569908100000},
                {'currentA': 3.2, 'voltageA': 247.14, 'timestamp': 1569908400000},
                {'currentA': 3.33, 'voltageA': 245.92, 'timestamp': 1569908700000},
                {'currentA': 3.4, 'voltageA': 246.09, 'timestamp': 1569909000000},
                {'currentA': 3.56, 'voltageA': 245.98, 'timestamp': 1569909300000},
                {'currentA': 3.54, 'voltageA': 246.38, 'timestamp': 1569909600000},
                {'currentA': 4.69, 'voltageA': 244.03, 'timestamp': 1569909900000},
                {'currentA': 4.25, 'voltageA': 243.98, 'timestamp': 1569910200000},
                {'currentA': 4.31, 'voltageA': 243.46, 'timestamp': 1569910500000},
                {'currentA': 5.05, 'voltageA': 246.54, 'timestamp': 1569910800000},
                {'currentA': 2.92, 'voltageA': 245.17, 'timestamp': 1569911100000},
                {'currentA': 5.67, 'voltageA': 244.2, 'timestamp': 1569911400000},
                {'currentA': 11.45, 'voltageA': 241.32, 'timestamp': 1569911700000},
                {'currentA': 11.01, 'voltageA': 244.72, 'timestamp': 1569912000000},
                {'currentA': 1.47, 'voltageA': 245.97, 'timestamp': 1569912300000},
                {'currentA': 1.81, 'voltageA': 244.42, 'timestamp': 1569912600000},
                {'currentA': 12.38, 'voltageA': 243.16, 'timestamp': 1569912900000},
                {'currentA': 9.17, 'voltageA': 242.32, 'timestamp': 1569913200000},
                {'currentA': 12.44, 'voltageA': 240.69, 'timestamp': 1569913500000},
                {'currentA': 4.79, 'voltageA': 248.23, 'timestamp': 1569913800000},
                {'currentA': 4.54, 'voltageA': 245.36, 'timestamp': 1569914100000},
                {'currentA': 4.9, 'voltageA': 244.05, 'timestamp': 1569914400000},
                {'currentA': 4.58, 'voltageA': 243.4, 'timestamp': 1569914700000},
                {'currentA': 4.76, 'voltageA': 242.48, 'timestamp': 1569915000000},
                {'currentA': 4.9, 'voltageA': 243.66, 'timestamp': 1569915300000},
                {'currentA': 4.98, 'voltageA': 243.9, 'timestamp': 1569915600000},
                {'currentA': 4.73, 'voltageA': 243.62, 'timestamp': 1569915900000},
                {'currentA': 4.63, 'voltageA': 243.22, 'timestamp': 1569916200000},
                {'currentA': 4.38, 'voltageA': 243.76, 'timestamp': 1569916500000},
                {'currentA': 4.35, 'voltageA': 244.12, 'timestamp': 1569916800000},
                {'currentA': 4.36, 'voltageA': 244.02, 'timestamp': 1569917100000},
                {'currentA': 4.59, 'voltageA': 244.24, 'timestamp': 1569917400000},
                {'currentA': 5.0, 'voltageA': 244.47, 'timestamp': 1569917700000},
                {'currentA': 4.17, 'voltageA': 244.96, 'timestamp': 1569918000000},
                {'currentA': 4.21, 'voltageA': 245.31, 'timestamp': 1569918300000},
                {'currentA': 2.7, 'voltageA': 247.1, 'timestamp': 1569918600000},
                {'currentA': 4.22, 'voltageA': 245.8, 'timestamp': 1569918900000},
                {'currentA': 3.94, 'voltageA': 245.13, 'timestamp': 1569919200000},
                {'currentA': 3.92, 'voltageA': 244.92, 'timestamp': 1569919500000},
                {'currentA': 3.68, 'voltageA': 245.4, 'timestamp': 1569919800000},
                {'currentA': 3.99, 'voltageA': 244.48, 'timestamp': 1569920100000},
                {'currentA': 3.43, 'voltageA': 244.44, 'timestamp': 1569920400000},
                {'currentA': 4.04, 'voltageA': 244.78, 'timestamp': 1569920700000},
                {'currentA': 3.89, 'voltageA': 245.88, 'timestamp': 1569921000000},
                {'currentA': 3.96, 'voltageA': 245.23, 'timestamp': 1569921300000},
                {'currentA': 4.19, 'voltageA': 245.51, 'timestamp': 1569921600000},
                {'currentA': 4.08, 'voltageA': 246.16, 'timestamp': 1569921900000},
                {'currentA': 4.69, 'voltageA': 246.8, 'timestamp': 1569922200000},
                {'currentA': 4.63, 'voltageA': 247.13, 'timestamp': 1569922500000},
                {'currentA': 4.63, 'voltageA': 245.74, 'timestamp': 1569922800000},
                {'currentA': 3.45, 'voltageA': 245.26, 'timestamp': 1569923100000},
                {'currentA': 2.07, 'voltageA': 246.1, 'timestamp': 1569923400000},
                {'currentA': 0.0, 'voltageA': 246.14, 'timestamp': 1569923700000},
                {'currentA': 2.85, 'voltageA': 246.7, 'timestamp': 1569924000000},
                {'currentA': 3.71, 'voltageA': 246.9, 'timestamp': 1569924300000},
                {'currentA': 4.22, 'voltageA': 248.0, 'timestamp': 1569924600000},
                {'currentA': 4.13, 'voltageA': 243.86, 'timestamp': 1569924900000},
                {'currentA': 4.61, 'voltageA': 243.1, 'timestamp': 1569925200000},
                {'currentA': 5.84, 'voltageA': 245.04, 'timestamp': 1569925500000},
                {'currentA': 5.59, 'voltageA': 244.79, 'timestamp': 1569925800000},
                {'currentA': 7.8, 'voltageA': 244.24, 'timestamp': 1569926100000},
                {'currentA': 1.9, 'voltageA': 245.52, 'timestamp': 1569926400000},
                {'currentA': 2.49, 'voltageA': 245.38, 'timestamp': 1569926700000},
                {'currentA': 2.35, 'voltageA': 245.34, 'timestamp': 1569927000000},
                {'currentA': -4.2, 'voltageA': 246.88, 'timestamp': 1569927300000},
                {'currentA': -6.15, 'voltageA': 247.59, 'timestamp': 1569927600000},
                {'currentA': -6.25, 'voltageA': 248.42, 'timestamp': 1569927900000},
                {'currentA': -6.76, 'voltageA': 248.5, 'timestamp': 1569928200000},
                {'currentA': -5.36, 'voltageA': 244.4, 'timestamp': 1569928500000},
                {'currentA': -5.07, 'voltageA': 244.8, 'timestamp': 1569928800000},
                {'currentA': -4.06, 'voltageA': 243.86, 'timestamp': 1569929100000},
                {'currentA': -4.55, 'voltageA': 243.61, 'timestamp': 1569929400000},
                {'currentA': -3.77, 'voltageA': 244.0, 'timestamp': 1569929700000},
                {'currentA': -3.24, 'voltageA': 244.14, 'timestamp': 1569930000000},
                {'currentA': -2.63, 'voltageA': 246.88, 'timestamp': 1569930300000},
                {'currentA': -3.0, 'voltageA': 246.91, 'timestamp': 1569930600000},
                {'currentA': -3.23, 'voltageA': 247.72, 'timestamp': 1569930900000},
                {'currentA': -3.45, 'voltageA': 247.7, 'timestamp': 1569931200000},
                {'currentA': -3.41, 'voltageA': 247.3, 'timestamp': 1569931500000},
                {'currentA': -3.44, 'voltageA': 247.09, 'timestamp': 1569931800000},
                {'currentA': -4.14, 'voltageA': 247.5, 'timestamp': 1569932100000},
                {'currentA': -4.51, 'voltageA': 248.76, 'timestamp': 1569932400000},
                {'currentA': -4.34, 'voltageA': 244.8, 'timestamp': 1569932700000},
                {'currentA': -4.4, 'voltageA': 244.58, 'timestamp': 1569933000000},
                {'currentA': -4.13, 'voltageA': 244.4, 'timestamp': 1569933300000},
                {'currentA': -3.69, 'voltageA': 243.88, 'timestamp': 1569933600000},
                {'currentA': -3.79, 'voltageA': 242.84, 'timestamp': 1569933900000},
                {'currentA': -3.68, 'voltageA': 242.88, 'timestamp': 1569934200000},
                {'currentA': -3.97, 'voltageA': 243.04, 'timestamp': 1569934500000},
                {'currentA': -3.81, 'voltageA': 243.16, 'timestamp': 1569934800000},
                {'currentA': -3.78, 'voltageA': 242.79, 'timestamp': 1569935100000},
                {'currentA': -3.27, 'voltageA': 242.18, 'timestamp': 1569935400000},
                {'currentA': -3.09, 'voltageA': 246.27, 'timestamp': 1569935700000},
                {'currentA': -3.15, 'voltageA': 246.57, 'timestamp': 1569936000000},
                {'currentA': -3.46, 'voltageA': 246.49, 'timestamp': 1569936300000},
                {'currentA': -3.37, 'voltageA': 246.54, 'timestamp': 1569936600000},
                {'currentA': -3.12, 'voltageA': 245.32, 'timestamp': 1569936900000},
                {'currentA': -3.14, 'voltageA': 245.13, 'timestamp': 1569937200000},
                {'currentA': -2.71, 'voltageA': 245.8, 'timestamp': 1569937500000},
                {'currentA': -2.81, 'voltageA': 246.24, 'timestamp': 1569937800000},
                {'currentA': -2.66, 'voltageA': 245.9, 'timestamp': 1569938100000},
                {'currentA': -2.92, 'voltageA': 245.97, 'timestamp': 1569938400000},
                {'currentA': 0.0, 'voltageA': 245.58, 'timestamp': 1569938700000},
                {'currentA': 0.0, 'voltageA': 244.96, 'timestamp': 1569939000000},
                {'currentA': 0.0, 'voltageA': 245.68, 'timestamp': 1569939300000},
                {'currentA': 0.0, 'voltageA': 245.48, 'timestamp': 1569939600000},
                {'currentA': 0.0, 'voltageA': 245.08, 'timestamp': 1569939900000},
                {'currentA': -2.64, 'voltageA': 245.64, 'timestamp': 1569940200000},
                {'currentA': 0.0, 'voltageA': 246.1, 'timestamp': 1569940500000},
                {'currentA': -2.89, 'voltageA': 246.51, 'timestamp': 1569940800000},
                {'currentA': -3.09, 'voltageA': 246.27, 'timestamp': 1569941100000},
                {'currentA': -2.96, 'voltageA': 246.41, 'timestamp': 1569941400000},
                {'currentA': -2.8, 'voltageA': 246.78, 'timestamp': 1569941700000},
                {'currentA': -2.5, 'voltageA': 246.99, 'timestamp': 1569942000000},
                {'currentA': -3.04, 'voltageA': 246.9, 'timestamp': 1569942300000},
                {'currentA': -2.93, 'voltageA': 247.42, 'timestamp': 1569942600000},
                {'currentA': -2.9, 'voltageA': 248.33, 'timestamp': 1569942900000},
                {'currentA': -3.0, 'voltageA': 244.55, 'timestamp': 1569943200000},
                {'currentA': -3.0, 'voltageA': 244.16, 'timestamp': 1569943500000},
                {'currentA': -3.04, 'voltageA': 244.77, 'timestamp': 1569943800000},
                {'currentA': -3.0, 'voltageA': 244.56, 'timestamp': 1569944100000},
                {'currentA': 0.0, 'voltageA': 244.2, 'timestamp': 1569944400000},
                {'currentA': 0.09, 'voltageA': 245.24, 'timestamp': 1569944700000},
                {'currentA': 0.19, 'voltageA': 244.52, 'timestamp': 1569945000000},
                {'currentA': 0.51, 'voltageA': 244.38, 'timestamp': 1569945300000},
                {'currentA': 0.38, 'voltageA': 244.76, 'timestamp': 1569945600000},
                {'currentA': 0.68, 'voltageA': 245.04, 'timestamp': 1569945900000},
                {'currentA': 0.26, 'voltageA': 245.19, 'timestamp': 1569946200000},
                {'currentA': 0.26, 'voltageA': 245.1, 'timestamp': 1569946500000},
                {'currentA': 0.22, 'voltageA': 244.6, 'timestamp': 1569946800000},
                {'currentA': 0.26, 'voltageA': 243.57, 'timestamp': 1569947100000},
                {'currentA': 0.32, 'voltageA': 243.32, 'timestamp': 1569947400000},
                {'currentA': 0.0, 'voltageA': 244.41, 'timestamp': 1569947700000},
                {'currentA': 0.0, 'voltageA': 243.92, 'timestamp': 1569948000000},
                {'currentA': 0.0, 'voltageA': 243.96, 'timestamp': 1569948300000},
                {'currentA': 0.0, 'voltageA': 243.12, 'timestamp': 1569948600000},
                {'currentA': 0.0, 'voltageA': 243.24, 'timestamp': 1569948900000},
                {'currentA': 0.0, 'voltageA': 243.74, 'timestamp': 1569949200000},
                {'currentA': 0.43, 'voltageA': 242.57, 'timestamp': 1569949500000},
                {'currentA': 0.62, 'voltageA': 242.3, 'timestamp': 1569949800000},
                {'currentA': 0.66, 'voltageA': 241.04, 'timestamp': 1569950100000},
                {'currentA': 0.84, 'voltageA': 244.85, 'timestamp': 1569950400000},
                {'currentA': 0.99, 'voltageA': 245.71, 'timestamp': 1569950700000},
                {'currentA': 3.77, 'voltageA': 244.82, 'timestamp': 1569951000000},
                {'currentA': 11.7, 'voltageA': 243.57, 'timestamp': 1569951300000},
                {'currentA': 11.6, 'voltageA': 242.56, 'timestamp': 1569951600000},
                {'currentA': 10.38, 'voltageA': 241.83, 'timestamp': 1569951900000},
                {'currentA': 10.06, 'voltageA': 241.24, 'timestamp': 1569952200000},
                {'currentA': 9.13, 'voltageA': 245.69, 'timestamp': 1569952500000},
                {'currentA': 9.23, 'voltageA': 244.55, 'timestamp': 1569952800000},
                {'currentA': 9.29, 'voltageA': 242.37, 'timestamp': 1569953100000},
                {'currentA': 5.64, 'voltageA': 244.14, 'timestamp': 1569953400000},
                {'currentA': 10.87, 'voltageA': 242.8, 'timestamp': 1569953700000},
                {'currentA': 6.85, 'voltageA': 243.92, 'timestamp': 1569954000000},
                {'currentA': 6.19, 'voltageA': 243.77, 'timestamp': 1569954300000},
                {'currentA': 8.19, 'voltageA': 243.67, 'timestamp': 1569954600000},
                {'currentA': 7.56, 'voltageA': 244.26, 'timestamp': 1569954900000},
                {'currentA': 8.54, 'voltageA': 244.53, 'timestamp': 1569955200000},
                {'currentA': 8.37, 'voltageA': 243.37, 'timestamp': 1569955500000},
                {'currentA': 5.19, 'voltageA': 243.32, 'timestamp': 1569955800000},
                {'currentA': 6.56, 'voltageA': 243.62, 'timestamp': 1569956100000},
                {'currentA': 6.31, 'voltageA': 244.06, 'timestamp': 1569956400000},
                {'currentA': 4.5, 'voltageA': 244.01, 'timestamp': 1569956700000},
                {'currentA': 9.12, 'voltageA': 244.64, 'timestamp': 1569957000000},
                {'currentA': 9.38, 'voltageA': 244.68, 'timestamp': 1569957300000},
                {'currentA': 7.97, 'voltageA': 245.12, 'timestamp': 1569957600000},
                {'currentA': 9.97, 'voltageA': 244.54, 'timestamp': 1569957900000},
                {'currentA': 9.66, 'voltageA': 244.03, 'timestamp': 1569958200000},
                {'currentA': 9.66, 'voltageA': 243.9, 'timestamp': 1569958500000},
                {'currentA': 9.36, 'voltageA': 245.28, 'timestamp': 1569958800000},
                {'currentA': 10.19, 'voltageA': 245.38, 'timestamp': 1569959100000},
                {'currentA': 10.18, 'voltageA': 246.01, 'timestamp': 1569959400000},
                {'currentA': 9.56, 'voltageA': 245.51, 'timestamp': 1569959700000},
                {'currentA': 10.37, 'voltageA': 242.48, 'timestamp': 1569960000000},
                {'currentA': 10.83, 'voltageA': 241.15, 'timestamp': 1569960300000},
                {'currentA': 8.86, 'voltageA': 241.28, 'timestamp': 1569960600000},
                {'currentA': 11.74, 'voltageA': 241.65, 'timestamp': 1569960900000},
                {'currentA': 10.53, 'voltageA': 242.28, 'timestamp': 1569961200000},
                {'currentA': 9.55, 'voltageA': 242.8, 'timestamp': 1569961500000},
                {'currentA': 10.58, 'voltageA': 243.46, 'timestamp': 1569961800000},
                {'currentA': 10.25, 'voltageA': 243.78, 'timestamp': 1569962100000},
                {'currentA': 8.08, 'voltageA': 244.42, 'timestamp': 1569962400000},
                {'currentA': 7.15, 'voltageA': 244.76, 'timestamp': 1569962700000},
                {'currentA': 10.02, 'voltageA': 244.9, 'timestamp': 1569963000000},
                {'currentA': 8.54, 'voltageA': 244.72, 'timestamp': 1569963300000},
                {'currentA': 10.34, 'voltageA': 244.81, 'timestamp': 1569963600000},
                {'currentA': 7.06, 'voltageA': 245.89, 'timestamp': 1569963900000},
                {'currentA': 6.95, 'voltageA': 245.98, 'timestamp': 1569964200000},
                {'currentA': 6.55, 'voltageA': 247.36, 'timestamp': 1569964500000},
                {'currentA': 7.32, 'voltageA': 243.36, 'timestamp': 1569964800000},
                {'currentA': 4.79, 'voltageA': 243.92, 'timestamp': 1569965100000},
                {'currentA': 3.32, 'voltageA': 246.12, 'timestamp': 1569965400000},
                {'currentA': 5.79, 'voltageA': 246.79, 'timestamp': 1569965700000},
                {'currentA': 3.45, 'voltageA': 248.12, 'timestamp': 1569966000000},
                {'currentA': 5.75, 'voltageA': 241.9, 'timestamp': 1569966300000},
                {'currentA': 3.91, 'voltageA': 246.3, 'timestamp': 1569966600000},
                {'currentA': 4.58, 'voltageA': 246.88, 'timestamp': 1569966900000},
                {'currentA': 4.64, 'voltageA': 247.14, 'timestamp': 1569967200000},
                {'currentA': 6.55, 'voltageA': 243.74, 'timestamp': 1569967500000},
                {'currentA': 5.59, 'voltageA': 243.9, 'timestamp': 1569967800000},
                {'currentA': 4.34, 'voltageA': 243.4, 'timestamp': 1569968100000},
                {'currentA': 4.35, 'voltageA': 242.72, 'timestamp': 1569968400000},
                {'currentA': 4.12, 'voltageA': 243.82, 'timestamp': 1569968700000},
                {'currentA': 6.44, 'voltageA': 244.48, 'timestamp': 1569969000000},
                {'currentA': 1.99, 'voltageA': 244.87, 'timestamp': 1569969300000},
                {'currentA': 6.72, 'voltageA': 245.34, 'timestamp': 1569969600000},
                {'currentA': 4.16, 'voltageA': 245.82, 'timestamp': 1569969900000},
                {'currentA': 6.55, 'voltageA': 247.06, 'timestamp': 1569970200000},
                {'currentA': 6.62, 'voltageA': 246.43, 'timestamp': 1569970500000},
                {'currentA': 6.78, 'voltageA': 247.02, 'timestamp': 1569970800000},
                {'currentA': 6.5, 'voltageA': 246.16, 'timestamp': 1569971100000},
                {'currentA': 2.06, 'voltageA': 245.56, 'timestamp': 1569971400000},
                {'currentA': 6.71, 'voltageA': 245.9, 'timestamp': 1569971700000},
                {'currentA': 4.22, 'voltageA': 245.92, 'timestamp': 1569972000000},
                {'currentA': 4.65, 'voltageA': 245.86, 'timestamp': 1569972300000},
                {'currentA': 3.99, 'voltageA': 246.27, 'timestamp': 1569972600000},
                {'currentA': 6.63, 'voltageA': 246.12, 'timestamp': 1569972900000},
                {'currentA': 3.11, 'voltageA': 247.62, 'timestamp': 1569973200000},
                {'currentA': 6.56, 'voltageA': 247.35, 'timestamp': 1569973500000},
                {'currentA': 6.18, 'voltageA': 247.58, 'timestamp': 1569973800000},
                {'currentA': 3.89, 'voltageA': 248.12, 'timestamp': 1569974100000},
                {'currentA': 5.11, 'voltageA': 244.69, 'timestamp': 1569974400000}
        ],
            'deviceKey': 'cc2f505e-ac4c-4524-89b8-98023cba2270'
        }
    }

    df: pandas.DataFrame = Store.parse_store_data(response)
    assert type(df) is pandas.DataFrame
    assert list(df.columns) == ['device_name', 'device_key', 'timestamp', 'currentA', 'voltageA']
    assert round(df.groupby('device_name').mean().voltageA[0], 3) == round(245.07394463667825, 3)


def test_store_get_data():
    client = fgp.ApiClient(url='http://localhost:8082', application='adalon')
    df = client.store.get_data(
        device_type='meter',
        store_name='meterPqStore',
        date_from=datetime.datetime(year=2019, month=10, day=1),
        date_to=datetime.datetime(year=2019, month=10, day=2),
        fields=['voltageA', 'currentA'],
        devices=['9000000002_9000000002']
    )

    assert df.groupby('device_name').count()['timestamp'][0] == 289
