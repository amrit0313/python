enemies = 2

# def increase_ememies():
#     enemies = 3
#     print(enemies) // this wil print 3 but down will print 2

# increase_ememies()
# print(enemies)     //this will print 2


def increaseEnemies():
    # enemies+=1 // we can't directly do this
    print(enemies)
    return enemies +1

enemies = increaseEnemies()
print(enemies)