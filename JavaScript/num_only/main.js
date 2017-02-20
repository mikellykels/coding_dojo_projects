// Make a function that copies an array, ONLY accepting the items that are numbers.

var numOnly = function(value) {

    var newNumOnly = [];

    for (var i = 0; i < value.length; i++) {
        if (typeof value[i] === "number") {
            newNumOnly.push(value[i]);
        }
    }
    return newNumOnly;
}

var arr = numOnly([1, "apple", -3, "orange", 0.5]);

console.log(arr);
