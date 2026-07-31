# Growth & SEO checklist

Practical, ordered steps — not theory. Work top to bottom.

## 1. Repo setup (do this before sharing anywhere)

- [ ] Rename `YOUR_USERNAME` placeholders in `README.md` and `docs/index.html` to your actual GitHub username/repo.
- [ ] Set the repo **description** (top of GitHub repo page) to a keyword-rich one-liner, e.g. *"A curated, searchable directory of AI tools for DevOps, SRE, and Platform Engineering."* — this is what shows in Google search results and GitHub search.
- [ ] Add **topics** on the repo (gear icon next to About): `awesome-list`, `devops`, `sre`, `aiops`, `mcp`, `platform-engineering`, `llmops`, `ai-agents`, `kubernetes`. Topics are how people browsing github.com/topics/devops find you.
- [ ] Enable **GitHub Pages**: Settings → Pages → Source: `main` branch, `/docs` folder. Your searchable site will be live at `https://YOUR_USERNAME.github.io/awesome-ai-sre-devops/`.
- [ ] Enable **Discussions** — Q&A and "which tool should I use for X" threads generate free long-tail content and repeat visits.
- [ ] Add `secrets.GITHUB_TOKEN` is already available by default for the Actions in this repo — no setup needed, but confirm Settings → Actions → General → Workflow permissions is set to "Read and write" so the discovery bot can open PRs.

## 2. SEO specifics

- [ ] The `<meta name="description">` and Open Graph tags are already in `docs/index.html` — just fill in your real repo/username.
- [ ] Google indexes GitHub Pages sites automatically once linked from somewhere; speed this up by submitting the URL in [Google Search Console](https://search.google.com/search-console).
- [ ] Write **one blog post per major category** on your own site/blog (e.g. "The state of AI incident response tools in 2026") that links back to the relevant `#anchor` on your list. This is what actually ranks — GitHub's domain authority helps the repo itself, but long-tail search traffic mostly comes from blog posts, not the list page.
- [ ] Keep the H1/H2 structure exactly as-is (`# Awesome AI SRE & DevOps`, `## Category Name`) — search engines weight headings heavily, and this doubles as your table of contents anchors.

## 3. Distribution (where to actually post it)

- [ ] Submit to [sindresorhus/awesome](https://github.com/sindresorhus/awesome) — the master list of awesome-lists. This is the single highest-leverage backlink in this space.
- [ ] Post to r/devops, r/sre, r/kubernetes (check each subreddit's self-promotion rules first — usually fine if framed as "I built this" with genuine context, not a bare link).
- [ ] Post to Hacker News as "Show HN: Awesome AI SRE & DevOps — a searchable directory of AI infra tools."
- [ ] Share on LinkedIn/X tagged to your personal brand — "why I built this" framing performs better than "here's a list."
- [ ] Submit to relevant newsletter roundups (e.g. DevOps Weekly, SRE Weekly) — most take reader submissions.

## 4. Keeping it "alive" (this is what personal-brand credibility actually runs on)

- [ ] The `discover-tools.yml` workflow runs weekly and opens a PR with candidates — review and merge the good ones every week or two. This keeps your commit history active, which both GitHub's algorithm and human visitors read as a signal of quality.
- [ ] Update the "Tool of the Month" section monthly — small effort, but it's the first thing repeat visitors check.
- [ ] Once you hit ~50-100 stars, add a `CHANGELOG` section to the README (like the reference repo you started from) — visible momentum is itself a growth driver, since people star lists that look alive.

## 5. Personal brand specifics

- [ ] Put your name, a one-line bio, and a link to your site/socials in a short "About the author" section at the bottom of the README — this is direct, low-friction personal-brand payoff from every star/fork.
- [ ] Pin this repo on your GitHub profile.
- [ ] Reference it in your résumé/LinkedIn "Featured" section once it has some traction (stars are a legible signal to recruiters in this space).
