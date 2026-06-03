# File Integrity Monitor

A Python tool that uses hashing to detect unauthorized changes to files. Built to learn how hashing works in a practical security context.

## What It Does

- Hashes files and stores a baseline
- Detects if a file has been tampered with by comparing hashes
- Demonstrates the difference between plain hashing, salted hashes, and peppered hashes

## How to Run

```bash
python file_integrity_monitor.py
```

## Example Usage

```
Enter file to monitor: secret.txt
Baseline hash stored.

Re-checking secret.txt...
✔ File integrity verified. No changes detected.

[After modifying the file]

Re-checking secret.txt...
✖ WARNING: File has been modified!
```

## Requirements

- Python 3.x
- No external libraries required (`hashlib` is built-in)

## What I Learned

- How SHA-256 hashing works
- Why plain hashes are vulnerable to rainbow table attacks
- How salting makes each hash unique even for identical inputs
- The difference between salt (stored with hash) and pepper (secret, not stored)
