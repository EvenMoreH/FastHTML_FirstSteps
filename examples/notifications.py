import asyncio
from datetime import datetime, timedelta
from fasthtml.common import *

app, rt = fast_app()

# Mock task list with due times
tasks = [
    {"id": 1, "title": "Buy groceries", "notify_at": datetime.now() + timedelta(seconds=10)},
    {"id": 2, "title": "Write report", "notify_at": datetime.now() + timedelta(seconds=20)},
]

# SSE generator to send notifications at the correct time
async def task_notifications():
    while tasks:  # Continue as long as there are tasks
        now = datetime.now()
        for task in tasks[:]:  # Iterate over a copy to allow safe removal
            if now >= task["notify_at"]:  # Check if it's time to notify
                yield sse_message(f"Task Notification: {task['title']} is due!")
                tasks.remove(task)  # Remove task after notification
        await asyncio.sleep(1)  # Check every second

@rt("/notifications")
async def notifications():
    return EventStream(task_notifications())

@rt("/")
def home():
    content = """
    <script>
        const eventSource = new EventSource("/notifications");
        eventSource.onmessage = function(event) {
            alert(event.data);  // Show notification
        };
    </script>
    <h1>Task List</h1>
    <ul>
        <li>Buy groceries (notified in 10 seconds)</li>
        <li>Write report (notified in 20 seconds)</li>
    </ul>
    """
    return Titled("Task Notifications", NotStr(content))

serve()