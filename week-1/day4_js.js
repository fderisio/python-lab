const s1 = "hola" // typeof string
const s2 = new String("hello") // typeof object porque usa el constructor

// prototypes vs constructor
function Book (title, author, year) {
    this.title = title
    this.author = author
    this.year = year
}
// de esta manera no satura el constructor con metodos activos para cada instancia
// en vez de generar el metodo dentro del constructor
Book.prototype.getAuthor(){
    return `The author of {$this.title} is {$this.author}`
}

// Inheritance usa un constructor dentro de otro (colocando los metodos dentro del prototype no los hereda)
function Podcast(title, author, year, month){
    Book.call(this, title, author, year, month)
    this.month = month
}

Podcast.prototype = Object.create(Book.prototype) // hereda los metodos del prototype del objeto

// ES6
class Car {
    constructor(brand, model, year){
        this.brand = brand
        this.model = model
        this.year = year
    }
    getBrand(){ // method in the prototype
        return `Brand of the car is {$this.brand}`
    }
}
const car1 = new Car ("BMW", "i8", 2018)

// Inheritance ES6
class eCar extends Car{
    constructor(brand, model, year, battery){
        super(brand, model, year)
        this.baterry = battery
    }
}

