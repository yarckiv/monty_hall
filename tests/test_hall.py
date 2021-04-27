# -*- coding: utf-8 -*-
import json

import pytest
import requests
import random

headers = {'Content-Type': 'application/json'}


def test_play():
    attempts = 100000
    choose = ('keep', 'change')
    r = requests.post('http://localhost:8888/play', headers=headers,
                      data=json.dumps({"choose_option":
                                           choose[random.randint(0, 1)],
                                       "attempts": attempts}))
    assert 200 == r.status_code
    result = r.json()
    wins_per = int((result.get('wins') * 100) / attempts)
    loose_per = int((result.get('loose') * 100) / attempts)
    print(f"\n\n wins_per --> \n {wins_per} \n\n")
    print(f"\n\n loose_per --> \n {loose_per} \n\n")
    assert pytest.approx(33) == wins_per
    assert loose_per == pytest.approx(66)
