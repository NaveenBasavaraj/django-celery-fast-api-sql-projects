var createCounter = function(n){
    return function(){
        return n++;
    };
}

const counter = createCounter(10)
console.log(counter());
console.log(counter());
console.log(counter());
console.log(counter());
console.log(counter());
console.log(counter());

var createCounterLet = function(n){
    let count = n;
    return function(){
        return count++;
    };
}

const counter2 = createCounterLet(10)
console.log(counter2());
console.log(counter2());
console.log(counter2());

class CounterClass{
    constructor(n){
        this.n = n;
    }
    increment(){
        return this.n++;
    }
}
console.log("")
const counterUsingClass = new CounterClass(20);
console.log(counterUsingClass.increment())
console.log(counterUsingClass.increment())
console.log(counterUsingClass.increment())
