document.getElementById("promptForm").addEventListener("submit", async function(event) {
    event.preventDefault(); // Prevent form from submitting the traditional way

    // Get values from the form
    const prompt = document.getElementById("prompt").value;
    const filename = document.getElementById("filename").value || "generated_image.png"; // Default filename if not provided

    // Prepare the request payload
    const payload = {
        prompt: prompt,
        filename: filename
    };

    try {
        // Send POST request to backend API
        const response = await fetch("http://localhost:8000/generate", {
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

        // Display the image
        const resultDiv = document.getElementById("result");
        const generatedImage = document.getElementById("generatedImage");
        generatedImage.src = imageUrl;
        resultDiv.style.display = "block"; // Show the result section
    } catch (error) {
        alert(error.message);
    }
});
