import turtle
t=turtle.Turtle()
t2=turtle.Turtle()

t.shape('turtle')
t.color('blue')

t2.shape('turtle')
t2.setposition(100,100)

def make_aquqre(t):
    for i in range(4):
        t.forward(100)
        t.right(90)

def make_spiral(t):
    for i in range(36):
        make_square(t)
        t.right(10)

make_spiral(+1)
t2.right(5)
make=spiral(+2)

turtle.mainloop()
