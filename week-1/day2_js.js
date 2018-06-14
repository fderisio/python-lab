let a=8
if (a=5) {
    console.log("this is true!")
}

console.log(5=="5") // true (== intenta convertir el segundo valor al tipo del primero
console.log(0=="") // true
console.log(0==false) // true
console.log(0==undefined) // false
console.log(0==null) // false
console.log(0==NaN) // false
console.log(typeof null) // object
console.log(typeof undefined) // undefined

let num = 5
num === 5 ? true : false

let i = 0
for ( ; i<5; i++) {
    console.log("do something")
}

let groceryList = ['kiwi', 'apple', 'banana', 'cherries']
for (let item of groceryList){
    console.log(item)
}

const grades = { "Tom": 8, "Anna": 9, "Lucy": 7 }
for (let keys in grades){
    console.log("Student:", keys,"- Grade:", grades[keys])
}
const values = Object.keys(grades) // devuelve array con los values [8, 9, 7])

// do while se va a ejecutar siempre una vez
let ii = 101;
do {
    console.log(ii);
} while (ii < 100);

// Functions
const numfn = function (num) {
    num > 100 ? "num is bigger than 100" : "num is smaller than 100"
}

const myFunc = new Function (num1, num2, console.log("the sum is" + num1+num2))
myFunc(1,2)

var obj1 = {"a":5, "b":3}
var obj2 = {"a":10, "c":7}
var obj3 = Object.assign(obj1, obj2)
console.log(obj3) // reescribe keys iguales

const objES6 = {...obj1, ...obj2};
const {a: value1, b: value2} = obj1; // guarda en una variable con el mismo nombre del key, el valor del key
console.log(value1) // 5

// concatenate lists ES6
let a = [1,2,3]
let b = [...a, 4,5,6]
let c = 9
let d = [...b, ...[c]]

// pasar args ES6
function sum(a,b,c){
    return a+b+c
}
const numArray = [1,2,3]
sum(...numArray) // 6

// arrow fn ES6
const even = (numb) => numb % 2 === 0;
const even = (numb) => {
    return numb % 2 === 0;
}
console.log(even(4))

class Shape {
    constructor (id, x, y) {
        this.id = id
        this.move(x, y)
    }
    move (x, y) {
        this.x = x
        this.y = y
    }
 }



