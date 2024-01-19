# # OOPs- Object oriented programming

# # classes
# # fuction 
# # objects
# # constructor
# # inheritance
# # polymorphism
# # (function overloading
# #  function overiding
# #  constructor overloading)
# # Abstraction
# # encapsulation


# class user:
#     def __init__(self,u,p):
#         self.username = u
#         self.password =p


#     username= None
#     password= None


#     def login(self):
#         print("sucessfully login",self.username)

#     def logout(self):
#         print("sucesfully logout",self.username)
        

# class test:
#     user1=user("priyanshu",12345)
#     user1.login()

#     user2=user("anuj bhai",2244)
#     user2.logout()



class product:
    def __init__(self,n,p,q):
     self.name=n
     self.price=p
     self.quantity=q

     name=None
     price=None
    quantity=None

    
class customer:
   def __init__(self,n,a):
      self.name=n
      self.address=a
        
      name,address=None


def calculate_total_(p,q):
   return q*p.price

def create_order_(c,p):
   order_details= c.name + c.address +p.name
   return order_details



class Test:
    pen=product('pen',20,1)
    book=product('Book',300,1)
    watch=product("casio",1200,1)

    c1=customer("priyanshu","gwalior")
    c2=customer("anusha","indore")
    c3=customer("sakshi","rau")
    


    
    

    