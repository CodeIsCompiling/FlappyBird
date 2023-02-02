move = 5
ove = 0
ao =" "
co =" "
eo =" "
go =" "
io =" "
ko =" "
mo =" "
oo =" "
qo =" "
so =" "
a =" "
b =" "
c =" "
d =" "
e =" "
f =" "
g =" "
h =" "
i =" "
j =" "
k =" "
l =" "
m =" "
n =" "
o =" "
p =" "
q =" "
r =" "
s =" "
t =" "

import time
time. sleep(0.5)
print("  ___________  ")
time. sleep(0.5)
print(" /           \ ")
time. sleep(0.5)
print(" |    play   | ")
time. sleep(0.5)
print(" \___________/ ")
time. sleep(0.5)
print("               ")
o = input ("press enter to start")
def printscreen():
  for z in range(55):
    print("")
  global a
  global b
  global c
  global d
  global e
  global f
  global g
  global h
  global i
  global g
  global k
  global l
  global m
  global n
  global o
  global p
  global q
  global r
  global s
  print("____________________________________________________")
  print(" ",a, b, )
  print(" ",c, d, )
  print(" ",e, f, )
  print(" ",g, h, )
  print(" ",i, j, )
  print(" ",k, l, )
  print(" ",m, n, )
  print(" ",o, p, )
  print(" ",q, r, )
  print(" ",s, t, )
  print("____________________________________________________")
def end():
  global a
  global b
  global c
  global d
  global e
  global f
  global g
  global h
  global i
  global j
  global k
  global l
  global m
  global n
  global o
  global p
  global q
  global r
  global s
  a =" "
  c =" "
  e =" "
  g =" "
  i =" "
  k =" "
  m =" "
  o =" "
  q =" "
  s =" "
  b ="                                         "
  d ="                                         "
  f ="                                         "
  h ="      _____       _        _     _       "
  j ="     |  ___|     / \      |_|   | |      "
  l ="     | |__      / _ \      _    | |      "
  n ="     |  __|    / /_\ \    | |   | |      "
  p ="     | |      / _____ \   | |   | |___   "
  r ="     |_|     /_/     \_\  |_|   |_____|  "
  t ="                                         "
def death():
  global a
  global b
  global c
  global d
  global e
  global f
  global g
  global h
  global i
  global j
  global k
  global l
  global m
  global n
  global o
  global p
  global q
  global r
  global s
  if ao == 1 and a =="o":
    end()
  if co == 1 and c =="o":
    end()
  if eo == 1 and e =="o":
    end()
  if go == 1 and g =="o":
    end()
  if io == 1 and i =="o":
    end()
  if ko == 1 and k =="o":
    end()
  if mo == 1 and m =="o":
    end()
  if oo == 1 and o =="o":
    end()
  if qo == 1 and q =="o":
    end()
  if so == 1 and s =="o":
    end()
    
def move_bird():
  global move
  global ove
  global a
  global c
  global e
  global g
  global i
  global k
  global m
  global o
  global q
  global s
  ove = ove - 1
  movem = input ("")
  if movem == (" "):
    ove = 2
  move = ove + move
  if move == 9:
    a = "o"
  else:
    a = " "
  if move == 8:
    c = "o"
  else:
    c = " "
  if move == 7:
    e = "o"
  else:
    e = " "
  if move == 6:
    g = "o"
  else:
    g = " "
  if move == 5:
    i = "o"
  else:
    i = " "
  if move == 4:
    k = "o"
  else:
    k = " "
  if move == 3:
    m = "o"
  else:
    m = " "
  if move == 2:
    o = "o"
  else:
    o = " "
  if move == 1:
    q = "o"
  else:
    q = " "
  if move == 0:
    s = "o"
  else:
    s = " "
  if (move < 0) or (move > 9):
    end()
    
while True:
  printscreen()
  death()
  move_bird()

# test git integration