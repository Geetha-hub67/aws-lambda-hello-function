# AWS Lambda Hello Function

## What I built
I created an AWS Lambda function in Python that returns a styled HTML page with a greeting and the current server time. I gave it a public Function URL and opened it in the browser. The code is in `lambda_function.py`. It reads an optional `?name=` value and escapes it with `html.escape` so visitors can't inject HTML.

## Architecture
```
Browser -> Function URL -> Lambda function (Python) -> HTML response
                                  |
                                  -> CloudWatch Logs
```

## Troubleshooting
- **Symptom:** after I changed the code, the Function URL stopped returning the page and showed a internal server error.
- **Diagnosis:** the browser only said that something failed, so I opened the function's logs in CloudWatch. The newest log stream showed `[ERROR] NameError: name 'name' is not defined`.
- **Cause:** I had renamed a variable on one line, but a later line still used the old name.
- **Fix:** I restored the variable name, deployed again, and the page loaded.

## What I learned
- Browser errors tell me something broke. The logs tell me what and where.
- A `NameError` means the code uses a name that doesn't exist, so I check spelling and line numbers.
- Lambda charges for running time, not for waiting time.
- A function URL with auth type NONE is public, so I deleted it after the lab.

## Clean-up
I removed the Function URL, deleted the function, and deleted its CloudWatch log group.
