async function fetchData(type) {
    try {
        let response = await fetch(`http://127.0.0.1:8000/${type}/`);
        let data = await response.json();
        document.getElementById("dfa-data").innerText = JSON.stringify(data, null, 2);
    } catch (error) {
        document.getElementById("dfa-data").innerText = "Error fetching data.";
    }
}

async function checkWord(type) {
    let word = document.getElementById("input").value;
    try {
        let response = await fetch(`http://127.0.0.1:8000/${type}/accept?word=${encodeURIComponent(word)}`);
        let result = await response.json();
        document.getElementById("result").innerText = result["status"];
    } catch (error) {
        document.getElementById("result").innerText = "Error fetching search results.";
    }
}
