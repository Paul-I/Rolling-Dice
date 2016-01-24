'# while True: this is just to be able to roll the dice again and again.'
while True:
    '# import random is just telling the computer what you are doin.'
    import random
    from os import system
    '# print is just to displaying something you want the computer to show.'
    print ("This is a dice rolling program")
    print ("Press the enter button to roll")
    '# input is telling the computer what to do when you something.'
    cmd = raw_input("Enter to roll")
    system("cls")
    '#This is tell the program range.'
    number = random.randint(1, 6)
    '#This give the program what to display for a certain choice.'
    if number == 1:
        print"[------------]"
        print"[            ]"
        print"[      O     ]"
        print"[            ]"
        print"[------------]"
    if number == 2:
        print"[------------]"
        print"[            ]"
        print"[   O    O   ]"
        print"[            ]"
        print"[------------]"
    if number == 3:
        print"[------------]"
        print"[   O        ]"
        print"[     O      ]"
        print"[       O    ]"
        print"[------------]"
    if number == 4:
        print"[------------]"
        print"[   O    O   ]"
        print"[            ]"
        print"[   O    O   ]"
        print"[------------]"
    if number == 5:
        print"[------------]"
        print"[   O    o   ]"
        print"[     O      ]"
        print"[   O    O   ]"
        print"[------------]"
    if number == 6:
        print"[------------]"
        print"[   O     O  ]"
        print"[   O     O  ]"
        print"[   O     O  ]"
        print"[------------]"
