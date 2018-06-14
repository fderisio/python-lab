class myMath {
    randomInt(num, num2 = 1){
        return (Math.random() * num) + num2
    }
}

String.prototype.reverse = function() {
    return this.toString().split("").reverse().join("")
}
"hello".reverse()

class Event {
    constructor(location, date){
        this.location = location
        this.date = date
        this.assistants = []
    }
    printInvitation(name){
        return `Dear ${name} \n The event will take place on ${this.date}. Location: ${this.location} `
    }
    confirmAssistance(name){
        let rsvp = prompt("Are you going to attend?", "Yes, of course!", "No, I'm not interested")
        rsvp ? this.assistants.push(name) : "Maybe next time"
    }
    printAssistants(){
        return this.assistants
    }
}
const event1 = new Event('Zürich', new Date(2025, 11, 17), ['Llorenç', 'Colin', 'Laurent']);
console.log(event1.printAssistants())

const event2 = Object.create(Event);
event2.init('Zürich', new Date(2025, 11, 17), ['Llorenç', 'Colin', 'Laurent']);
const  event3 = eventFactory('Zürich', new Date(2025, 11, 17), ['Llorenç', 'Colin', 'Laurent']);

class FamiliarReunion {
    constructor(location, date, familyMembers, ocassion){
        super(location, date)
        this.familyMembers = []
        this.ocassion = ocassion
    }
    welcome(){
        this.familyMembers.map(member => `Welcome ${member}`)
    }
}
