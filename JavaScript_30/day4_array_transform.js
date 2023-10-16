function power(x){
    return Math.pow(x,x);
}

var map = function(arr, fn) {
    return arr.map(fn);
}

const numbers = [2,3,4,5];
// const results = map(numbers, power);

console.log(map(numbers, power));

var mapWithFor = function(arr, fn) { // The strategy design pattern
    const res = []
    for (const i in arr){
        res.push(fn(arr[i],i));
    }
    return res;
};

console.log(mapWithFor(numbers, power));
