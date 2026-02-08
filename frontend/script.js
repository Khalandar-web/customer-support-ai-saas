async function sendMessage() {
  const message = document.getElementById("message").value;

  try {
    const response = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message })
    });

    const data = await response.json();
    document.getElementById("reply").innerText =
      data.reply || JSON.stringify(data);

  } catch (error) {
    console.error(error);
    document.getElementById("reply").innerText =
      "❌ Cannot reach backend";
  }
}
