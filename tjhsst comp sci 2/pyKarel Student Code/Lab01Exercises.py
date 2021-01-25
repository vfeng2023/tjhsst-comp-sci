#name: Vivian Feng
from pyKarel import *
wld = World()
karel = Robot(wld)

school = World('maze',height = 4, width = 5)
bob = Robot(school)

mv = World("school")
karen = Robot(mv,direction = south,x=1,y=4)

wld.mainloop()
school.mainloop()
mv.mainloop()
