# x = 0

# while x < 5:
#     print('hell0')
#     x = x + 1

# for i in range(5):
#     print('Hi')

# def namer(some_name):
#     print('hello ' + some_name + 'how '+ 'are you')
#     print(f'hello {some_name} how are u')

# namer('samuel')

# cgpa = 4.2

# with open('C:\\Users\\Sam\\Desktop\\myfile.txt','w') as file:
#     file.write('hello how are you\n')
#     file.write(f'your cgpa is {cgpa}\n')

class studentdetails:
    def __init__(self,first_name,second_name,course):
        self.first_name = first_name
        self.second_name = second_name
        self.course = course
        

    def names(self):
        print('hello '+ self.first_name+' '+self.second_name)

    def courses(self):
        print(f'your course is {self.course}')

    def cgpa(self,mycgpa):
        int(mycgpa)
        str(mycgpa)
        print(f'your cgpa is {mycgpa}')



student1 = studentdetails('Ann','Atwix','computer science')

# student1.names()
# student1.courses()
student1.cgpa(5)


my_list = ['car','cow','house',2,'ann']

my_list.append('makerere')
my_list.pop()


print(my_list)
print(   len(my_list)   )

