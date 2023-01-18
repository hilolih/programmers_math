let union = (setA, setB)  => {
    let _union = new Set(setA)
    for (let elem of setB) {
        _union.add(elem)
    }
    return _union
}

let intersection = (setA, setB)  => {
    let _intersection = new Set()
    for (let elem of setB) {
        if (setA.has(elem)) {
            _intersection.add(elem)
        }
    }
    return _intersection
}

n2bai = new Set([2,4,6,8,10,12])
n3bai = new Set([3,6,9,12])
