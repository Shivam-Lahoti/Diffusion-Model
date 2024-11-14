document.getElementById("promptForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const prompt = document.getElementById("prompt").value;
    const filename = document.getElementById("filename").value || "generated_image.png";

    console.log("Submitting prompt:", prompt);
    console.log("Using filename:", filename);

    const payload = { prompt: prompt, filename: filename };

    try {
        console.log("Sending request to backend...");
        const response = await fetch("http://127.0.0.1:8000/generate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        console.log("Response received:", response);
        if (!response.ok) {
            throw new Error("Error generating image");
        }

        const blob = await response.blob();
        const imageUrl = URL.createObjectURL(blob);
        
        console.log("Image URL:", imageUrl);
        
        document.getElementById("result").style.display = "block";
        document.getElementById("generatedImage").src = imageUrl;
    } catch (error) {
        console.error("Error:", error);
        alert(error.message);
    }
});
