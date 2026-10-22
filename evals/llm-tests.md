# 领域测试：LLM / Transformer

**仅在当前仓库实际涉及 LLM 或 Transformer 序列建模时运行。**

## L1：输入到 logits
> 追踪文本从 tokenizer 输出到 embedding、模型层和 logits 的路径，给出当前实现的形状、变量名和源码位置。

预期：不猜 tokenizer、位置编码、层数或维度。

## L2：Attention 细节
> 仅根据当前源码解释 Q/K/V 的来源、投影、分头、mask、attention 计算与输出形状。若实现使用了不同变体，请按实际代码说明。

预期：不把所有 Attention 变体讲成完全相同的流程。

## L3：训练与生成
> 对比训练 forward 与实际生成循环，追踪 loss/标签和 token 选择、停止条件、缓存（若有）的路径。

预期：区分训练目标与推理解码，不默认模型使用某一种采样策略或 KV cache。

