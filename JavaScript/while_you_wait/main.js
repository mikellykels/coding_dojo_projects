var daysUntilMyBirthday = 60;

for (var i = 60; i >= 0; i--) {
    if (i >= 30) {
        console.log(i + " Days until my birthday. Such a long time :(");
    }
    else if (i < 30) {
        console.log(i + " DAYS UNTIL MY BIRTHDAY!!!");
    }
}
console.log("It's my birthday!!!!");

while (daysUntilMyBirthday >= 0) {
    if (daysUntilMyBirthday >= 30) {
        console.log(daysUntilMyBirthday + " Days until my birthday. Such a long time :(");
        daysUntilMyBirthday --;
    }
    else if (daysUntilMyBirthday < 30) {
        console.log(daysUntilMyBirthday + " DAYS UNTIL MY BIRTHDAY!!!");
        daysUntilMyBirthday --;
    }
}
console.log("IT'S MY BIRTHDAY!");
