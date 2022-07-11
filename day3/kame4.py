import turtle
t=turtle.Turtle()
t2=turtle.Turtle()

t.shape('turtle')
for _ in range(5):
    t.forward(100)
    t.right(144)

t2.shape('turtle')
t2.setposition(100,100)
for _ in range(5):
    t2.color('blue')
    t2.forward(400)
    t2.right(144)
turtle.mainloop()

