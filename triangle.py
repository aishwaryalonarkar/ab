#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE

    #if a==0 & b==0 & c==0:
		#raise TriangleError, "Invalid triangle" 
		if a < 1 or b < 1 or c < 1:
			raise TriangleError, "Invalid triangle" 
		if a+b<c or a+c<b or c+b<a:
			raise TriangleError, "Invalid triangle"
	
   

		no_uniq = len(set([a, b, c]))

		return ["equilateral", "isosceles", "scalene"][no_uniq - 1]


# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
	pass
