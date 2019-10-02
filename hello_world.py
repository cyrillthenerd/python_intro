name = input("Enter your name here")

teacher = input("Enter your teachers name here")

print("Hello " + name + " and welcome to your first Python lesson with " + teacher + " !")

start_link = input("Paste the link from " + teacher + " here:" )

f= open("intro.txt","w+")

f.write("Hello World my name is " + name + " and I'm currently in my very first Python lesson with " + teacher + " !")
f.write(teacher + " asked me to write down this important link: " + start_link)

print(f.read)

print("Congratulations you just learned the very basics of Python!! Your teacher which goes by the name of " + teacher + " is unbelievably proud and is hoping that this little intro got you as excited as he is :-D")
