function printRange(start, end, skip) {
    for (var i = start; i < end; i++) {
        if (end !== undefined && skip !== undefined) {
            console.log(i);
            i = i + skip - 1;
        } else {
            skip = 1;
            console.log(i);
        }
    }
}

printRange(1, 15, 2);
printRange(-50, 15, 3);
printRange(2, 20);
