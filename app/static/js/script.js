document.addEventListener('DOMContentLoaded', function () {
    const runBtn = document.getElementById('run-btn');

    runBtn.addEventListener('click', async () => {
        const code = document.getElementById('code-input').value;
        const userInput = document.getElementById('user-input').value;

        const response = await fetch('/run', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                code: code,
                input: userInput
            })
        });

        const result = await response.json();
        document.getElementById('output').textContent = result.output;
    });
});

































// let editor = CodeMirror.fromTextArea(document.getElementById("editor"), {
//     lineNumbers: true,
//     mode: "python",
//     theme: "default"
// });

// function runCode() {
//     const code = editor.getValue();
//     const userInput = document.getElementById("input").value;

//     fetch("/run", {
//         method: "POST",
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({ code: code, input: userInput })
//     })
//     .then(response => response.json())
//     .then(data => {
//         document.getElementById("output").textContent = data.output;
//     });
// }
