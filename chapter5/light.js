let light = () => {
    let total = 0;
    for (let i=1; i <= 13; i++) {
        if ( i % 2 == 0 || i % 3 == 0 ) {
            total += 1;
        }
    }
    return total;
}

