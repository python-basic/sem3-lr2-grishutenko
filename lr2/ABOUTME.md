# Гришутенко Павел
1. Язык программирования С
2. Низкоуровневое программирование на языках ассемблера
3. Обратный инженеринг
## Мое портфолио
https://grishutenko.github.io
## Картинка
![мотивация](ana-juma-sFTMwH2Tvec-unsplash.jpg)
## Площадь треугольника по теореме Герона
```python
import math

def main():
    a = float(input("a : "))
    b = float(input("b : "))
    c = float(input("c : "))

    result = geron_sq(a,b,c)
    print(result)

def geron_sq(a,b,c):
    p = (a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

main()
```
