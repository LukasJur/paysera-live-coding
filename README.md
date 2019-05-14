# paysera-live-coding
Coding tasks for paysera 
Source: https://github.com/romasnavasinskas/paysera-live-coding
# Original assignment
# 1. Our football team finished the championship. The result of each match look like "x:y". Results of all matches are recorded in the collection.

For example: `["3:1", "2:2", "0:1", ...]`

Write a function that takes such collection and counts the points of our team in the championship. Rules for counting points for each match:

```
if x>y - 3 points
if x<y - 0 point
if x=y - 1 point
```

Notes: there are 10 matches in the championship
```
0 <= x <= 4
0 <= y <= 4
```


---


# 2. Given an array arr of strings complete the function landPerimeter by calculating the total perimeter of all the islands. Each piece of land will be marked with 'X' while the water fields are represented as 'O'. Consider each tile being a perfect 1 x 1piece of land. Some examples for better visualization:

```
['XOOXO',
 'XOOXO',
 'OOOXO',
 'XXOXO',
 'OXOOO']
``` 

![Image](https://i.snag.gy/ZOQYs2.jpg)

should return: "Total land perimeter: 24", 

while

```
['XOOO',
 'XOXO',
 'XOXO',
 'OOXX',
 'OOOO']
```

![Image](https://i.snag.gy/Kv9BEz.jpg)

should return: "Total land perimeter: 18"

Good luck!


---


# 3. Consider having a cow that gives a child every year from her fourth year of life on and all her subsequent children do the same.

After n years how many cows will you have?

```
countCows(0); // should equal 1
countCows(1); // should equal 1
countCows(3); // should equal 2
countCows(4); // should equal 3
countCows(10);// should equal 28
```
Return null if n is not an integer.

Note: Assume all the cows are alive after n years.
