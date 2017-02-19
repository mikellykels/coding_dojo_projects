/*
Make a function that takes a number of quarters (1 quarter = 1 game).

There is a 1 in 100 chance to win the slot machine (which will give you between 50 - 100 coins - use Math.random and Math.floor to pick a random number of coins).

While the user still has quarters, use Math.random to determine if they won.

If they ever win, return the number of quarters (ex: they had 50 remaining quarters and won 90, so it should return 140).

Return 0 if all the quarters were wasted.
*/

function randomChance(coin) {
    var rand = (Math.trunc(Math.random() * 101) + 1)
    for (var i = coin; i >= 0; i--) {
        var playRand = (Math.trunc(Math.random() * 101) + 1)
        if (playRand === rand) {
            var won = (Math.trunc(Math.random() * 101) + 50)
            var total = won + i;
            console.log("With " + i + " coins left, you won " + won + " coins! You now have " + total + " coins.");
            i = total;
            break;
        }
        else if (i === 0) {
            console.log("You ran out of coins, game over!");
        }
        console.log(i);
    }
    console.log(rand, playRand);
}

randomChance(100);

// Let the user pass the number they are willing to leave with:

function randomChance(coin, max) {
    var rand = (Math.trunc(Math.random() * 101) + 1);
    var total = won + i;
    for (var i = coin; i >= 0; i--) {
        var playRand = (Math.trunc(Math.random() * 101) + 1)
        if (playRand === rand) {
            var won = (Math.trunc(Math.random() * 51) + 50)
            var total = won + i;
            console.log("With " + i + " coins left, you won " + won + " coins! You now have " + total + " coins.");
            i = total;
        }
        else if (i === max) {
            console.log("You have hit your limit, leave now!");
            break;
        }
        else if (i === 0) {
            console.log("You ran out of coins, game over!");
            break;
        }
        console.log(i);
    }
    console.log(rand, playRand);
}

randomChance(25, 50);
