let X = 0
while (X < 10) {
    X++;
    if (X === 2) {
        continue;
    }
    if (X === 9) {
        break
    }
    console.log(X);
}