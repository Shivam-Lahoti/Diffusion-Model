document.getElementById("promptForm").addEventListener("submit", async function(event) {
    event.preventDefault(); // Prevent form from submitting the traditional way

    const prompt = document.getElementById("prompt").value;
    const filename = document.getElementById("filename").value || "generated_image.png";

    const payload = {
        prompt: prompt,
        filename: filename
    };

    // Show loading message
    const loadingMessage = document.getElementById("loadingMessage");
    loadingMessage.style.display = "block";

    try {
        // Send POST request to backend API
        const response = await fetch("http://127.0.0.1:8000/generate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        // Check if the response is OK
        if (!response.ok) {
            throw new Error("Error generating image");
        }

        // Convert response to blob to display as image
        const blob = await response.blob();
        const imageUrl = URL.createObjectURL(blob);

        // Hide loading message
        loadingMessage.style.display = "none";

        // Display the generated image
        const resultDiv = document.getElementById("result");
        const generatedImage = document.getElementById("generatedImage");
        generatedImage.src = imageUrl;
        resultDiv.style.display = "block"; // Show the result section
    } catch (error) {
        console.error("Error:", error);
        alert(error.message);
        // Hide loading message in case of error
        loadingMessage.style.display = "none";
    }
});
