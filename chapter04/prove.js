let prove = (n) => {
    console.log(`今からP(${n})が成り立つことを証明します`);
    k = 0;
    console.log(`ステップ1により、P(${k})が成り立ちます`);
    while( k < n ){
        console.log(`ステップ2により、P(${k})が成り立つならばP(${k+1})も成り立つと言えます`);
        console.log(`したがって、P(${k+1})が成り立つと言えます`);
        k = k + 1;
    }
    console.log(`以上で証明が終わりました。`);

}

//prove(2)
prove(100)
