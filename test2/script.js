function calculateTip() {
    const bill = (document.getElementById('bill').value);
    const tipPercentage = (document.getElementById('tipPercentage').value);
  
    if (bill > 0 && tipPercentage >= 0) {
      const tipAmount = (bill * tipPercentage) / 100;
      document.getElementById('result').innerText = "Money " + tipAmount;
    }
  }
  