# Audit Worksheet (dev) — `results\agent_dev_baseline_dense_b800\traces.json`

## q01 (`answerable=True`, `status=answered`, `searches=1`)
- **Question:** How does the NIST AI RMF define an AI system?
- **Expected Answer:** An engineered or machine-based system that can, for a given set of objectives, generate outputs such as predictions, recommendations, or decisions influencing real or virtual environments, operating with varying levels of autonomy.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 6, 'evidence': 'The AI RMF refers to an AI system as an engineered or machine-based system that can, for a given set of objectives, generate outputs such as predictions, recommendations, or decisions influencing real or virtual environments. AI systems are designed to operate with varying levels of autonomy'}]
- **Agent Answer:** According to the NIST AI RMF, an AI system is defined as "an engineered or machine-based system that can, for a given set of objectives, generate outputs such as predictions, recommendations, or decisions influencing real or virtual environments" [B:nist-ai-100-1:p006:c02]. The framework also notes that AI systems are designed to operate with varying levels of autonomy [B:nist-ai-100-1:p006:c02].
- **Citations:** ['B:nist-ai-100-1:p006:c02']
  - Cited `[B:nist-ai-100-1:p006:c02]` (p.6): The AI RMF refers to an AI system as an engineered or machine-based system that can, for a given set of objectives, generate outputs such as predictions, recommendations, or decisions influencing real or virtual environments. AI systems are designed to operate with varying levels of autonomy (Adapted from: OECD Recommendation on AI:2019; ISO/IEC 22989:2022).

## q02 (`answerable=True`, `status=abstain`, `searches=4`)
- **Question:** When considering the negative impact of a potential event in the AI RMF, what two components determine risk?
- **Expected Answer:** Risk is a function of (1) the negative impact, or magnitude of harm, that would arise if the circumstance or event occurs, and (2) the likelihood of occurrence.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 9, 'evidence': 'When considering the negative impact of a potential event, risk is a function of 1) the negative impact, or magnitude of harm, that would arise if the circumstance or event occurs and 2) the likelihood of occurrence'}]
- **Agent Answer:** Không đủ bằng chứng để trả lời.
- **Citations:** []

## q03 (`answerable=True`, `status=abstain`, `searches=4`)
- **Question:** If an organization is unable to measure an AI risk accurately, does that indicate the AI system poses low or high risk?
- **Expected Answer:** No. The inability to appropriately measure AI risks does not imply that an AI system necessarily poses either a high or low risk.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 10, 'evidence': 'The inability to appropriately measure AI risks does not imply that an AI system necessarily poses either a high or low risk.'}]
- **Agent Answer:** Không đủ bằng chứng để trả lời.
- **Citations:** []

## q04 (`answerable=True`, `status=answered`, `searches=1`)
- **Question:** When challenges in specifying AI risk tolerances remain unresolved, can a risk management framework always be readily applied to mitigate negative AI risks?
- **Expected Answer:** No. While the AI RMF can prioritize risk, it does not prescribe risk tolerance, and where challenges for specifying AI risk tolerances remain unresolved, there may be contexts where a risk management framework is not yet readily applicable for mitigating negative AI risks.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 12, 'evidence': 'To the extent that challenges for specifying AI risk tolerances remain unresolved, there may be contexts where a risk management framework is not yet readily applicable for mitigating negative AI risks.'}]
- **Agent Answer:** No. When challenges in specifying AI risk tolerances remain unresolved, a risk management framework cannot always be readily applied; rather, there may be contexts where a risk management framework is not yet readily applicable for mitigating negative AI risks [B:nist-ai-100-1:p012:c02].
- **Citations:** ['B:nist-ai-100-1:p012:c02']
  - Cited `[B:nist-ai-100-1:p012:c02]` (p.12): Emerging knowledge and methods to better inform harm/cost-benefit tradeoffs will continue to be developed and debated by businesses, governments, academia, and civil society. To the extent that challenges for specifying AI risk tolerances remain unresolved, there may be contexts where a risk management framework is not yet readily applicable for mitigating negative AI risks.

## q05 (`answerable=True`, `status=abstain`, `searches=4`)
- **Question:** What are the seven characteristics of trustworthy AI systems listed by the NIST AI RMF, and how should they be balanced?
- **Expected Answer:** The seven characteristics are valid and reliable, safe, secure and resilient, accountable and transparent, explainable and interpretable, privacy-enhanced, and fair with harmful bias managed; creating trustworthy AI requires balancing each based on the AI system's context of use.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 17, 'evidence': 'Characteristics of trustworthy AI systems include: valid and reliable, safe, secure and resilient, accountable and transparent, explainable and interpretable, privacy-enhanced, and fair with harmful bias managed. Creating trustworthy AI requires balancing each of these characteristics based on the AI system’s context of use.'}]
- **Agent Answer:** Không đủ bằng chứng để trả lời.
- **Citations:** []

