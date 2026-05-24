#!/usr/bin/env bash
# Sets up symlinks from ~/.claude/{commands,templates} to this repo.
# Run once after cloning, and re-run whenever files are added.
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"

# Each context dir may contain commands/*.md and templates/*.md.
# general/templates: hotfix-template.md
for context in personal work general; do
  for f in "$REPO_DIR/$context/commands/"*.md; do
    ln -sfv "$f" "$HOME/.claude/commands/$(basename "$f")"
  done
  for f in "$REPO_DIR/$context/templates/"*.md; do
    ln -sfv "$f" "$HOME/.claude/templates/$(basename "$f")"
  done
done

echo "Done. Symlinks created in ~/.claude/commands/ and ~/.claude/templates/"
