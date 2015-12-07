while True:
    import random
    from os import system
    print ("This is a dice rolling program")
    print ("Press the enter button to roll")
    cmd = raw_input ("Enter to run, q to quit")
    system("cls")
    number=random.randint(1,6)
    if number==1:
        print"[------------]"
        print"[            ]"
        print"[      O     ]"
        print"[            ]"
        print"[------------]"
    if number==2:
        print"[------------]"
        print"[            ]"
        print"[   O    O   ]"
        print"[            ]"
        print"[------------]"
    if number==3:
        print"[------------]"
        print"[   O        ]"
        print"[     O      ]"
        print"[       O    ]"
        print"[------------]"
    if number==4:
        print"[------------]"
        print"[   O    O   ]"
        print"[            ]"
        print"[   O    O   ]"
        print"[------------]"
    if number==5:
        print"[------------]"
        print"[   O    o   ]"
        print"[     O      ]"
        print"[   O    O   ]"
        print"[------------]"
    if number==6:
        print"[------------]"
        print"[   O     O  ]"
        print"[   O     O  ]"
        print"[   O     O  ]"
        print"[------------]"
