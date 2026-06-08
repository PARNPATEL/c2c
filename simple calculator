<html>
<script>
function calculate() {
    var a = parseInt(myfrm.txt1.value);
    var b = parseInt(myfrm.txt2.value);
    var op = myfrm.choice.value;
    var c;

    if (op == "sum")
        c = a + b;
    else if (op == "sub")
        c = a - b;
    else if (op == "mul")
        c = a * b;
    else if (op == "div")
        c = a / b;

    myfrm.ans.value = c;
}
</script>

<body>
<form name="myfrm">
    No1 : <input type="text" name="txt1"><br><br>
    No2 : <input type="text" name="txt2"><br><br>

    Choice :
    <select name="choice">
        
        <option value="sum">+</option>
        <option value="sub">-</option>
        <option value="mul">*</option>
        <option value="div">/</option>
    </select>

    <input type="button" value="Calculate" onclick="calculate()">

    <br><br>
    Answer : <input type="text" name="ans" readonly>
</form>
</body>
</html>
