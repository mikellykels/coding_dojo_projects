// Write a function that will print index, symbol and name:

function fancyArr(){
    var arr = ["James", "Jill", "Jane", "Jack"];

    for (var i = 0; i < arr.length; i++) {
        console.log(i + " --- " + arr[i]);
    }
}

fancyArr();

// Let the user pass in a symbol that will print:

function fancyArr2(symbol){
    var arr = ["James", "Jill", "Jane", "Jack"];

    for (var i = 0; i < arr.length; i++) {
        console.log(i + " " + symbol + " " + arr[i]);
    }
}

fancyArr2("::");

// Have an extra parameter reversed. If the user passes true, print the elements in reverse order

function fancyArr3(symbol, reversed){
    var arr = ["James", "Jill", "Jane", "Jack"];

    for (var i = 0; i < arr.length; i++) {
        if (reversed == true) {
            arr.reverse();
            console.log(i + " " + symbol + " " + arr[i]);
        } else {
            console.log(i + " " + symbol + " " + arr[i]);
        }
    }
}

fancyArr3("->", true);
