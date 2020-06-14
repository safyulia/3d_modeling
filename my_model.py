#!/usr/bin/env python
# coding: utf-8

# In[248]:


from solid import *
from solid.utils import *
from solid import union, cube, translate, rotate, square, circle, polyhedron, polygon
from solid import text, linear_extrude, resize
from solid import difference, intersection, multmatrix, cylinder, color


# In[287]:


#сам корпус одеколона 
s=color([0.85, 0.7, 0.45, 0.5])(cube ([40,18,78])) - color([0.65, 0.67, 0.72, 0.8, 0.5])(translate([2,2,10])(cube([36,14,79])))
#крышка
kr=translate([0,0,78])(polyhedron([[2,2,0],[38,2,0],[38,16,0],[2,16,0],[14,2,6],[26,2,6],[14,16,6],[26,16,6]],[[0,1,2,3],[4,5,7,6],[0,4,5,1],[3,6,7,2],[0,4,6,3],[1,2,7,5]]))
#колпачок
df=translate([20,9,83])(cylinder(40,15,5,5,5))+translate([20,9,83])(cylinder(40,5,6,6,5))
#итог
ode=s+kr+df


# In[288]:


scad_render_to_file(ode, 'D:/3d_modeling/scadfile.scad')


# In[ ]:





# In[ ]:




