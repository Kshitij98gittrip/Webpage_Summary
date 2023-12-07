const btn = document.getElementById("summarise");
btn.addEventListener("click", function() {
    btn.disabled = true;
    btn.innerHTML = "Summarising...";
    chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
        var url = tabs[0].url;
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "http://127.0.0.1:5000/summary?url=" + url, true);
        xhr.onload = function() {
            var text = xhr.responseText;
            const p = document.getElementById("output");
            p.innerHTML = text;
            btn.disabled = false;
            btn.innerHTML = "Summarise";
            addCopyButton("output");
        }
        xhr.send();
    });
});

const btn1 = document.getElementById("major_points");
btn1.addEventListener("click", function() {
    btn1.disabled = true;
    btn1.innerHTML = "Getting Points...";
    chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
        var url = tabs[0].url;
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "http://127.0.0.1:5000/majorpoints?url=" + url, true);
        xhr.onload = function() {
            var response = JSON.parse(xhr.responseText);  // Parse JSON response
            var points = response.points;
            
            const p = document.getElementById("output1");
            p.innerHTML = '<ul>';
            points.forEach(function(point) {
                p.innerHTML += '<li>' + point + '</li>';
            });
            p.innerHTML += '</ul>';
            btn1.disabled = false;
            btn1.innerHTML = "Major Points";
            addCopyButton("output1");
        }
        xhr.send();
    });
});

function addCopyButton(outputId) {
    const p = document.getElementById(outputId);

    // Create a button for copying
    const copyButton = document.createElement("button");
    copyButton.innerText = "Copy to Clipboard";
    copyButton.addEventListener("click", function () {
        copyToClipboard(p.innerText);
    });

    // Append the copy button to the specified output element
    p.appendChild(copyButton);
}

function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(function () {
        // console.log("Text successfully copied to clipboard");
        alert('Text copied to clipboard!');

    }).catch(function (err) {
        console.error("Unable to copy text to clipboard", err);
    });
}