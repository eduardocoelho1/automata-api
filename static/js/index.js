async function sendJSON(type) {
    let inputData = document.getElementById("jsonInput").value;

    let response = await fetch(`http://127.0.0.1:8000/${type}/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: inputData
    });

    let result = await response.json();
    document.getElementById("response").innerText = JSON.stringify(result, null, 2);
}