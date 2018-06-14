class Dish {
    constructor(name, price, ingredients){
        this.name = name
        this.price = price
        this.ingredients = ingredients
    }
    cost(){
        let totalCost = 0
        this.ingredients.map(ingredient => {
            totalCost += ingredient.cost
        })
        return totalCost
    }
    profit(){
        return this.price - this.cost()
    }
}

class Restaurant {
    constructor(){
        this.orders = {}
    }
    orderDish(dish, customer){
        this.orders[customer.name] === undefined ? this.orders[customer.name] = [dish] : this.orders[customer.name].push(dish)      
    }
    printOrders(){
        let allOrders = []
        Object.keys(this.orders).map(order => {
            this.orders[order].map(item => allOrders.push(item))
        })
        return allOrders.map((order, index) => {
            return `Order #${index}: ${order.name} \n`
        }).join("")
    }
    printCheck(clientName){      
        let total = 0;
        return `${clientName.name}\n` +
        this.orders[clientName.name].map((order, index) => {
            console.log(order)
            total += order.price
            return `Order #${index}: ${order.name} \n`
        }).join("") + `Total: $${total}\n`
    }
    totalProfit(){
        let allOrders = []
        let result = 0
        Object.keys(this.orders).map(order => {
            this.orders[order].map(item => allOrders.push(item))
        })
        allOrders.map(order => { result += order.profit() })
        return `The profit of the restaurant is $${result}`
    }
    customerProfit(customer){
        let result = 0
        this.orders[customer.name].map(order => { result += order.profit() })
        return result
    }
}

class Ingredient {
    constructor(ingredient, cost){
        this.ingredient = ingredient
        this.cost = cost
    }
}

class Customer {
    constructor (name, id){
        this.name = name;
        this.id = id;
    }
}

// adding ingredients & prices
const cheese = new Ingredient('Cheese', 5);
const pepperoni = new Ingredient('Pepperoni', 2);
const dough = new Ingredient('Dough', 5);
const tomato = new Ingredient('Tomato', 5);
const lettuce = new Ingredient('Lettuce', 5);

// adding dishes
const pizza = new Dish('Pizza', 24, [cheese, pepperoni, dough]);
const salad = new Dish('Salad', 20, [lettuce, cheese, tomato]);

// adding customers
const pluto = new Customer('Pluto', 1);
const goofy = new Customer('Goofy', 2);

// adding restaurant
const restaurant = new Restaurant()

// console.log(pizza.cost()) // => 27
// console.log(pizza.profit()) // => 8
restaurant.orderDish(pizza, pluto);
restaurant.orderDish(salad, pluto);
restaurant.orderDish(salad, goofy);
console.log(restaurant.printOrders());
// console.log(restaurant.printCheck(pluto));
console.log(restaurant.totalProfit())
// console.log(restaurant.customerProfit(pluto))