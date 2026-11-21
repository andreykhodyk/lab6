good_deeds = {
    'today': [
        'Make a compliment to a friend',
        'Call your grandparents',
        'Embrace parents'
    ],
    'tomorrow': [
        'Feed the birds in the park',
        'Give unnecessary things to those who need them',
        'Smile'
    ]
}

for day in good_deeds:
    print(day + ':')
    for deed in good_deeds[day]:
        print(deed)