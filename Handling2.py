new_file = open('pasta.txt', 'x')
new_file.close()
import os
print("Checking if file exists or not...")
if os.path.exists('pasta.txt'):
    os.remove('testing.txt')
else:
    print("The file does not exist")
pasta = open('pasta.txt', 'w')
pasta.txt.write("I love pasta.\nPasta is my favorite food.\nI could eat pasta every day!")
pasta.txt.close()
os.remove('platter.txt')
os.rmdir('testing')