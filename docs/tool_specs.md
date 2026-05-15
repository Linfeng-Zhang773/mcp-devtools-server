# DevTools MCP Server – Tool Specifications

## Conventions

- All tools return either successful `result` data or a structured error object
- All file paths are relative to a configured `repo_root` (passed as parameter)
- All tools are async-capable internally; long operations have a default 30s timeout

## Error Schema

Every tool that can fail should return on error:
```json
{
  "error": {
    "type": "user_error" | "tool_error" | "system_error",
    "code": "<short_code>",
    "message": "<human readable>",
    "details": {...}        // optional structured info
  }
}
```

## 1. code_search

Hybrid keyword + AST-aware search across a code repository.

Input:
- `repo_path: str` – absolute path to repo root
- `query: str` – keyword/regex pattern to search for
- `file_types: list[str] = ["py"]` – file extensions to include
- `scope: "any" | "function" | "class" = "any"` – AST-level filter (Python only)
- `max_results: int = 50`

Output:
```json
{
  "matches": [
    {
      "file": "src/auth/login.py",
      "line_number": 42,
      "line_content": "def login(username, password):",
      "context": ["..3 lines before..", "..matched line..", "..3 lines after.."],
      "enclosing_symbol": "login"   // function/class name if applicable
    }
  ],
  "total_count": 12
}
```

Errors: user_error.invalid_repo, tool_error.ripgrep_failed

## 2. git_history

Query commit history for a file or symbol.

Input:
- `repo_path: str`
- `file_path: str` – path relative to repo
- `max_commits: int = 20`
- `since_days: int | None = None`

Output:
```json
{
  "commits": [
    {
      "sha": "abc123",
      "author": "Alice",
      "date": "2026-04-15T10:30:00Z",
      "message": "fix: handle null user in login",
      "files_changed": 3
    }
  ]
}
```

Errors: user_error.not_a_repo, user_error.file_not_found

## 3. run_static_analysis  (Day 2)

Wraps pylint / mypy / bandit. Returns unified issue list.

## 4. run_tests  (Day 2)

Runs pytest in Docker sandbox.

## 5. lookup_docs  (Day 2)

Searches local docs and docstrings.
