class Person {
    constructor(firstName, lastName, isAlive){
        this.firstName = firstName
        this.lastName = lastName
        this.isAlive = isAlive
    }
    greet(){
        return `Hello this is ${firstName} ${lastName}`
    }
}

class Writer extends Person {
    constructor(firstName, lastName, isAlive, pseudonym){
        super(firstName, lastName, isAlive)
        this.pseudonym = firstName.concatenate(lastName).split("").revers().join("")
    }
    signBook(){

    }

}

class Developer extends Person {
    constructor(firstName, lastName, isAlive, codename){
        super(firstName, lastName, isAlive)
        this.codename = codename
    }
    impress(){
        return `01 \n 01 \n 01 \n 01 \n 01 \n ${this.codename}`
    }   
}
const laurent = new Developer('Laurent', 'Hoxhaj', 'yes', 'Ping Pong King');
//console.log(laurent.impress())

class Singer extends Person {
    constructor(firstName, lastName, isAlive, melody){
        super(firstName, lastName, isAlive)
        this.melody = melody
        this.artisticName = "Fancy", firstName, lastName
    }
    sing(){
        return this.melody.repeat(3)
    }   
}
const singer1 = new Singer ("Katy", 'Perry', 'Yes', 'Lalala')
//console.log(singer1.sing())

class JuniorDeveloper extends Developer {
    constructor(firstName, lastName, isAlive, codename){
        super(firstName, lastName, isAlive)
        this.codename = codename
        this.isStrugling = true
    }
    complain(){
        return this.codename.upperCase()
    } 
    workHard(){
        let str = `${this.codename} is working hard. `
        return str.repeat(10)
    }  
}
const junior1 = new JuniorDeveloper('fio', 're', 'yes', 'fr')
console.log(junior1.workHard())