---
name: paper-source-code-learning
description: >
  A general-purpose workflow for studying research papers and their code
  implementations across machine learning and software domains. Use when
  analyzing a paper, understanding a model or algorithm, tracing source code,
  explaining data flow and tensor shapes, comparing training and inference,
  examining experiments, or adapting a method to a new task.
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
- `domains/multimodal-learning.md`: use only when the current paper or code actually involves multiple modalities, multimodal fusion, cross-modal interaction, or modality-specific learning.

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

The overall architecture, source-code analysis, and tensor/data-flow explanation MUST form one traceable structure. Do not present the architecture first and then provide disconnected module details.

### 1. Assign stable module IDs

Before deep-diving into source code, create a verified overall architecture diagram. Assign stable IDs to every major module, such as M1, M2, M3, and M4.

Every module must show, when applicable:
- Module ID and responsibility.
- Actual source class/function.
- Input and output variables.
- Tensor shapes or data structures.
- Connections to upstream and downstream modules.

Use actual source variable names wherever possible. If conceptual names are needed, explicitly map them to source variables.

### 2. Build an architecture-to-source mapping table

Before explaining module internals, provide a mapping table:

| Module ID | Architecture role | Source location | Input variable/shape | Output variable/shape | Next module |
|---|---|---|---|---|---|

Every major architecture component must have a corresponding source location when code is available. If a location cannot be verified, mark it as unverified instead of inventing one.

### 3. Preserve variable identity across all explanations

Maintain a variable lineage table:

| Conceptual name | Actual source variable | Shape/type | Created by | Consumed by |
|---|---|---|---|---|

Do not silently replace source variable names with generic names such as h, z, or feature.

If a conceptual tensor corresponds to several intermediate source variables, show the complete transformation chain.

### 4. Explain modules in architecture order

For each module, use this structure:

**Module ID and name**

1. **Location in the overall architecture:** Identify the exact node and its upstream/downstream connections.
2. **Source location:** File path, class, and function.
3. **Input:** Actual variable names, shapes, and meanings.
4. **Computation:** The concrete operations in execution order.
5. **Output:** Actual variable names and resulting shapes.
6. **Data-flow connection:** Explain exactly which downstream module consumes each output.
7. **Training behavior:** Explain loss and gradient connections only when relevant.
8. **Architecture update:** Show a small subgraph highlighting this module and its connections.

Never explain an isolated operation without showing where its inputs originate and where its outputs go.

### 5. Trace branches and convergence explicitly

For branching architectures, show each path separately and identify where paths split or converge.

For example, if a model uses one path to calculate routing weights and another path to generate expert representations, show both paths and the exact operation that combines them.

Do not imply that two paths use the same features merely because they belong to the same conceptual module.

### 6. Align training losses with the architecture

For every loss term, identify:
- Which module outputs it consumes.
- Where the loss is calculated.
- Which branches receive gradients.
- Whether any tensor is detached or a parameter is frozen.
- How the loss contributes to the total objective.

Use a loss-to-module mapping table when multiple losses are present.

### 7. Reconcile the architecture with source evidence

After tracing the call path, update the architecture diagram to reflect the actual implementation.

If the paper diagram, initial conceptual diagram, and source implementation differ, explicitly distinguish them. Do not silently force source variables into an assumed architecture.

### 8. Perform a traceability audit before answering

Check that:
- Every major architecture node is explained.
- Every detailed module maps back to an architecture node.
- Every important variable has a traceable origin and downstream consumer.
- Every major connection is supported by source evidence or marked as an inference.
- The reader can locate any detail in the overall architecture without guessing.

If the architecture-to-detail mapping is incomplete, fix the mapping before adding more isolated details.

### 9. Teach from the whole to the part and back

First establish the whole architecture. Then explain one module at a time. After each module, return to the overall architecture and show what has now been understood.

The goal is not merely to explain individual operations, but to help the reader understand how those operations form the complete model.

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
