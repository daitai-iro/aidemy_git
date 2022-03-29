#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

with open("./hyakuniissyu.txt", encoding="utf-8") as f:
    wakas = [s.strip() for s in f.readlines()]

print(wakas[random.randrange(len(wakas))])