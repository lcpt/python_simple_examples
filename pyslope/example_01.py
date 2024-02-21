# -*- coding: utf-8 -*-
'''PySlope simple example.

Based on: https://pyslope.readthedocs.io/en/latest/examples.html
'''

import pyslope

s= pyslope.Slope(height=3, angle=30, length=None)


# Material defined with key word arguments
m1= pyslope.Material(unit_weight=20, friction_angle=45, cohesion=2, depth_to_bottom=2)
# Material defined with positional arguments
m2= pyslope.Material(20, 30, 2, 5)
s.set_materials(m1, m2)

# Loads
u1= pyslope.Udl(magnitude = 100, offset = 2, length = 1)

# by default offset = 0 (m) and length = None.
u2= pyslope.Udl(magnitude = 20)

# assign uniform loads to model
s.set_udls(u1, u2)

# define line load, similiar to Udl except there is no length parameter and magnitude is in units (kN/m)
p1= pyslope.LineLoad(magnitude = 10, offset = 3)

# assign line loads to slope
s.set_lls(p1)

s.set_water_table(4)

s.plot_boundary()
s.set_analysis_limits(s.get_top_coordinates()[0] - 5, s.get_bottom_coordinates()[0] + 5)

# The user can change the number of slices and iterations with the method below.
# The line below is implicitly called and only required by the user if they want to change iterations
s.update_analysis_options(
    slices=50,
    iterations=2500,
    tolerance=0.005,
    max_iterations=50
)

# run analysis
s.analyse_slope()

# print out minimum calculated factor of safety
print(s.get_min_FOS())
fg1= s.plot_boundary()
fg1.write_image('fg1.svg')
fg2= s.plot_critical()
fg2.write_image('fg2.svg')
fg3= s.plot_all_planes(max_fos=2)
fg3.write_image('fg3.svg')
