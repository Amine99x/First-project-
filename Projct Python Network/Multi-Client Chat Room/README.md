# First-project-
Network Programming in Python Project


---

## 🚀 How It Works

###  1. Server
- The server listens on `127.0.0.1:59000`.
- When a client connects:
  - It asks for an alias (nickname).
  - Starts a new thread to listen to that client.
  - Broadcasts messages to all connected clients.

###  2. Client
- The user runs `client.py`, enters an alias.
- The client:
  - Listens for incoming messages using a thread.
  - Sends typed messages using another thread.

###  Two threads are used:
- One for **receiving** messages from the server.
- One for **sending** typed messages to the server.

---

## 💻 Run the App

### 1️⃣ Start the server:
```bash
python server.py



## ✅ Step 3: Push to GitHub

1. Create the GitHub repo (name: `chat-room-socket-threading`).
2. In your terminal:

```bash
git init
git add .
git commit -m "Done" 
git push origin main

