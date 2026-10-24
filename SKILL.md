---
name: paper-source-code-learning
description: >
  A general-purpose workflow for studying research papers and their code
  implementations across machine learning and software domains. Use when
  analyzing a paper, understanding a model or algorithm, tracing source code,
  explaining data flow and tensor shapes, comparing training and inference,
  examining experiments, adapting a method to a new task, or generating an
  interactive HTML architecture explorer with clickable modules and traceable data flow.
---

# Paper & Model Source-Code Learning

Use this Skill to understand the paper and the implementation that is actually present. It is domain-neutral: identify the current research object first, then choose only the methods relevant to it.

## Non-negotiable rules

- Answer the user's current question first; deepen only as much as needed.
- Treat the current paper, repository, configuration, and version as the source of truth for implementation claims.
- Never assume the current project is related to a previously studied model or shares its architecture.
- Do not assume any specific module, operation, loss, training strategy, or post-processing step exists until evidence is found.
- Separate **paper-stated design**, **source-verified implementation**, **experiment-reported result**, and **inference / unverified hypothesis**.
- Never invent filenames, symbols, line numbers, shapes, default values, results, or implementation behavior.
- For source claims, cite repository-relative paths and function/class names; include line ranges only when reliable.
- If available sources cannot establish a claim, state what is missing instead of guessing.
- Use Chinese by default when the user uses Chinese; retain original technical names and identifiers.

## New-project isolation: prevent cross-paper contamination

At the start of every new paper/model task:

1. Re-identify the paper, research problem, task type, repository, framework, version/commit if available, and active configuration.
2. Build a fresh evidence map from current materials. Do not carry over architecture assumptions, tensor dimensions, hyperparameters, or conclusions from earlier projects.
3. Determine which domain reference, if any, is relevant. Load only that reference when it materially helps.
4. Keep facts from different papers/repositories separate. If asked to compare them, make an explicit side-by-side comparison and identify each fact's source.
5. If the paper and repository describe different variants, report the discrepancy rather than silently reconciling them.

## Start-up workflow

When beginning a new paper or repository:

1. Inventory available papers, source files, configs, README, environment clues, and entry points.
2. Summarize the research question, claimed contribution, method family, inputs, outputs, and evaluation setup from available evidence.
3. Identify training and inference entry points if code is available.
4. Draw a compact end-to-end flow containing only verified or clearly labeled components.
5. List uncertainties and continue with the best-supported next step. Ask at most one direct clarification question if missing information blocks progress.

If no source code is available, analyze the paper as a paper; do not pretend to have verified an implementation.

## Investigation workflow

Use only phases relevant to the question:

1. **Research question and contribution** — problem, motivation, claimed contribution.
2. **Architecture / algorithm** — components, responsibilities, inputs, outputs, flow.
3. **Source call path** — entry points, active configuration, calls, conditions, return values.
4. **Data-flow trace** — tensors or data structures, shapes, layouts, indexing, consumers.
5. **Operation mechanics** — exact equations, operators, sampling/indexing rules, shape changes.
6. **Training and inference** — objectives, assignment, losses, gradients, optimizer, decoding and post-processing as applicable.
7. **Experiments** — datasets, baselines, metrics, ablations, results, limitations.
8. **Task adaptation** — task mismatch, data distribution, reusable components, necessary changes, validation plan.

## Domain selection: load only when relevant

These are optional guides, not assumptions about the current model:

- `domains/object-detection.md`: only for detection, localization, or instance segmentation.
- `domains/llm-transformer.md`: only for language models or Transformer-based sequence modeling.
- `domains/diffusion-models.md`: only for diffusion/noise-based generation.
- `domains/retrieval-rag.md`: only for retrieval, embedding search, reranking, or retrieval-augmented generation.
- `domains/multimodal-learning.md`: only when the current paper or code actually involves multiple modalities, multimodal fusion, cross-modal interaction, or modality-specific learning.

If a method combines domains, consult multiple references only where the combination is evidenced. If no reference fits, use the general workflow and do not force a match.

General references:
- `references/source-reading.md`: source verification and call-path tracing.
- `references/tensor-tracing.md`: dimensions and concrete data operations.
- `references/training-inference.md`: training, inference, losses, selection, and post-processing.
- `references/paper-analysis.md`: paper reading and contribution analysis.
- `references/experiment-analysis.md`: experiments, metrics, ablations, and claims.
- `references/output-templates.md`: reusable answer layouts.

