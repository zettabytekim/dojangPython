with open('hello2.txt', 'w') as file:
    for i in range(3):
        file.write('Hello, world! {0}\n'.format(i))
