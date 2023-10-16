var createCounter = function(init){
    let count = init;
    function increment(){
        return ++count;

    }

    function decrement(){
        return --count;

    }

    function reset(){
        count = init;
        return count;
    }

    return {
        increment: increment,
        decrement: decrement,
        reset: reset,
    }
}

class Counter{
    constructor(init){
        this.init = init;
        this.count = init; 
    }
    increment(){
        return this.count++;
    }
    decrement(){
        return this.count--;
    }
    reset(){
        this.count = init;
        return this.count;
    }
}