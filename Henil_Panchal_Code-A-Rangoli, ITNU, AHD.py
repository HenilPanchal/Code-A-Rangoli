'''
This is Python code to make "HAPPY DIWALI"  text and a  Multi colour Rangoli Hexagon.
In this code Each alphabet is programmed in python along with setting their coordinates and size.
Thus, making  it a Truely code to Graphic Rangoli.

Made by : Henil Shalin Panchal
Institute: Institute of Technology , Nirma University, Ahmedabad.
Email Id: keyuriksppanchal@gmail.com
'''

import turtle    # Using Python's Inbuilt Turtle Library.

t_pen = turtle.Pen();
# Creates Instance of Turtle.
t_pen.speed(speed ='fastest');
turtle.bgcolor('white');# set the background colour "white".

t_pen.pencolor("white");
t_pen.setpos(-300,200);# set postion of turtle pen


t_pen.pencolor("black");
t_pen.width(9);
t_pen.left(90);
t_pen.forward(50);
t_pen.backward(100);
t_pen.forward(50);         # code for "H"
t_pen.right(90);
t_pen.forward(80);
t_pen.left(90);
t_pen.forward(50);
t_pen.backward(100);
t_pen.forward(50);


t_pen.up();
t_pen.setpos(-200,130);
t_pen.down();
t_pen.right(30);              # code for "a"
t_pen.forward(100);
t_pen.right(120);
t_pen.forward(100);
t_pen.backward(50);
t_pen.left(60);
t_pen.backward(50);
t_pen.up();

t_pen.setpos(-80,120);
t_pen.down();
t_pen.left(90);              # code for "p"
t_pen.forward(100);
t_pen.right(90);
t_pen.forward(50);
t_pen.right(90);
t_pen.forward(50);
t_pen.right(90);
t_pen.forward(50);

t_pen.up();


t_pen.setpos(-10,120);
t_pen.down();
t_pen.right(90);              # code for  another "p"
t_pen.forward(100);
t_pen.right(90);
t_pen.forward(50);
t_pen.right(90);
t_pen.forward(50);
t_pen.right(90);
t_pen.forward(50);
t_pen.up();

t_pen.setpos(60,170);
t_pen.down();
t_pen.right(90);
t_pen.forward(50);
t_pen.backward(50);    # code for "y"
t_pen.right(90);
t_pen.forward(50);
t_pen.right(90);
t_pen.forward(50);
t_pen.backward(100);

t_pen.up();

t_pen.setpos(10,70);
t_pen.down();
t_pen.right(90);
t_pen.backward(50);    # code for "d"
t_pen.right(90);
t_pen.backward(70);
t_pen.left(90);
t_pen.forward(50);
t_pen.right(90);
t_pen.forward(70);

t_pen.up();

t_pen.setpos(80,70);
t_pen.down();
t_pen.right(90);
t_pen.forward(40);
t_pen.backward(20);    # code for "i"
t_pen.right(90);
t_pen.forward(70);
t_pen.right(90);
t_pen.forward(20);
t_pen.backward(40);

t_pen.up();

t_pen.setpos(150,70);
t_pen.down();
t_pen.right(90);
t_pen.backward(70);    # code for  "w"
t_pen.right(90);
t_pen.forward(20);
t_pen.left(90);
t_pen.forward(35);
t_pen.backward(35);
t_pen.right(90);
t_pen.forward(20);
t_pen.left(90);
t_pen.forward(70);

t_pen.up();
t_pen.setpos(210,0);
t_pen.down();
t_pen.right(30);              # code for "a"
t_pen.forward(80);
t_pen.right(120);
t_pen.forward(80);
t_pen.backward(50);
t_pen.left(60);
t_pen.backward(30);

t_pen.up();


t_pen.setpos(310,0);
t_pen.down();
t_pen.left(90);        # code for "l"
t_pen.forward(70);
t_pen.backward(80);
t_pen.right(90);
t_pen.forward(40);

t_pen.up();

t_pen.setpos(370,-10);
t_pen.down();
t_pen.forward(40);
t_pen.backward(20);   #code for "i"
t_pen.left(90);
t_pen.forward(70);
t_pen.left(90);
t_pen.forward(20);
t_pen.backward(40);

t_pen.up();

t_pen.setpos(-100,-50);    # set position of multicolour hexagon.
t_pen.down()


colour = ['red','blue', 'green','orange', 'purple', 'yellow'];
# list of colours for the Rangoli Hexagon.

for i in range(120):                  # iterates 120 times to make a complete filled hexagon.
	t_pen.pencolor(colour[i%6]);  # set a specific colour for a side.
	t_pen.width(i//10 +1);        # set linearly  increasing width to fill the hexagon.
	t_pen.forward(i);             # tell the pointer to go forward by ith steps.
	t_pen.left(60);               # turn the pointer to rotate left by  60  degrees.
	

