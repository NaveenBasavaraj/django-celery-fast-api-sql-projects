//node print_something.js

const createHelloWorld = function() {
    return function(...args) {
        return "Hello World";
    }();
}

const helloFunction = createHelloWorld(); // Call the outer function to get the inner function
//const result = helloFunction(); // Call the inner function

console.log(helloFunction); // Output: "Hello World"


console.log(add(1,2))

function add(a,b){
    return a+b;
};

let a = [1,2];
let b = [3,4];

console.log([...a, ...b])

function addlist(...args){
    //return args[0] + args[1];
    console.log(args[0] + args[1]);
}

console.log(addlist(8,2));