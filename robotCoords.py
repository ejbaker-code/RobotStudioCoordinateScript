#takes tab delimited coordinates from robotcoords.txt, formats into RobotStudio code file robotcode.txt to move robot to specified coordinates

import csv
import os
coords = open ('bluerobotcoords.txt')
reader = csv.reader(coords, delimiter='\t')
d = list(reader)
coords.close()
robotcode = open("bluerobotcode.txt", "w")
tab = "\t"
v1 = 0
v2 = 0
v3 = 0
movel = "MoveL Offs(p10,VAR1,VAR2,VAR3), V200, fine, toolpen\WObj:=whiteboard;"
movep10 = "MoveL p10, v200, fine, toolpen\WObj:=whiteboard;"
varset = "VAR1 := " + str(v1) + "; VAR2 := " + str(v2) + "; VAR3 := " + str(v3) + ";"
robotcode.write("MODULE MainModule \n \t")
robotcode.write("CONST robtarget p10:=[[469.36,-103.94,412.05],[0.719835,-0.0230894,0.692629,0.0396127],[-1,-1,0,1],[9E+9,9E+9,9E+9,9E+9,9E+9,9E+9]]; \n \t")
robotcode.write("PROC main() \n \t \t")
robotcode.write(movep10)
robotcode.write("\n\t\t\t" + varset + "\n\t\t" + movel)
#coord_data  = open("robotcoords.txt", newline='\t')
#v1 = coord_data.read()
#print("v1 is : ", v1)
#v2 = coord_data.read()
#print("v2 is : ", v2)
#v3 = coord_data.read()
#print("v3 is : ", v3)
#coord_data.close()
for co in d:
    v1 = co[0]
    v2 = co[1]
    v3 = co[2]
    varset = "VAR1 := " + str(v1) + "; VAR2 := " + str(v2) + "; VAR3 := " + str(v3) + ";"
    robotcode.write("\n\t\t\t" + varset + "\n\t\t" + movel)
robotcode.write("\n\t\t"+movep10)
robotcode.write("\n\t ENDPROC \n ENDMODULE")
robotcode.close()

#takes tab delimited coordinates from robotcoords.txt, formats into RobotStudio code file robotcode.txt to move robot to specified coordinates

coords = open ('spirocoords.txt')
reader = csv.reader(coords, delimiter='\t')
d = list(reader)
coords.close()
robotcode = open("spirocode.txt", "w")
tab = "\t"
v1 = 0
v2 = 0
v3 = 50
movel = "MoveL Offs(p10,VAR1,VAR2,VAR3), V200, fine, toolpen\WObj:=whiteboard;"
movep10 = "MoveL p10, v200, fine, toolpen\WObj:=whiteboard;"
varset = "VAR1 := " + str(v1) + "; VAR2 := " + str(v2) + "; VAR3 := " + str(v3) + ";"
robotcode.write("MODULE MainModule \n \t")
robotcode.write("CONST robtarget p10:=[[469.36,-103.94,412.05],[0.719835,-0.0230894,0.692629,0.0396127],[-1,-1,0,1],[9E+9,9E+9,9E+9,9E+9,9E+9,9E+9]]; \n \t")
robotcode.write("PROC main() \n \t \t")
robotcode.write(movep10)
robotcode.write("\n\t\t\t" + varset + "\n\t\t" + movel)
for co in d:
    v1 = co[0]
    v2 = co[1]
    v3 = co[2]
    varset = "VAR1 := " + str(v1) + "; VAR2 := " + str(v2) + "; VAR3 := " + str(v3) + ";"
    robotcode.write("\n\t\t\t" + varset + "\n\t\t" + movel)
robotcode.write("\n\t\t"+movep10)
robotcode.write("\n\t ENDPROC \n ENDMODULE")
robotcode.close()

