###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("winter")


q1 = codesters.Square(100, 100, 200, 'blue')
q2 = codesters.Square(-100, 100, 200, 'yellow')
q3 = codesters.Square(-100, -100, 200, 'red')
q4 = codesters.Square(100, -100, 200, 'green')

s1 = codesters.Sprite("tramen", 100, 100)
s1.set_size(0.15)
s2 = codesters.Sprite("yt", -100, -100)
s2.set_size(0.3)
s3 = codesters.Sprite("chess", 100, -100)
s3.set_size(0.65)
s4 = codesters.Sprite("mario", -100, 100)
s4.set_size(0.5)

message1 = codesters.Text("Quinn Rampenthal",0,220,"red")
message1 = codesters.Text("My favorite stuff",0,-220,"red")