## Source verification contract

- Prefer checked-out source and active configuration for implementation facts; use the paper to explain stated intent.
- A class existing in a repository does not prove it is used by the active configuration.
- Verify config switches before explaining a branch as default behavior.
- Follow callers and consumers; do not stop at a function definition if asked about runtime behavior.
- If an operation is not found in one file, search the call path and related modules before concluding it is absent.
- Scope negative claims: “I did not find this in the inspected path/files,” not “the entire system never does this.”
- Do not combine different frameworks, forks, versions, paper variants, training code, and deployment code without marking the distinction.
- Comments and names are clues, not proof; inspect executable statements and call sites.
- If only a paper PDF is available, label implementation details as unverified.

## Data and tensor explanation contract

For every important tensor or data structure, explain as relevant:
- exact variable or field name;
- shape, layout, type, units, or schema;
- meaning of each dimension or field;
- where it is created;
- the exact operation that changes it;
- input and output before/after that operation;
- where it is consumed next.

Do not assume `C` means channels rather than classes; define symbols in context. Do not assume all models use tensors. When asked “how exactly?”, show the operation, index mapping, equation, or a small numerical example. Avoid vague phrases when mechanics can be traced.



## Architecture-to-Detail Traceability Contract

The overall architecture, source-code analysis, tensor explanations, and interactive webpage MUST form one traceable structure. Do not present an architecture diagram followed by disconnected module descriptions.

### 1. Stable module IDs
Assign stable IDs (M1, M2, M3, ...) to major modules. Use the same IDs in the architecture diagram, source mapping table, detailed explanations, JSON configuration, and webpage. Do not silently renumber modules when refining the analysis.

### 2. Architecture-to-source mapping
Before deep dives, provide or record a mapping table:

| Module ID | Architecture role | Source location | Inputs | Outputs | Next consumer | Evidence status |
|---|---|---|---|---|---|---|

Use actual file paths, class/function names, and source variable names when verified. If code is unavailable, label the source location as unavailable rather than inventing it.

### 3. Variable lineage
For every important variable, trace:
- where it is created;
- its actual shape/type/schema;
- each concrete operation that changes it;
- its output variable and resulting shape/type;
- the module/function that consumes it next.

Map conceptual names to actual source variables explicitly. Never silently substitute generic names for implementation identifiers.

### 4. Explain in architecture order
For each module:
1. Locate it in the whole architecture.
2. Give its source location and evidence status.
3. Explain inputs and their origin.
4. Explain operations in execution order.
5. Explain outputs and shape/type changes.
6. Identify the exact downstream consumer.
7. Explain training/loss/gradient behavior only when relevant and verified.
8. Return to the whole architecture and show which path has been explained.

### 5. Branches and convergence
Show separate branches separately. Explicitly identify where they split and converge, which variables flow along each edge, and whether the connection is data flow or training-only flow. Do not collapse materially different branches into a vague “feature” node.

### 6. Audit
Before finishing, check that every major architecture node has details, every detailed module maps back to a node, and every important edge/variable has a source or an explicit evidence status. If the mapping is incomplete, repair it before adding more isolated detail.

## Interactive Architecture Explorer Contract

For a new-paper learning workflow, create an interactive architecture webpage when local file creation is available and the user has supplied enough paper/source material to establish at least a preliminary architecture. Do not require the user to repeat this request. For focused follow-up questions, update the existing explorer only when it materially helps.

### Required deliverables

Create a paper-specific output folder, for example `artifacts/<paper-slug>/`, containing:

- `paper_network_explorer.html`: a standalone, locally openable interactive webpage.
- `paper_model_config.json`: the editable model/architecture configuration used by the webpage.
- Optionally, `architecture-evidence.md`: a compact evidence ledger linking major nodes and edges to paper sections or source locations.

Use the reusable template at `templates/paper_network_explorer.html` and the build helper `scripts/build_explorer.py`. Do not recreate the UI from scratch unless the template cannot meet a stated requirement.

### Webpage interaction requirements

The generated page must, where supported by the template:

