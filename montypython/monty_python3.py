#!/usr/bin/env python3

round = 0           # integer round initiated to 0
answer = " "

while round < 3 and answer != "Brian":
    round += 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of ___________": ')
    if answer == 'Brian':
        print('Correct!')
