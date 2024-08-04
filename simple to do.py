def choices():
    print('1. add an item')
    print('2. remove an item')
    print('3. show part of a list')
    print('4. show entire list')
    print('5. exit')
    option = int(input('>>>'))

#intro
print('Welcome - this is your personal to-do list')
print(' ')
name = input('What is your name?')
print ('Welcome',name,'.Lets start the application')
print(' ')
print('What do you want to do?')
print('CHOOSE:')



list = []

print('')

#add an item
if option == 1:
    print('what do you want to add?')
    add = str(input('>'))
    list.append(add)
    print('list updated')
    print('')
    #redoing the loop
    choices()


#remove an item
elif option ==2:
    print('what do you want to remove?')
    print('enter the item no. (0,1,2,3...) from the list')
    print(list)
    remove = int(input('>'))
    del list[remove]
    print('')
    print(list)
    print('')
    choices()

#incomplete - generates an error
