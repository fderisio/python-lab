"use strict";

const isString = (str) => typeof(str) === "string";
isString('hello'); // => true
isString(['hello']); // => false
isString('this is a long sentence'); // => true
isString({ a: 2 }); // => false

const isArray = (str2) => str2 instanceof Array;
isArray('hello'); // => false
isArray(['hello']); // => true
isArray([2, {}, 10]); // => true
isArray({ a: 2 }); // => false

const areSameType = (str2) => {
    if (str2 instanceof Array) {
        let sameType = typeof str2[0]
        for (let i = 1; i<str2.length; i++) {
            if (typeof str2[i] !== sameType) {
                return false;
            }
        }
        return true
    }
}
areSameType(['hello', 'world', 'long sentence']) // => true
areSameType([1, 2, 9, 10]) // => true
areSameType([['hello'], 'hello', ['bye']]) // => false
areSameType([['hello'], [1, 2, 3], [{ a: 2 }]]) // => true

const longest = (...args) => {
    let str = args.reduce((a, b) => a + b)
    return str.replace(/[^\w\s]|(.)\1/gi, ""); ///(.)(?=.*\1)/g, ""); 
}
console.log(longest('abcccaa', 'acddddffzzz')) // => 'abcdfz'

const convert = (number) => {
    return number.toString().split('').sort().reverse()
}
convert(429563) // => [9, 6, 5, 4, 3, 2]
convert(324) // => [4, 3, 2]

let authors = ['kerouac', 'fante', 'fante', 'buk', 'hemingway', 'hornby', 'kerouac', 'buk', 'fante']
const countRepetitions = (names) => {
    let result = {}
    names.map(item => {
        result.hasOwnProperty(item) ? result[item] += 1 : result[item] = 1
    })
    return result
}
countRepetitions(authors)

const isCaught = (str) => {}

var group = {
    Amy: 20,
    Bill: 15,
    Chris: 10
}
const splitTheBill = (group) => {
    let bill = 0;
    let result = {}
    Object.keys(group).map((key, index) => {
        bill += group[key]
    })
    Object.keys(group).map((key, index) => {
        result[key] = (bill / Object.keys(group).length) - group[key]
    })
    return result
}
splitTheBill(group)

const exp = (a, b) => a ** b
exp(5, 3); // => 125
exp(2, 4); // => 16
exp(5, 1); // => 5
exp(6, 0); // => 1

const factorial = (num) => {
    if (num === 0) { return 1 }
    let result = num
    while (num > 1) {
        result *= (num - 1)
        num --
    }
    return result
}
factorial(5); // => 120
factorial(4); // => 24
factorial(0); // => 1

const fibonacci = (num) => {
    let result = [0, 1]
    if (num === 1) { return [0] }
    while (result.length < num) {
        result.push(result[result.length-1] + result[result.length-2])
    }
    return result
}
console.log(fibonacci(3)); // 0, 1, 1

const confirmEnding = (str1, str2) => 
    str1.substring(str1.length-str2.length, str1.length) === str2;
confirmEnding("Open sesame", "same"); // true

/*diffArray(
    ["andesite", "grass", "dirt", "pink wool", "dead shrub"],
    ["diorite", "andesite", "grass", "dirt", "dead shrub"]
  ) // [ 'pink wool', 'diorite' ]*/

const isAnagram = (str1, str2) => str1 === str2.split("").reverse().join("")
isAnagram('hello', 'olleh'); // => true
isAnagram('world', 'ordly'); // => false
isAnagram('fante', 'tenaff'); // => false

boxVolume(10, 10, 10); // => 1
boxVolume(5, 5, 5); // => 0,125
boxVolume(5, 5, 5.1); // => 0,1275

merge({ a: 3, b: 2 }, { a: 2, c: 4 }); // { a: 3, b: 2, c: 4 }
merge({ a: 3, b: 2 }, { a: 2, c: 4 }, { e: 8, c: 5}); // { a: 3, b: 2, c: 4, e: 8 }

invert({ a: 3, b: 2 }); // { 2: 'b', 3: 'a' }

const obj = {
    'keyCode': 'JS',
    2: 'Program Paradigm',
    Target: 'Browser',
  };
  
  Object.keys(obj); // ['2', 'keyCode', 'Target']

//Write a function that expects two rectangles and returns the intersected rectangle (if any).
//Each rectangle is represented by two points in a two dimensional space.
//For example: [1, 1] and [4, 3]. Is the rectangle with point the corners at [1, 1], [4, 1], [1, 3] and [4, 3].

intersect([[1, 1], [4, 3]], [[2, 2], [6, 7]]); // => [2, 2], [4, 3]
intersect([[2, 1], [4, 4]], [[1, 1], [8, 8]]); // => [4, 4], [2, 1]*/