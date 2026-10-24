\
# Domain Guide: Multimodal Learning

Use only when the current paper or implementation actually uses two or more modalities or cross-modal information.

## Identify the task and modalities
- Name the actual modalities and final prediction/task.
- Determine whether inputs are raw data, pretrained features, or embeddings.
- Verify data alignment, sequence lengths, padding/masks, feature dimensions, and missing-modality handling from the data pipeline.

## Trace each modality separately
For each modality, record input variable/schema, preprocessing, encoder, output variable/shape, and next consumer. Do not assume modalities share dimensions, time steps, or encoders.

## Analyze interaction and fusion
Use the actual implementation to determine whether it uses concatenation, addition, weighted fusion, cross-modal attention, gating, routing, mixture-of-experts, or another method. Record input/output shapes, projection and normalization steps, broadcast axes, and the exact operation.

## Analyze modality-specific experts and routing (if present)
Trace router input, score calculation, normalization, expert selection/weights, expert outputs, aggregation, and downstream consumers. Do not infer a router or expert structure from the paper title alone.

## Analyze losses and distillation (if present)
For every loss, record the prediction/feature it consumes, labels or teacher targets, formula, weight, call site, gradient path, and any detach/frozen parameters. Separate training-only branches from inference.

## Experiments
Inspect unimodal baselines, modality ablations, fusion ablations, routing/experts ablations, distillation ablations, robustness to missing/noisy modalities, and reported metrics only where available.

## Architecture webpage
When the interactive explorer is generated, represent modality-specific paths as distinct nodes or branches. Show where they split and converge, label cross-modal edges with actual variables, and mark source-unverified paths explicitly.
