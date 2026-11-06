# Brain Imaging Privacy

A community-maintained website connecting brain imaging privacy evidence with information for researchers, study participants, DPOs and legal professionals, and policymakers.

## Website and local preview

Requires Python 3.11 or newer. Content is Markdown, presentation uses shared HTML templates and CSS. A small Python build converts the content into five static HTML pages; no JavaScript or server is needed to read the generated site.

```bash
cd /run/media/cyril/Data/BrainImagingPrivacy
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-site.txt
python scripts/build_site.py
python scripts/check_site.py
python -m http.server 8000 --directory _site
```

Open http://localhost:8000. Rebuild after editing Markdown, templates or CSS, then refresh the browser. Generated HTML can also be opened directly from `_site/index.html`.

## Edit the site

| Location | Purpose |
| --- | --- |
| `docs/index.md` | Homepage text, audience cards and resource links |
| `docs/researchers.md` | Researcher content |
| `docs/participants.md` | Participant content |
| `docs/legal.md` | DPO and legal content |
| `docs/policy.md` | Policy content |
| `docs/_layouts/` | Shared HTML templates |
| `docs/assets/css/style.css` | Shared styling |
| `scripts/build_site.py` | Markdown-to-HTML build |

Metadata between `+++` delimiters uses TOML. Write the page body in Markdown. Keep relative links such as `researchers.html` so the site works under the repository's Pages path or a future custom domain. The build uses Python rather than Jekyll, avoiding a Ruby dependency for contributors already working with Python notebooks. `_site/` is generated and ignored by Git.

## Papers and tools

- [Expert ratings](papers/expert-ratings/): the existing notebook and survey data, now grouped together. Work in progress; not yet a published paper.
- [metaprivBIDS paper](papers/metaprivbids/): reference and links to the existing OpenNeuro analysis repository. Analyses are maintained there; software remains in its own tool repository.

## GitHub Pages

The workflow builds and checks pull requests. To publish when ready, select **Settings → Pages → Source: GitHub Actions**, then manually run **Build and publish website** from Actions on `main`. This uploads only `_site/`; it does not publish the research folders as website files. It does not deploy on ordinary pushes. No custom domain is configured.

## Contributions and status

See [CONTRIBUTING.md](CONTRIBUTING.md). The audience pages are initial drafts awaiting expert review. Do not interpret them as final consensus recommendations. The initial development is coordinated by [Cyril Pernet](https://github.com/CPernet); additional maintainers and reviewers are welcome.

The existing [MIT license](LICENSE) is retained. Each future paper contribution must identify any different licensing or data-access conditions.
