
//let series_count = 10;
let  current= 0, next = 1, temp;

//you cant do prompt
//you cant do alert
const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

readline.question('How many numbers do you need?', series_count => {
console.log('Fibonacci Series:');

for (let i = 1; i <= series_count; i++) {    
    console.log(current);
    temp = current + next;
    current = next
    next = temp;

} 
  readline.close();
});

