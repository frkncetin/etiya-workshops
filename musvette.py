
import string
alphabet = list(string.ascii_lowercase)
#print(alphabet)
def print_rangoli(size):

#size=3
    l = []
    for i in range(size):
        l.append(alphabet[i])
    print(l)
    
    for i in range(1,(size+1)):
        
        #for j in range(1,(size*2)):

        print(l[-i].center((size*4)-3,"-"))        


print_rangoli(3)


# import string
# alphabet = list(string.ascii_lowercase)
# #print(alphabet)
# def print_rangoli(size):

# #size=3
#     l = []
#     for line in range(1,4):
#         l.append(alphabet[i])
#     print(l)

#     for x in range((size*4)-3):
#         if x

# print_rangoli(4)
