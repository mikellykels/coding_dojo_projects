var hour = 6;
var minute = 15;
var period = "PM";

if (hour <= 6) {
    if (minute < 30) {
        if (period === "AM") {
            console.log("It's just after " + hour + " in the morning!");
        }
        else if (period === "PM") {
            console.log("It's just after " + hour + " in the evening!");
        }
    }
    if (minute > 30) {
        if (period === "AM") {
            console.log("It's almost the next hour in the morning!");
        }
        else if (period === "PM") {
            console.log("It's almost the next hour in the evening!");
        }
    }
}
else if (hour > 6) {
    if (minute < 30) {
        if (period === "AM") {
            console.log("It's just after " + hour + " in the morning!");
        }
        else if (period === "PM") {
            console.log("It's just after " + hour + " in the evening!");
        }
    }
    if (minute > 30) {
        if (period === "AM") {
            console.log("It's almost the next hour in the morning!");
        }
        else if (period === "PM") {
            console.log("It's almost the next hour in the evening!");
        }
    }
} else {
    console.log("Who know's what time it is!");
}