## q06 (`answerable=True`, `status=answered`, `searches=1`)
- **Question:** What is the goal of AI robustness under unanticipated conditions, and how must a system perform if operating in an unexpected setting?
- **Expected Answer:** Robustness aims for appropriate system functionality across a broad set of conditions including unanticipated uses; it requires performing as expected and minimizing potential harms to people if operating in an unexpected setting.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 19, 'evidence': 'Robustness is a goal for appropriate system functionality in a broad set of conditions and circumstances, including uses of AI systems not initially anticipated. Robustness requires not only that the system perform exactly as it does under expected uses, but also that it should perform in ways that minimize potential harms to people if it is operating in an unexpected setting.'}]
- **Agent Answer:** Under unanticipated conditions, the goal of robustness is to ensure appropriate system functionality across a broad set of conditions and circumstances, including uses of AI systems that were not initially anticipated [B:nist-ai-100-1:p019:c02]. If operating in an unexpected setting, a system must perform in ways that minimize potential harms to people [B:nist-ai-100-1:p019:c02].
- **Citations:** ['B:nist-ai-100-1:p019:c02']
  - Cited `[B:nist-ai-100-1:p019:c02]` (p.19): Robustness or generalizability is defined as the “ability of a system to maintain its level of performance under a variety of circumstances” (Source: ISO/IEC TS 5723:2022). Robustness is a goal for appropriate system functionality in a broad set of conditions and circumstances, including uses of AI systems not initially anticipated. Robustness requires not only that the system perform exactly as it does under expected uses, but also that it should perform in ways that minimize potential harms to people if it is operating in an unexpected setting.

## q07 (`answerable=True`, `status=abstain`, `searches=4`)
- **Question:** Does making an AI system transparent guarantee that it is accurate, secure, privacy-enhanced, or fair?
- **Expected Answer:** No. A transparent system is not necessarily an accurate, privacy-enhanced, secure, or fair system, though it is difficult to determine whether an opaque system possesses those characteristics.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 21, 'evidence': 'A transparent system is not necessarily an accurate, privacy-enhanced, secure, or fair system. However, it is difficult to determine whether an opaque system possesses such characteristics, and to do so over time as complex systems evolve.'}]
- **Agent Answer:** Không đủ bằng chứng để trả lời.
- **Citations:** []

## q08 (`answerable=True`, `status=answered`, `searches=1`)
- **Question:** What distinct questions do transparency, explainability, and interpretability answer about an AI system?
- **Expected Answer:** Transparency answers 'what happened' in the system, explainability answers 'how' a decision was made, and interpretability answers 'why' a decision was made along with its meaning or context to the user.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 22, 'evidence': 'Transparency can answer the question of “what happened” in the system. Explainability can answer the question of “how” a decision was made in the system. Interpretability can answer the question of “why” a decision was made by the system and its meaning or context to the user.'}]
- **Agent Answer:** According to the NIST AI RMF, transparency, explainability, and interpretability answer the following distinct questions about an AI system:

- **Transparency** can answer the question of “what happened” in the system [B:nist-ai-100-1:p022:c01].
- **Explainability** can answer the question of “how” a decision was made in the system [B:nist-ai-100-1:p022:c01].
- **Interpretability** can answer the question of “why” a decision was made by the system and its meaning or context to the user [B:nist-ai-100-1:p022:c01].
- **Citations:** ['B:nist-ai-100-1:p022:c01']
  - Cited `[B:nist-ai-100-1:p022:c01]` (p.22): Risks to interpretability often can be addressed by communicating a description of why an AI system made a particular prediction or recommendation. (See “Four Principles of Explainable Artificial Intelligence” and “Psychological Foundations of Explainability and Interpretability in Artificial Intelligence” found here.)

Transparency, explainability, and interpretability are distinct characteristics that support each other. Transparency can answer the question of “what happened” in the system. Explainability can answer the question of “how” a decision was made in the system. Interpretability can answer the question of “why” a decision was made by the system and its meaning or context to the user.

