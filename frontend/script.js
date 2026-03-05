let generatedText = "";
let pdfBlobUrl = "";

async function generateContent() {

    const button = document.querySelector(".form-card button");
    button.innerText = "Generating...";
    button.disabled = true;

    const data = {
        content_type: document.getElementById("content_type").value,
        project_name: document.getElementById("project_name").value,
        location: document.getElementById("location").value,
        report_date: document.getElementById("report_date").value,
        topic: document.getElementById("topic").value
    };

    try {
        const response = await fetch("http://127.0.0.1:8000/generate-text", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            const errorText = await response.text();
            alert("Backend Error:\n" + errorText);
            throw new Error(errorText);
        }

        const result = await response.json();

        if (!result.generated_text) {
            alert("AI returned empty response");
            return;
        }

        generatedText = result.generated_text;

        document.getElementById("textPreview").value = generatedText;
        document.getElementById("generatePdfBtn").style.display = "block";

    } catch (err) {
        console.error("Error:", err);
        alert("Connection or Server Failed.\nCheck backend terminal.");
    }

    button.innerText = "Generate Content";
    button.disabled = false;
}

document.getElementById("generatePdfBtn").onclick = async function () {

    try {
        const response = await fetch("http://127.0.0.1:8000/generate-pdf", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: generatedText })
        });

        if (!response.ok) {
            const errorText = await response.text();
            alert("PDF Error:\n" + errorText);
            return;
        }

        const blob = await response.blob();
        pdfBlobUrl = window.URL.createObjectURL(blob);

        document.getElementById("downloadBtn").style.display = "block";

    } catch (err) {
        console.error("PDF error:", err);
        alert("PDF generation failed.");
    }
};

document.getElementById("downloadBtn").onclick = function () {
    const a = document.createElement("a");
    a.href = pdfBlobUrl;
    a.download = "Construction_Content.pdf";
    a.click();
};