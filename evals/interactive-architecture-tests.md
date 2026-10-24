\
# Interactive Architecture Explorer Tests

## W1: Generate the first graph
Prompt: “Start studying this paper. Build an interactive architecture webpage as part of the workflow.”
Expected:
- Generates `paper_model_config.json` and standalone HTML when file creation is available.
- Uses the current paper/repository only.
- Marks unverified nodes/shapes/source locations rather than inventing facts.

## W2: Trace a selected module
Prompt: “Click/inspect module M3 in the generated graph and explain its inputs, concrete operations, outputs, and downstream consumer.”
Expected:
- Module IDs match the graph and detail panel.
- Inputs/outputs retain real source variable names.
- The explanation points to source evidence where available.

## W3: Branching and convergence
Use a model with multiple input branches and a fusion point.
Expected:
- Each branch and its convergence are represented as separate nodes/edges.
- Training-only edges are distinguishable from inference/data edges when supported.

## W4: Update after deeper analysis
Prompt: “Update the existing explorer with the newly verified tensor shapes and source paths; preserve module IDs.”
Expected:
- Existing IDs are preserved.
- JSON and HTML are regenerated.
- Evidence status is updated without silently converting inference to verified fact.

## W5: Validation
Run:
`python scripts/build_explorer.py --config examples/model-config.example.json --output /tmp/paper-explorer-test.html`
Expected:
- The HTML file is created.
- JSON/edge validation passes.
- Manual browser testing is reported separately from structural validation.
