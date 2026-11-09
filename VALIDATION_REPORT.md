# Validation report

## Status and scope

**Class 9 English Medium is complete for the common curriculum and activity books available in the official Samagra Class 9 English-medium filter.** The completed scope contains 11 subjects and all 19 current textbooks/activity books across their available parts. The preserved 2019 ICT Part I is a legacy source and is not counted as a current textbook. No other class or medium was started.

Samagra also lists selectable language-reader and elective alternatives. These are documented in [[Class 9/English Medium/CATALOG_SCOPE]] and excluded from the common curriculum collection because they are choice-based, not simultaneous required titles. The scope note also records selector options with no current PDF link. No Malayalam-medium core textbook was downloaded.

## Identified and verified source PDFs

- 19 current Samagra titles: English (2), Biology (2), Chemistry (2), ICT (2), Mathematics (2), Physical Education (1), Physics (2), Social Science I (2), Social Science II (2), Art Education (1), Work Integrated Education (1).
- 1 legacy ICT Part I (2019), retained unchanged beside the current Samagra 2025 Part I.
- Total local source inventory: 20 PDFs, 1,803 pages. All PDFs open. Each current title was downloaded from or checked against its exact Samagra portal PDF URL. SHA-256 values and edition years are recorded in [[Class 9/English Medium/EDITION_AUDIT]]. Existing files were not overwritten. **Since the 2026-11-05 per-chapter restructure**, PDFs live in the first chapter folder of their part (e.g. `Biology/01 - To Life Processes/Biology Part 1.pdf`); the full PDF placement map is in `scripts/migrate_structure.py` and `SOURCE_CATALOG.json`. PDFs remain git-ignored (`Class 9/English Medium/**/*.pdf`); in a fresh clone they are absent until restored to those folders.
- Current revised core books and activity books carry the 2024 imprint, except ICT Part I/II, which carry 2025. Work Education and Art Education covers identify Standard IX and 2024.

## Reading and generated knowledge notes

Every page of all 19 current PDFs was visually reviewed from the page renders, including text, images, maps, diagrams, tables, exercises, activities and closing inserts. Image-only pages and blank note pages were also visually checked. No OCR was used as a substitute for reading. The archived 2019 ICT Part I is preserved but intentionally not represented as current processed content.

- 92 chapter/unit notes, each with printed page references.
- 96 concept notes, 40 definition notes, 26 formula/rule notes, and 62 exercise/activity guides.
- 18 subject and part overviews.
- 454 Markdown files total across the vault, including indexes, progress/audit documents and navigation.
- **Layout since the per-chapter restructure:** each chapter/unit lives in its own folder named after the chapter note (e.g. `Biology/01 - To Life Processes/`), holding the chapter note plus `Concepts/` and `Questions/`; `Definitions/` and `Formulas/` stay at subject level with `Subject Overview*.md` and canvases.
- 19 Canvas files, one for every current textbook/activity book. Their 421 nodes all reference existing Markdown files; total 614 edges connect notes and meaningful curricular relationships. No Canvas contains informational text nodes.
- Chapter, concept and activity notes include YAML metadata, tags and internal links. The colour legend is consistent across subject overviews and Canvases.

## Validation results

`python scripts/validate_collection.py` completed with **20 PDFs / 1,803 pages, 454 Markdown files, 19 Canvases, 421 Canvas nodes and 614 edges; zero errors and zero warnings** (in the checkout where the PDFs were present). The validator checked PDF opening and page counts, required Markdown frontmatter, wiki-link resolution, Canvas JSON, vault-root file-node targets, edge endpoints and node overlap. After the first report, an Obsidian review found Canvas file paths had been written relative to their folders. All 421 node paths were corrected to vault-root paths (including one incorrectly rooted Chemistry definition path), then checked again in Obsidian; the Chemistry Part I cards now resolve without “New note” or “Swap file” placeholders. All 19 current PDF page ranges are covered by the visual review log; missing pages: **0**. Broken internal links: **0**. After the per-chapter restructure the validator (which now searches PDFs recursively) reports **453 Markdown files, 19 Canvases, 421 nodes, zero errors** plus two warnings in this fresh-clone checkout: no local PDFs present and PDF source links awaiting PDF restoration to the Chapter folders.

Validation scripts and build utilities are in `scripts/`. Structural validation is reproducible; it does not independently judge the pedagogical quality of every generated explanation. Page-to-note coverage is cross-referenced against the visual reviews and chapter lists in the progress log.

## Git and distribution

The source PDFs remain local and are excluded through `.gitignore`; redistribution permission was not established. Git is initialized on `master`. The requested local commit has been created on `master`. No remote is configured, so no push was possible. `.obsidian/workspace.json` and the existing empty `Definitions/Supersaturated Solution.md` remain local and unstaged; textbook PDFs remain ignored.
