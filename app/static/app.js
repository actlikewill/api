function getOrders() {
    
    let request = new XMLHttpRequest();
    request.open('GET', 'http://localhost:5000/api/v1/orders')
    request.setRequestHeader('Content-Type', 'application/json')
    request.onload = function () {
        let data = JSON.parse(this.response);
        console.log(data)
    }
    request.send();
    }

getOrders()

function placeOrders() {
    
    let request = new XMLHttpRequest();
    request.open('POST', 'http://localhost:5000/api/v1/orders?item=Burger&quantity=23')
    request.setRequestHeader('Content-Type', 'application/json')
    request.onload = function () {
        let data = JSON.parse(this.response);
        console.log(data)
    }
    request.send();
    }

placeOrders()
