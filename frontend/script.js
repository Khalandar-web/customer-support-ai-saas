async function sendMessage() {
  const message = document.getElementById("message").value;

  const response = await fetch("http://backend:8000/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ message })
  });

  const data = await response.json();

  // 👇 MUST MATCH id="reply"
  document.getElementById("reply").innerText = data.reply;
}
