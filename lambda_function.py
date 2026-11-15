import html
from datetime import datetime, timezone

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Geetha's Lambda Lab</title>
<style>
  body { margin: 0; min-height: 100vh; display: grid; place-items: center;
         background: #eef4fb; font-family: "Segoe UI", Arial, sans-serif; color: #14213d; }
  .card { width: min(92vw, 480px); background: #fff; border-radius: 10px;
          overflow: hidden; box-shadow: 0 6px 24px rgba(20,33,61,0.15); }
  .band { background: #2f6fed; height: 70px; }
  .body { padding: 22px 28px 28px; }
  h1 { margin: 0 0 8px; font-size: 1.5rem; }
  p { margin: 6px 0; color: #55637d; }
  .tag { background: #fff1cc; padding: 2px 8px; border-radius: 4px; color: #14213d; }
</style>
</head>
<body>
  <div class="card">
    <div class="band"></div>
    <div class="body">
      <h1>Hello from Lambda, NAME!</h1>
      <p>This page was built by a function that ran just now.</p>
      <p>Time on the server: <span class="tag">TIME</span></p>
      <p>Try adding <span class="tag">?name=YourName</span> to the address.</p>
    </div>
  </div>
</body>
</html>"""


def lambda_handler(event, context):
    params = (event or {}).get("queryStringParameters") or {}
    # html.escape stops anyone from sneaking HTML or scripts into the page
    name = html.escape(params.get("name", "Geetha"))
    now = datetime.now(timezone.utc).strftime("%d %b %Y, %H:%M:%S UTC")

    body = PAGE.replace("NAME", name).replace("TIME", now)

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html; charset=utf-8"},
        "body": body,
    }
