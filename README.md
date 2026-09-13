# Master Copywriter

A Claude Code skill: writes, rewrites and critiques selling copy at a 5th grade reading level, drawing on a bundled library of 14 direct response books (distilled and in full) that it reads and cross-references before drafting. Hooks, headlines, bullets, leads, sales letters, VSLs, emails, ads, landing pages, advertorials, offers, guarantees, full funnels.

## Install

```bash
git clone https://github.com/arichardgit/master-copywriter.git ~/master-copywriter && ln -sfn ~/master-copywriter/skills/master-copywriter ~/.claude/skills/master-copywriter
```

Start a new Claude Code session and type `/master-copywriter`, or just ask for copy; it triggers on its own.

## Layout

```
skills/master-copywriter/
  SKILL.md                     the working instructions
  references/INDEX.md          map of the library and routing table
  references/books/            fourteen dense distillations
  references/doctrine.md       where the authors agree, disagree, and how to resolve it
  references/awareness-alignment.md
  references/source/           full text of the fourteen books as structured JSON
  scripts/check_copy.py        reading level, AI tells, buzzwords, dashes, passive voice
```

The creative-strategy repo bundles a copy of this skill; this repo is the standalone version.
