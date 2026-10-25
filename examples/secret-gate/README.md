# secret-gate

A small prompt-submit hook that blocks prompts containing likely credentials before they reach the model.

- `secret_gate_hook.py`: the hook. Reads JSON on stdin (`{"prompt": "..."}`), exits 2 with a reason on stderr if it finds a likely secret, otherwise exits 0.
- `test_secret_gate.py`: tests.

## Behavior

- Reports the kind of secret and a three-character masked preview. It never echoes the value.
- Fails open on malformed input.
- Covers AWS access key ids, private key blocks, GitHub tokens, Slack tokens, `sk-` style API keys, and `password=`/`api_key=` style assignments. Add patterns for your own stack.
- Pattern matching produces false positives and misses. It is a guard rail, not a guarantee.

## Run the tests

```
python3 -I test_secret_gate.py -v
```

## Register it

Add it as a prompt-submit hook in your agent's settings. For Claude Code, the shape is roughly:

```json
{
  "hooks": {
    "UserPromptSubmit": [
      { "hooks": [ { "type": "command", "command": "python3 /absolute/path/to/secret_gate_hook.py" } ] }
    ]
  }
}
```

Hook configuration formats change between versions. Check the current documentation for your agent before relying on this snippet, and append to any existing hook entries instead of replacing them.
