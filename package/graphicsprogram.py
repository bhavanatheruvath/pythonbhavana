from graphics.rectangle import area as r_area,perimter as r_perimeter
from graphics.circle import area as c_area, circumference as c_circumference
from graphics.threedgraphics.cuboid import area as cub_area, perimeter as cub_perimeter
from graphics.threedgraphics.sphere import area as s_area,circumference as s_circumference

print("Area of rectangle : ",r_area(4,5))
print("Perimeter of rectangle : ",r_perimeter(4,5))

print("Area of circle: ",c_area(3))
print("Circumference of circle: ",c_circumference(3))

print("Area of cuboid: ",cub_area(2,2,4))
print("Perimeter of cuboid: ",cub_perimeter(2,2,4))

print("Area of sphere: ",s_area(4))
print("Circumference of sphere: ",s_circumference(4))

