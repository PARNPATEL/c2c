<!DOCTYPE html>
<html>
<head>
    <title>GST Calculator</title>

    <script>
        function calculateGST() {

            var amount = parseFloat(document.getElementById("amount").value);
            var rate = parseFloat(document.getElementById("gstRate").value);

            var gst = (amount * rate) / 100;
            var total = amount + gst;

            document.getElementById("result").innerHTML =
                "Amount: ₹ " + amount.toFixed(2) + "<br>" +
                "GST (" + rate + "%): ₹ " + gst.toFixed(2) + "<br>" +
                "Total: ₹ " + total.toFixed(2);
        }
    </script>

    <style>
        body {
            text-align: center;
            font-family: Times New Roman;
        }

        h1 {
            font-size: 60px;
        }

        label {
            font-size: 40px;
        }

        input, select {
            font-size: 30px;
            padding: 10px;
        }

        button {
            font-size: 30px;
            padding: 10px 20px;
            margin-top: 20px;
        }

        #result {
            margin-top: 30px;
            font-size: 40px;
        }
    </style>
</head>

<body>

    <h1>GST Calculator</h1>

    <label>Enter Amount (in INR):</label>
    <input type="text" id="amount" value="10000">
    <br><br>

    <label>Select GST Rate:</label>

    <select id="gstRate">
        <option value="5">5%</option>
        <option value="12">12%</option>
        <option value="18" selected>18%</option>
        <option value="28">28%</option>
    </select>

    <br><br>

    <button onclick="calculateGST()">
        Calculate GST
    </button>

    <div id="result">
        Amount: ₹ 10000.00 <br>
        GST (18%): ₹ 1800.00 <br>
        Total: ₹ 11800.00
    </div>

</body>
</html>
