# 5. Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

Ax = int(input('Введите координаты точки A по оси х :'))
Ay = int(input('Введите координаты точки A по оси y :'))

Bx = int(input('Введите координаты точки B по оси х :'))
By = int(input('Введите координаты точки B по оси y :'))

AB = round(((Bx-Ax)**2 + (By-Ay)**2)**0.5 , 3)

print(f'Расстояние между точками А({Ax},{Ay}) и B({Bx},{By} = {AB}')

