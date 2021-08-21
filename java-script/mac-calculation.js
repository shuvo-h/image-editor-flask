// getting ID 
function getId(idName) {
    const idElement = document.getElementById(idName);
    return idElement;
}
// getting innerText of ID
function getInnerText(idName) {
    // get the id by calling getID function 
    const targetId = getId(idName);
    return targetId.innerText;
}

// Function to get memory cost 
function memoryPrice(memory) {
    const extraMemoryCost = getId('extra-memory');
    if (memory == '8GB') {
        extraMemoryCost.innerText = '0';
    }else{
        extraMemoryCost.innerText = '180';
    }
    // update the toal cost 
    totalCost();
}

// function to get Storage Cost 
function storagePrice(ssd) {
    const extraStorageCost = getId('extra-storage-cost');
    if (ssd == '256GB') {
        extraStorageCost.innerText = '0';
    }else if (ssd == "512GB") {
        extraStorageCost.innerText = "100";
    }else{
        extraStorageCost.innerText = '180';
    }

    // update the toal cost 
    totalCost();
}

// function to calculate delivery charge 
function deliveryCharge(date) {
    const deliveryCostId = getId('delivery-charge');
    switch (true) {
        case (date == "25th"):
            deliveryCostId.innerText = '0';
            break;

        case (date == "21th"):
            deliveryCostId.innerText = '20';
            break;
    
        default:
            // Nothing to do here just break the loop 
            break;
    }

    // update the toal cost 
    totalCost();
}

// total cost calculation 
function totalCost() {
    // get integer value of all cost 
    const bestPrice = parseInt(getInnerText('best-price'));
    const memoryCost = parseInt(getInnerText('extra-memory'));
    const storageCost = parseInt(getInnerText('extra-storage-cost'));
    const deliveryCost = parseInt(getInnerText('delivery-charge'));

    // summation of all cost 
    const totalPrice = bestPrice + memoryCost + storageCost + deliveryCost;
    
    // Update the total price 
    const totalCostId = getId('total-price');
    totalCostId.innerText = totalPrice;

    // display the total without pomo discount 
    getId('total').innerText = totalPrice;
}

// Calculation of pomo code 
function pomoDiscount() {
    const totalPrice = parseInt(getInnerText('total-price'));
    const totalId = getId('total');

    // verify pomo code 
    const pomoField = getId('pomo-code');
    const pomoValue = pomoField.value;
    const pomoCode = pomoValue.toLowerCase();
    if (pomoCode == 'stevekaku') {
        // reduce 20% of total cost 
        const total = totalPrice - ((totalPrice*20)/100);
        totalId.innerText = total;
        pomoField.value = "";
    }

}

// Event handler for memory
document.getElementById('8GB-memory').addEventListener('click',function () {
   memoryPrice('8GB');
})
document.getElementById('16GB-memory').addEventListener('click',function () {
   memoryPrice('16GB');
})

// Event handler for storage
document.getElementById('256GB-ssd').addEventListener('click', function () {
    storagePrice('256GB');
})
document.getElementById('512GB-ssd').addEventListener('click', function () {
    storagePrice('512GB');
})
document.getElementById('1TB-ssd').addEventListener('click', function () {
    storagePrice('1TB');
})

// Event handler for delivery date 
document.getElementById('delivery-25th').addEventListener('click',function () {
    deliveryCharge('25th');
})
document.getElementById('delivery-21th').addEventListener('click',function () {
    deliveryCharge('21th');
})


// Event handler for pomo code 
document.getElementById('pomo-btn').addEventListener('click',function () {
    pomoDiscount();
})
