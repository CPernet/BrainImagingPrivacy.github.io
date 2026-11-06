# Contributing

## Suggest evidence or corrections

Use the repository's **Submit evidence** or **Website correction** issue template. Include the relevant page/data type, a source, the conditions under which a finding applies, and the change proposed. Do not upload confidential information, direct identifiers or restricted participant data.

## Edit content

1. Create a branch or fork.
2. Edit the relevant Markdown file in `docs/`. The metadata uses TOML between `+++` delimiters; the remaining content uses Markdown.
3. Build and check using the commands in the root README.
4. Open a pull request explaining the change and its evidence.

Scientific guidance changes need review by an appropriate subject expert; jurisdiction-specific interpretations need legal review. Explicitly distinguish empirical findings, expert judgement and proposed guidance. Draft content must remain labelled until reviewed. A source's presence on the site does not imply endorsement of every statement in it.

## Review records

For each approved substantive revision, add a dated entry to `CHANGELOG.md` identifying the page, reviewer(s), supporting sources and reason for the change. Do not silently replace the published expert ratings when new evidence is submitted: document the reassessment and preserve the original analysis.

## Add a paper

Create `papers/<short-name>/README.md` containing the citation/status, purpose, named maintainer, authoritative notebook location, data-access instructions and dependencies. Host new analyses in that folder or link to their existing repository. Avoid two editable copies. Keep tools in their own repositories.

For locally hosted notebooks, use paths relative to the paper folder and document how to reproduce the outputs. Record tool versions, random seeds where relevant, and any licensing differences. Publicly shareable data only; large datasets should be linked from an appropriate archive.

## Shared maintenance

Maintainership is not limited to the initial coordinator. Add collaborators and subject reviewers as the group forms. A future `.github/CODEOWNERS` file can assign agreed reviewers to pages and papers; names should only be added with their agreement.
