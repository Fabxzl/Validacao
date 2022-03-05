import re 
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
      
def check(email):  
  
    
    
    if(re.search(regex,email)):  
        print("Valido")  
          
    else:  
        print("Invalido")  
      
  
if __name__ == '__main__' :  
      
    
    email = "Arktrain326@gmail.com"
      
    
    check(email) 
  
    email = "batn.test1@ourearth.org"
    check(email) 
  
    email = "hurtxzi326.com"
    check(email) 