## q09 (`answerable=True`, `status=abstain`, `searches=4`)
- **Question:** What three major categories of AI bias does NIST identify, and do they require discriminatory intent or prejudice to occur?
- **Expected Answer:** Systemic, computational and statistical, and human-cognitive bias; each can occur even in the absence of prejudice, partiality, or discriminatory intent.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 23, 'evidence': 'NIST has identified three major categories of AI bias to be considered and managed: systemic, computational and statistical, and human-cognitive. Each of these can occur in the absence of prejudice, partiality, or discriminatory intent.'}]
- **Agent Answer:** Không đủ bằng chứng để trả lời.
- **Citations:** []

## q10 (`answerable=True`, `status=abstain`, `searches=4`)
- **Question:** Why can datasets used to train AI systems create risks that differ from traditional software?
- **Expected Answer:** Training data may not truthfully or appropriately represent the intended context, ground truth may not exist or be available, and datasets can become detached from their original context or become stale relative to deployment.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 43, 'evidence': 'The data used for building an AI system may not be a true or appropriate representation of the context or intended use of the AI system, and the ground truth may either not exist or not be available.'}]
- **Agent Answer:** Không đủ bằng chứng để trả lời.
- **Citations:** []

## q11 (`answerable=True`, `status=answered`, `searches=1`)
- **Question:** Under Human-AI interaction considerations in the AI RMF, do all AI systems require human oversight?
- **Expected Answer:** No. Human-AI configurations range from fully autonomous to fully manual; some AI systems may not require human oversight (such as models used to improve video compression), while other systems specifically require it.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 45, 'evidence': 'Some AI systems may not require human oversight, such as models used to improve video compression. Other systems may specifically require human oversight.'}]
- **Agent Answer:** No, under the Human-AI interaction considerations in the AI RMF, not all AI systems require human oversight [B:nist-ai-100-1:p045:c02]. The framework notes that human-AI configurations can span from fully autonomous to fully manual, and some AI systems may not require human oversight (such as models used to improve video compression), while other systems may specifically require human oversight [B:nist-ai-100-1:p045:c02].
- **Citations:** ['B:nist-ai-100-1:p045:c02']
  - Cited `[B:nist-ai-100-1:p045:c02]` (p.45): Issues that merit further consideration and research include:

1. Human roles and responsibilities in decision making and overseeing AI systems need to be clearly defined and differentiated. Human-AI configurations can span from fully autonomous to fully manual. AI systems can autonomously make decisions, defer decision making to a human expert, or be used by a human decision maker as an additional opinion. Some AI systems may not require human oversight, such as models used to improve video compression. Other systems may specifically require human oversight.

## q12 (`answerable=True`, `status=abstain`, `searches=4`)
- **Question:** In the 2023 AI RMF Core Framework under the Measure function, what does MEASURE 1.1 require for AI risks or trustworthiness characteristics that will not or cannot be measured?
- **Expected Answer:** Measurement starts with the most significant AI risks identified during MAP, and any risks or trustworthiness characteristics that will not or cannot be measured must be properly documented.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 34, 'evidence': 'MEASURE 1.1: Approaches and metrics for measurement of AI risks enumerated during the MAP function are selected for implementation starting with the most significant AI risks. The risks or trustworthiness characteristics that will not – or cannot – be measured are properly documented.'}]
- **Agent Answer:** Không đủ bằng chứng để trả lời.
- **Citations:** []

## q13 (`answerable=True`, `status=abstain`, `searches=4`)
- **Question:** In the core AI RMF 1.0 framework (not the GAI profile) under the Manage function, what mechanisms must post-deployment AI system monitoring plans include under MANAGE 4.1?
- **Expected Answer:** Post-deployment monitoring plans must include mechanisms for capturing and evaluating input from users and other relevant AI actors, appeal and override, decommissioning, incident response, recovery, and change management.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 38, 'evidence': 'MANAGE 4.1: Post-deployment AI system monitoring plans are implemented, including mechanisms for capturing and evaluating input from users and other relevant AI actors, appeal and override, decommissioning, incident response, recovery, and change management.'}]
- **Agent Answer:** Không đủ bằng chứng để trả lời.
- **Citations:** []

