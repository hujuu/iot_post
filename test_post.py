import ambient

ambi = ambient.Ambient(2607, "fca0d37c61f9dc95") # ご自分のチャネルID、ライトキーに置き換えてください

data = [
    {'created': '2017-02-18 12:00:00', 'd1': 1.1, 'd2': 2.1},
    {'created': '2017-02-18 12:01:00', 'd1': 1.5, 'd2': 3.8},
    {'created': '2017-02-18 12:02:00', 'd1': 1.0, 'd2': 0.8},
    {'created': '2017-02-18 12:03:00', 'd1': 1.6, 'd2': 1.7}
]
r = ambi.send(data)

# r = ambi.send({"d1": temp, "d2": humid})
