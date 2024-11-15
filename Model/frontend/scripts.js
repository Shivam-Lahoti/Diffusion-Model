document.getElementById("promptForm").addEventListener("submit", async function (event) {
    event.preventDefault(); // Prevent default form submission

    const prompt = document.getElementById("prompt").value;
    const filename = document.getElementById("filename").value || "generated_image.png";

    const payload = {
        prompt: prompt,
        filename: filename,
    };

    // Show loading animation
    const loadingMessage = document.getElementById("loadingMessage");
    const resultDiv = document.getElementById("result");
    const generatedImage = document.getElementById("generatedImage");
    loadingMessage.style.display = "block"; // Show loading
    resultDiv.style.display = "none"; // Hide result

    try {
        // Send POST request to backend
        const response = await fetch("http://127.0.0.1:8000/generate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(payload),
        });

        if (!response.ok) {
            throw new Error("Error generating image");
        }

        // Get the final image path
        const data = await response.json();
        const imageUrl = `http://127.0.0.1:8000/${data.imagePath}`;

        // Hide loading and show result
        loadingMessage.style.display = "none";
        generatedImage.src = imageUrl;
        resultDiv.style.display = "block";
    } catch (error) {
        console.error("Error:", error);
        alert("Failed to generate image. Please try again.");
        loadingMessage.style.display = "none";
    }
});
