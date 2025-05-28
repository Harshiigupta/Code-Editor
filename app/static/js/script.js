let editor = CodeMirror.fromTextArea(document.getElementById("editor"), {
    lineNumbers: true,
    mode: "python",
    theme: "default"
});

function runCode() {
    const code = editor.getValue();
    const userInput = document.getElementById("input").value;

    fetch("/run", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ code: code, input: userInput })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("output").textContent = data.output;
    });
}