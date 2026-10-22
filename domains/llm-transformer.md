# 领域参考：LLM 与 Transformer

**仅在当前论文/源码确实涉及语言模型或 Transformer 序列建模时使用。** Transformer 并不意味着所有模型都有完全相同的模块和推理流程。

## 需要识别
- tokenizer / vocabulary 与输入 ID；
- embedding、位置/旋转位置信息（若有）；
- encoder-only、decoder-only、encoder-decoder 或其他结构；
- attention 变体、mask 规则、归一化与前馈层；
- 预训练目标、监督微调、偏好优化或其他训练阶段（以证据为准）；
- logits、采样/解码、停止条件和输出后处理；
- KV cache、并行策略或量化是否实际启用。

## 重点追踪
- token ID 如何变成嵌入；
- `[B,T,D]` 等维度在当前实现中的具体含义；
- attention 的 Q/K/V 来源、投影、分头、mask、权重与输出；
- logits 如何转换为 token 选择；
- 训练标签、loss mask 和 padding 如何处理；
- 训练 forward 与生成循环的区别；
- 论文训练方案是否与仓库代码一致。

不要默认所有模型都使用相同 tokenizer、位置编码、attention、训练阶段或解码策略。