- Show the whole model/algorithm as a directed graph with stable module IDs (M1, M2, ...).
- Let users click a module to see its purpose, exact source location, inputs, outputs, data types/shapes, computation steps, upstream/downstream modules, and verification status.
- Highlight adjacent upstream/downstream nodes and edges when a module is selected.
- Search modules, variables, and source identifiers.
- Distinguish ordinary data-flow edges from training/loss edges.
- Allow navigation from a module detail to its upstream/downstream modules.
- Import/export the JSON configuration for later edits and updates.
- Work as a local HTML file without a backend or external network dependency.

### Architecture and evidence rules

- Build nodes and edges from the current paper and repository only; never reuse EMOE, PP-DocLayoutV3, or another project's assumed architecture as facts for a new project.
- Preserve stable module IDs and source variable names across the diagram, detail panels, tables, and explanations.
- Label every module's evidence status, such as `source-verified`, `paper-described`, `inferred`, or `unverified`.
- Include exact repository-relative paths and class/function names when verified. Never invent source paths, tensor shapes, call relationships, or loss connections.
- When only the paper is available, still create a paper-level diagram if useful, but mark implementation locations and unverified shapes clearly as unavailable or unverified.
- Every edge must have a justified meaning. Label important edges with the variable/data being passed and its shape when known.
- Separate training-only flows (loss, matching, gradient/teacher paths) from inference/data flows where the graph supports it.
- If a module has multiple inputs or outputs, show each relevant variable as an input/output row; do not collapse materially different branches into a vague “features” label.
- If the graph is too large, create a high-level graph plus linked subgraphs or grouped modules. Do not omit important branches solely to make the diagram small.

### Build workflow

1. Inspect the actual paper, source files, configuration and runtime entry points.
2. Draft a module/edge inventory and map each node to source evidence.
3. Create `paper_model_config.json` following `references/model-config-schema.md`.
4. Choose clear, non-overlapping node coordinates and make the graph readable. Use the provided node types where appropriate: `input`, `feature`, `router`, `fusion`, `prediction`, and `loss`; other types may be used if needed.
5. Run `python scripts/build_explorer.py --config <config-path> --output <html-path>` from the Skill package or adapt the paths to the actual workspace.
6. Validate that the HTML builds, the JSON parses, all edge endpoints exist, module IDs are unique, and each major module has a status and data-flow explanation.
7. Open the resulting HTML in a browser when the environment allows; otherwise state that structural validation was performed but browser interaction was not visually tested.
8. Return links/paths to both files and explain how to open the HTML and update the JSON. Do not claim the diagram is fully source-verified if any nodes remain inferred or unverified.

### Progressive refinement

Create a useful first version after the initial architecture/source inventory, marking unknowns rather than waiting for every detail. As the user studies modules, update the same JSON and regenerate the HTML so that newly verified shapes, source locations, operations, and data-flow links appear in the same architecture. Do not silently renumber established modules; update the evidence status instead.

### Fallback

If file creation or Python execution is unavailable, provide the validated JSON configuration and explain how to use the included template/build helper. If no source code is available, do not invent code details; make the evidence level explicit.

## Training, inference, and evaluation contract

Keep distinct: forward computation; training-time target assignment/matching (if any); loss; backpropagation and optimizer update; inference decoding/ranking/thresholding/post-processing; offline evaluation.

Do not assume Hungarian matching, Top-K, NMS, attention, diffusion sampling, a particular loss, or any other named mechanism exists. Confirm it in the paper or active implementation.

For ranking/filtering, identify the ranked object, score, axis, threshold/count, index mapping, and whether the step itself deduplicates or merges.

## Experiment and task-adaptation contract

- Distinguish paper-reported numbers from local reproduction.
- State dataset split, metric, baseline, and conditions when available.
- Do not infer statistical significance or causality without evidence.
- For adaptation, define the target output; compare labels, data distribution, granularity, objectives, training, evaluation and post-processing as applicable.
- Separate **required changes**, **high-priority experiments**, **optional experiments**, and **not justified yet**.
- Recommend a minimal baseline and measurable validation plan before architectural rewrites.

## Response style

Start with a direct answer. Use compact diagrams, tables, equations, or examples when useful. For a new paper, start with the big picture; for a focused follow-up, answer the exact question first. Correct earlier assumptions openly when new evidence changes the interpretation.

## Done criteria

A focused explanation is complete when the user can tell what is claimed; where the operation occurs (if source exists); its inputs, computation, outputs, and next consumer; and what is verified, inferred, or still unknown.
