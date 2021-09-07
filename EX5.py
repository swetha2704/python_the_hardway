my_name = 'Zed A. Shaw'
2 my_age = 35;
3 my_height = 74;
4 my_weight = 180 # lbs
5 my_eyes = 'Blue'
6 my_teeth = 'White'
7 my_hair = 'Brown'
8
9 print "Let's talk about %s." % my_name
10 print "He's %d inches tall." % my_height
11 print "He's %d pounds heavy." % my_weight
12 print "Actually that's not too heavy."
13 print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
14 print "His teeth are usually %s depending on the coffee." % my_teeth
15
16 # this line is tricky, try to get it exactly right
17 print "If I add %d, %d, and %d I get %d." % (
18 my_age, my_height, my_weight, my_age + my_height + my_weight)
