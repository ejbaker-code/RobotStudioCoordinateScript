# RobotStudioCoordinateScript
This Python script takes a tab delimited text file of coordinates [x \t y \t z, new line for each coordinate] and outputs a text file with RobotStudio code using MoveL offset from a preset "origin point" to move to each point (starting at the origin, ending at the origin).

The coordinate text file from my project is included, as are the text files output by the code.

This was created for use with an ABB IRB 140 robot. Change file names, origin point, toolpen names, and workspace names as needed; the original ones are specific to my project.

AUTHOR: Elliot Baker
Created for ENGR100 class, April 2021.
