#!/usr/bin/env python3
# Copyright (c) 2008-11 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

numbers = []
total = 0
lowest = None
highest = None

while True:
    try:
        line = input("Введите число или нажмите Enter: ")
        if not line:
            break
        number = int(line)
        numbers.append(number)
        total += number
        if lowest is None or lowest > number:
            lowest = number
        if highest is None or highest < number:
            highest = number
    except ValueError as err:
        print(err)

print("числа:", numbers)
if numbers:
    print("количество =", len(numbers), "сумма =", total,
          "наименьшее =", lowest, "наибольшее =", highest,
          "среднее =", total / len(numbers))