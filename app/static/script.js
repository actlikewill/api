function getOrders() {
    const url = `http://localhost:5000/api/v1/orders`

    fetch(url).then(function(response) {
        return response.json();
    }).then(function(data) {
        console.log(data)
    }).catch(function() {
        console.log('error')
    })
    

console.log('app start')
console.log('app running')
}
getOrders()

function placeOrder() {
    url = `http://localhost:5000/api/v1/orders?item=Burger&quantity=10`
    return fetch(url, {
        method: "POST"
    }).then(function(response) {
        return response.json();
    }).then(function(data) {
        console.log(data)
    }).catch(function() {
        console.log('error: could not post')
    })
}

placeOrder()

console.log("async at work")