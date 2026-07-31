# Contributing

Thanks for helping keep this list useful. A few rules keep it high-signal:

## Adding a tool

1. Open a PR (not just an issue) adding one line in the correct category table, in this format:

   ```
   | [Tool Name](https://link) | Open-source / Commercial | One sentence: who it's best for and why |
   ```

2. No marketing copy — write it the way you'd describe it to a colleague, not the way the vendor's homepage describes it.
3. The tool must be either: (a) actively maintained (a commit or release in the last 6 months), or (b) a widely-used foundational project (e.g. Kubernetes, Prometheus) that AI tools in this space build on.
4. One PR per tool, please — makes review and revert easy.
5. Run `npx awesome-lint` locally before opening the PR; CI will also check this.

## Reporting a dead link or outdated entry

Open an issue or PR — link-check CI runs weekly and will also catch most of these automatically, but manual reports are faster.

## Categories

If your tool doesn't fit an existing category and you think it deserves a new one, propose it in the PR description with 2-3 other tools that would join it. Categories are only added once there are at least 3 solid entries for them.

## Code of Conduct

Participation in this project is governed by the [Code of Conduct](CODE_OF_CONDUCT.md).
