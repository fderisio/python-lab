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