## q14 (`answerable=True`, `status=answered`, `searches=1`)
- **Question:** Why are confabulations a natural byproduct of how generative AI models are designed?
- **Expected Answer:** Generative models generate outputs approximating the statistical distribution of their training data (for instance, LLMs predicting the next token or word), which can yield both accurate outputs and factually inaccurate or inconsistent ones.
- **Gold:** [{'source_id': 'nist-ai-600-1', 'page': 10, 'evidence': 'Confabulations are a natural result of the way generative models are designed: they generate outputs that approximate the statistical distribution of their training data; for example, LLMs predict the next token or word in a sentence or phrase.'}]
- **Agent Answer:** Confabulations are a natural byproduct of how generative AI models are designed because they generate outputs that approximate the statistical distribution of their training data (for instance, large language models predict the next token or word in a sentence or phrase) [B:nist-ai-600-1:p010:c02]. Although this statistical prediction can yield factually accurate and consistent outputs, it can also generate outputs that are factually inaccurate or internally inconsistent [B:nist-ai-600-1:p010:c02].
- **Citations:** ['B:nist-ai-600-1:p010:c02']
  - Cited `[B:nist-ai-600-1:p010:c02]` (p.10): Confabulations can occur across GAI outputs and contexts.9,10 Confabulations are a natural result of the way generative models are designed: they generate outputs that approximate the statistical distribution of their training data; for example, LLMs predict the next token or word in a sentence or phrase. While such statistical prediction can produce factually accurate and consistent outputs, it can also produce outputs that are factually inaccurate or internally inconsistent. This dynamic is particularly relevant when it comes to open-ended prompts for long-form responses and in domains which require highly contextual and/or domain expertise.

## q15 (`answerable=True`, `status=abstain`, `searches=4`)
- **Question:** Can model distillation or compression eliminate the environmental impacts of generative AI models?
- **Expected Answer:** No. Although creating smaller model versions via distillation or compression can reduce environmental impacts at inference time, training and tuning those models may still contribute to their environmental impacts, and there is no agreed-upon method to estimate environmental impacts from GAI.
- **Gold:** [{'source_id': 'nist-ai-600-1', 'page': 12, 'evidence': 'Methods for creating smaller versions of trained models, such as model distillation or compression, could reduce environmental impacts at inference time, but training and tuning such models may still contribute to their environmental impacts.'}]
- **Agent Answer:** Không đủ bằng chứng để trả lời.
- **Citations:** []

## q16 (`answerable=True`, `status=abstain`, `searches=4`)
- **Question:** What triggers 'model collapse' when training generative AI models on synthetic data?
- **Expected Answer:** Model collapse occurs when model training over-relies on synthetic data, causing data points to disappear from the new model's output distribution, threatening robustness and amplifying homogenization.
- **Gold:** [{'source_id': 'nist-ai-600-1', 'page': 13, 'evidence': 'Model collapse can occur when model training over-relies on synthetic data, resulting in data points disappearing from the distribution of the new model’s outputs.'}]
- **Agent Answer:** Không đủ bằng chứng để trả lời.
- **Citations:** []

## q17 (`answerable=True`, `status=abstain`, `searches=4`)
- **Question:** In the Generative AI Profile under the Govern function, what balance must transparency policies under GV-1.2-001 achieve regarding training data origin?
- **Expected Answer:** Transparency policies and processes should document the origin and history of training data and generated data for GAI applications to advance digital content transparency, while balancing the proprietary nature of training approaches.
- **Gold:** [{'source_id': 'nist-ai-600-1', 'page': 18, 'evidence': 'Establish transparency policies and processes for documenting the origin and history of training data and generated data for GAI applications to advance digital content transparency, while balancing the proprietary nature of training approaches.'}]
- **Agent Answer:** Không đủ bằng chứng để trả lời.
- **Citations:** []

## u_dev_01 (`answerable=False`, `status=abstain`, `searches=4`)
- **Question:** Under the NIST AI RMF 1.0 or Generative AI Profile, what exact maximum administrative fine or percentage of global annual turnover is specified as a statutory penalty for non-compliance?
- **Absence Reason:** Checked all 48 physical pages of NIST.AI.100-1.pdf and 64 physical pages of NIST.AI.600-1.pdf: terms 'administrative fine', 'global turnover', 'statutory penalty', 'penalty', 'fines', 'non-compliance', and 'percentage' occur 0 times. NIST AI RMF is voluntary and defines no monetary fines.
- **Agent Answer:** Không đủ bằng chứng để trả lời.
- **Citations:** []

## u_dev_02 (`answerable=False`, `status=abstain`, `searches=4`)
- **Question:** What minimum benchmark accuracy percentage (such as an MMLU or SWE-bench score) does NIST AI 100-1 or NIST AI 600-1 mandate before deploying a generative AI model in production?
- **Absence Reason:** Checked all physical pages of both PDFs: 'mmlu', 'swe-bench', and 'percentage' occur 0 times; all 14 mentions of 'benchmark' discuss qualitative benchmark selection, label errors, or bias evaluation (e.g., MS-2.3-001, MS-2.11-001) without any numeric accuracy cutoff.
- **Agent Answer:** Không đủ bằng chứng để trả lời.
- **Citations:** []

