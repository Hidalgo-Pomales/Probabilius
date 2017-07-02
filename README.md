# Probabilius

## Introduction:

What is Probability and Statistics? Probability and statistics  are sections of mathematics that deal with data collection and analysis. Probability is the study of chance and is a very fundamental subject that we apply in everyday living, while statistics is more concerned with how we handle data using different analysis techniques and collection methods. Probability theory consists of a vast collection of axioms and theorems that provides the scientific community with many contributions, including the naming and description of random variables that occur frequently in applications, the theoretical results associated with these random variables, and the applied results associated with these random variables for statistical applications. Probabilius will be a programing language to solve basic probability and statistics problems. This language will feature some of the most used concepts and formulas from the probability and statistics environment. The user will be able to write down the desired operations such as combinations, permutations, standard deviation, mean and other measurements of dispersion and central tendency. Also, the user will be able to resolve basic probabilities and set theory problems. Probabilius will interpret what the user entered  and display the desired outcome of the calculation. On the other hand, our motivations  and reasons for developing this programming language includes, expanding our knowledge in the Probability and Statistics field, simplify the complex calculations for the user needs, improve performance of the user’s work, challenge ourselves to explore an area outside of our expertise, and develop our critical thinking for problem solving skills. 

[![Watch the video](https://raw.github.com/GabLeRoux/WebMole/master/ressources/WebMole_Youtube_Video.png)](https://youtu.be/amQT-dShGx4)


## Language Features:

* Descriptive Statistics
* Measures of Central Tendency
* Average X
* Median X
* Trimmed Mean
* Mode X
* Measures of Dispersion
* Standard Deviation X
* Variance X
* Range
* Set Theory
* Union X
* Intersection X
* Complement X
* Permutations 
* Total Permutations
* Circular Permutations
* Partial Permutations
* Partial Permutations of Different Kinds of Objects
* Combinations X
* Probabilities 
* Addition, subtraction, multiplication and division of the previously mentioned features.

### Example of a program 
Average:
```javascript
Probalius > avg((10,20)) 
Result:
Probalius > 15
```
Median:
```javascript
Probabilius > median((13, 18, 13, 14, 13, 16, 14, 21, 13))
Result:
Probalius > 14
```
Trimmed Mean: 
```javascript
Probalius > trim(20, (60, 81, 83, 91, 99))
Result: 
Probalius > 85
```
Mode:
```javascript
Probalius > mode((1,2,1,4,5,8,1))
Result:
Probalius > 1
```
Standard Deviation:
```javascript
Probalius > stanDev((600, 470, 170, 430, 300))
Result: 
Probalius > 147
```
Variance:
```javascript
Probalius > var((600, 470, 170, 430, 300))
Result:
Probalius > 21,704
```
Range:
```javascript
Probalius > range((4, 6, 9, 3, 7))
Result:
Probalius > 3
```
Union:
```javascript
Probalius > union((1,2,3,4,5,7),(1,4,8,9))
Result:
Probalius > (1,2,3,4,5,7,8,9)
```
Intersection:
```javascript
Probalius > intersection((1,2,3,4,5,7),(1,4,8,9))
Result:
Probalius > (1,4)
```
Complement:
```javascript
Probalius > comp((1, 2, 4, 6), (1, 2, 4, 6, 7, 8, 9))
Result:
Probalius > (7, 8, 9)
```
Total Permutations:
```javascript
Probalius > totalPer(10)
Result:
Probalius > 90
```
Circular Permutations:
```javascript
Probalius >  cirPer(6)
Result:
Probalius > 120
```
Partial Permutations:
```javascript
Probalius > partial((2,5))
Result: 20
```
Combinations:
```javascript
Probalius > combination((10,2))
Result: 
Probalius > 45
```

## Software Requirements and Specifications
Probabilius will be used to solve basic probability and statistics problems. It will feature some concepts and formulas from the probability and statistics area. The user will be able to write down the desired operations such as combinations, permutations, standard deviation, mean and other measurements of dispersion and central tendency. Probabilius will interpret what the user entered  and display the desired outcome of the operation. We will be using Python for developing our proposed programming language Probabilius. The parsing tool that we will be using PLY, an implementation of lex and yacc which are Python modules. Lex deals with the lexical analysis area, whereas yacc is a module to create the parser for the project. The proposed language will be able to run in any OS that supports Python (e.g. Windows, OS X, Linux).

