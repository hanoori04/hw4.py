name = input('input his/her name : ')

def rep_char(c, n) :

  print(c * n)

def draw_line_string(user_name) :
  msg1 = 'Hello ' + user_name +',' 
  msg2 = 'Welcome to Seoul.' 

  rep_char('-' , len(msg1) if (len(msg1) > len(msg2)) else len(msg2))
  print(msg1)
  print(msg2)
  rep_char('-' , len(msg1) if (len(msg1) > len(msg2)) else len(msg2))

draw_line_string(name)