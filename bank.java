lass Bank {
    
    constructor(amount) {
        this.amount = amount;
    }

    
    getBalance() {
        console.log("Balance is: " + this.amount);
    }

    
    deposit(amount) {
        this.amount = this.amount + amount;
    }

    
    withdraw(amount) {
        this.amount = this.amount - amount;
    }
}


let myobj = new Bank(1000);

myobj.getBalance();   // 1000

myobj.deposit(5000);
myobj.getBalance();   // 6000

myobj.withdraw(10000);
myobj.getBalance();   // -4000
