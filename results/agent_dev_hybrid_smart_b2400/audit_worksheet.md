# Audit Worksheet (dev) — `results\agent_dev_hybrid_smart_b2400\traces.json`

## q01 (`answerable=True`, `status=answered`, `searches=2`)
- **Question:** How does the NIST AI RMF define an AI system?
- **Expected Answer:** An engineered or machine-based system that can, for a given set of objectives, generate outputs such as predictions, recommendations, or decisions influencing real or virtual environments, operating with varying levels of autonomy.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 6, 'evidence': 'The AI RMF refers to an AI system as an engineered or machine-based system that can, for a given set of objectives, generate outputs such as predictions, recommendations, or decisions influencing real or virtual environments. AI systems are designed to operate with varying levels of autonomy'}]
- **Agent Answer:** The NIST AI RMF defines an AI system as "an engineered or machine-based system that can, for a given set of objectives, generate outputs such as predictions, recommendations, or decisions influencing real or virtual environments" [B:nist-ai-100-1:p006:c02]. It also notes that AI systems are designed to operate with varying levels of autonomy [B:nist-ai-100-1:p006:c02].
- **Citations:** ['B:nist-ai-100-1:p006:c02']
  - Cited `[B:nist-ai-100-1:p006:c02]` (p.6): The AI RMF refers to an AI system as an engineered or machine-based system that can, for a given set of objectives, generate outputs such as predictions, recommendations, or decisions influencing real or virtual environments. AI systems are designed to operate with varying levels of autonomy (Adapted from: OECD Recommendation on AI:2019; ISO/IEC 22989:2022).

## q02 (`answerable=True`, `status=answered`, `searches=1`)
- **Question:** When considering the negative impact of a potential event in the AI RMF, what two components determine risk?
- **Expected Answer:** Risk is a function of (1) the negative impact, or magnitude of harm, that would arise if the circumstance or event occurs, and (2) the likelihood of occurrence.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 9, 'evidence': 'When considering the negative impact of a potential event, risk is a function of 1) the negative impact, or magnitude of harm, that would arise if the circumstance or event occurs and 2) the likelihood of occurrence'}]
- **Agent Answer:** When considering the negative impact of a potential event in the AI RMF, risk is determined as a function of two components:

1. The negative impact, or magnitude of harm, that would arise if the circumstance or event occurs [B:nist-ai-100-1:p009:c02].
2. The likelihood of occurrence [B:nist-ai-100-1:p009:c02].
- **Citations:** ['B:nist-ai-100-1:p009:c02']
  - Cited `[B:nist-ai-100-1:p009:c02]` (p.9): 1.1 Understanding and Addressing Risks, Impacts, and Harms

In the context of the AI RMF, risk refers to the composite measure of an event’s probability of occurring and the magnitude or degree of the consequences of the corresponding event. The impacts, or consequences, of AI systems can be positive, negative, or both and can result in opportunities or threats (Adapted from: ISO 31000:2018). When considering the negative impact of a potential event, risk is a function of 1) the negative impact, or magnitude of harm, that would arise if the circumstance or event occurs and 2) the likelihood of occurrence (Adapted from: OMB Circular A-130:2016). Negative impact or harm can be experienced by individuals, groups, communities, organizations, society, the environment, and the planet.

## q03 (`answerable=True`, `status=answered`, `searches=1`)
- **Question:** If an organization is unable to measure an AI risk accurately, does that indicate the AI system poses low or high risk?
- **Expected Answer:** No. The inability to appropriately measure AI risks does not imply that an AI system necessarily poses either a high or low risk.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 10, 'evidence': 'The inability to appropriately measure AI risks does not imply that an AI system necessarily poses either a high or low risk.'}]
- **Agent Answer:** If an organization is unable to appropriately measure AI risks, it does not imply that the AI system necessarily poses either a high or low risk [B:nist-ai-100-1:p010:c01].
- **Citations:** ['B:nist-ai-100-1:p010:c01']
  - Cited `[B:nist-ai-100-1:p010:c01]` (p.10): Fig. 1. Examples of potential harms related to AI systems. Trustworthy AI systems and their responsible use can mitigate negative risks and contribute to benefits for people, organizations, and ecosystems.

1.2 Challenges for AI Risk Management

Several challenges are described below. They should be taken into account when managing risks in pursuit of AI trustworthiness.

1.2.1 Risk Measurement

AI risks or failures that are not well-defined or adequately understood are difficult to measure quantitatively or qualitatively. The inability to appropriately measure AI risks does not imply that an AI system necessarily poses either a high or low risk. Some risk measurement challenges include:

## q04 (`answerable=True`, `status=answered`, `searches=1`)
- **Question:** When challenges in specifying AI risk tolerances remain unresolved, can a risk management framework always be readily applied to mitigate negative AI risks?
- **Expected Answer:** No. While the AI RMF can prioritize risk, it does not prescribe risk tolerance, and where challenges for specifying AI risk tolerances remain unresolved, there may be contexts where a risk management framework is not yet readily applicable for mitigating negative AI risks.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 12, 'evidence': 'To the extent that challenges for specifying AI risk tolerances remain unresolved, there may be contexts where a risk management framework is not yet readily applicable for mitigating negative AI risks.'}]
- **Agent Answer:** No. To the extent that challenges for specifying AI risk tolerances remain unresolved, there may be contexts where a risk management framework is not yet readily applicable for mitigating negative AI risks [B:nist-ai-100-1:p012:c02].
- **Citations:** ['B:nist-ai-100-1:p012:c02']
  - Cited `[B:nist-ai-100-1:p012:c02]` (p.12): Emerging knowledge and methods to better inform harm/cost-benefit tradeoffs will continue to be developed and debated by businesses, governments, academia, and civil society. To the extent that challenges for specifying AI risk tolerances remain unresolved, there may be contexts where a risk management framework is not yet readily applicable for mitigating negative AI risks.

## q05 (`answerable=True`, `status=answered`, `searches=4`)
- **Question:** What are the seven characteristics of trustworthy AI systems listed by the NIST AI RMF, and how should they be balanced?
- **Expected Answer:** The seven characteristics are valid and reliable, safe, secure and resilient, accountable and transparent, explainable and interpretable, privacy-enhanced, and fair with harmful bias managed; creating trustworthy AI requires balancing each based on the AI system's context of use.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 17, 'evidence': 'Characteristics of trustworthy AI systems include: valid and reliable, safe, secure and resilient, accountable and transparent, explainable and interpretable, privacy-enhanced, and fair with harmful bias managed. Creating trustworthy AI requires balancing each of these characteristics based on the AI system’s context of use.'}]
- **Agent Answer:** According to the NIST AI RMF, the seven characteristics of trustworthy AI systems are:
1. **Valid and reliable** [B:nist-ai-100-1:p017:c01]
2. **Safe** [B:nist-ai-100-1:p017:c01]
3. **Secure and resilient** [B:nist-ai-100-1:p017:c01]
4. **Accountable and transparent** [B:nist-ai-100-1:p017:c01]
5. **Explainable and interpretable** [B:nist-ai-100-1:p017:c01]
6. **Privacy-enhanced** [B:nist-ai-100-1:p017:c01]
7. **Fair with harmful bias managed** [B:nist-ai-100-1:p017:c01]

**How they should be balanced:**
- Balancing these characteristics must be based on the AI system's context of use [B:nist-ai-100-1:p017:c01].
- The characteristics influence one another, and extreme imbalances (such as highly secure but unfair systems, accurate but opaque and uninterpretable systems, or inaccurate but secure, privacy-enhanced, and transparent systems) are undesirable [B:nist-ai-100-1:p018:c04].
- A comprehensive approach to risk management requires balancing trade-offs among the characteristics [B:nist-ai-100-1:p018:c04].
- Decisions to commission or deploy an AI system should be grounded in a contextual assessment of trustworthiness characteristics alongside relative risks, impacts, costs, and benefits, and informed by a broad set of interested parties [B:nist-ai-100-1:p018:c04].
- **Citations:** ['B:nist-ai-100-1:p017:c01', 'B:nist-ai-100-1:p018:c04']
  - Cited `[B:nist-ai-100-1:p017:c01]` (p.17): 3. AI Risks and Trustworthiness

For AI systems to be trustworthy, they often need to be responsive to a multiplicity of criteria that are of value to interested parties. Approaches which enhance AI trustworthiness can reduce negative AI risks. This Framework articulates the following characteristics of trustworthy AI and offers guidance for addressing them. Characteristics of trustworthy AI systems include: valid and reliable, safe, secure and resilient, accountable and transparent, explainable and interpretable, privacy-enhanced, and fair with harmful bias managed. Creating trustworthy AI requires balancing each of these characteristics based on the AI system’s context of use. While all characteristics are socio-technical system attributes, accountability and transparency also relate to the processes and activities internal to an AI system and its external setting.
  - Cited `[B:nist-ai-100-1:p018:c04]` (p.18): Trustworthiness characteristics explained in this document influence each other. Highly secure but unfair systems, accurate but opaque and uninterpretable systems, and inaccurate but secure, privacy-enhanced, and transparent systems are all undesirable. A comprehensive approach to risk management calls for balancing tradeoffs among the trustworthiness characteristics. It is the joint responsibility of all AI actors to determine whether AI technology is an appropriate or necessary tool for a given context or purpose, and how to use it responsibly. The decision to commission or deploy an AI system should be based on a contextual assessment of trustworthiness characteristics and the relative risks, impacts, costs, and benefits, and informed by a broad set of interested parties.

## q06 (`answerable=True`, `status=answered`, `searches=1`)
- **Question:** What is the goal of AI robustness under unanticipated conditions, and how must a system perform if operating in an unexpected setting?
- **Expected Answer:** Robustness aims for appropriate system functionality across a broad set of conditions including unanticipated uses; it requires performing as expected and minimizing potential harms to people if operating in an unexpected setting.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 19, 'evidence': 'Robustness is a goal for appropriate system functionality in a broad set of conditions and circumstances, including uses of AI systems not initially anticipated. Robustness requires not only that the system perform exactly as it does under expected uses, but also that it should perform in ways that minimize potential harms to people if it is operating in an unexpected setting.'}]
- **Agent Answer:** Under unanticipated conditions, robustness is a goal for appropriate system functionality across a broad set of conditions and circumstances, including uses of AI systems that were not initially anticipated [B:nist-ai-100-1:p019:c02]. When operating in an unexpected setting, the system must perform not only as it does under expected uses, but also in ways that minimize potential harms to people [B:nist-ai-100-1:p019:c02].
- **Citations:** ['B:nist-ai-100-1:p019:c02']
  - Cited `[B:nist-ai-100-1:p019:c02]` (p.19): Robustness or generalizability is defined as the “ability of a system to maintain its level of performance under a variety of circumstances” (Source: ISO/IEC TS 5723:2022). Robustness is a goal for appropriate system functionality in a broad set of conditions and circumstances, including uses of AI systems not initially anticipated. Robustness requires not only that the system perform exactly as it does under expected uses, but also that it should perform in ways that minimize potential harms to people if it is operating in an unexpected setting.

## q07 (`answerable=True`, `status=answered`, `searches=1`)
- **Question:** Does making an AI system transparent guarantee that it is accurate, secure, privacy-enhanced, or fair?
- **Expected Answer:** No. A transparent system is not necessarily an accurate, privacy-enhanced, secure, or fair system, though it is difficult to determine whether an opaque system possesses those characteristics.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 21, 'evidence': 'A transparent system is not necessarily an accurate, privacy-enhanced, secure, or fair system. However, it is difficult to determine whether an opaque system possesses such characteristics, and to do so over time as complex systems evolve.'}]
- **Agent Answer:** No. According to the NIST AI RMF, a transparent AI system is not necessarily an accurate, privacy-enhanced, secure, or fair system [B:nist-ai-100-1:p021:c01]. However, it is difficult to determine whether an opaque system possesses such characteristics, particularly over time as complex systems evolve [B:nist-ai-100-1:p021:c01].
- **Citations:** ['B:nist-ai-100-1:p021:c01']
  - Cited `[B:nist-ai-100-1:p021:c01]` (p.21): ple, how a human operator or user is notified when a potential or actual adverse outcome caused by an AI system is detected. A transparent system is not necessarily an accurate, privacy-enhanced, secure, or fair system. However, it is difficult to determine whether an opaque system possesses such characteristics, and to do so over time as complex systems evolve.

## q08 (`answerable=True`, `status=answered`, `searches=1`)
- **Question:** What distinct questions do transparency, explainability, and interpretability answer about an AI system?
- **Expected Answer:** Transparency answers 'what happened' in the system, explainability answers 'how' a decision was made, and interpretability answers 'why' a decision was made along with its meaning or context to the user.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 22, 'evidence': 'Transparency can answer the question of “what happened” in the system. Explainability can answer the question of “how” a decision was made in the system. Interpretability can answer the question of “why” a decision was made by the system and its meaning or context to the user.'}]
- **Agent Answer:** According to the NIST AI RMF, transparency, explainability, and interpretability answer the following distinct questions about an AI system:

- **Transparency** can answer the question of "what happened" in the system [B:nist-ai-100-1:p022:c01].
- **Explainability** can answer the question of "how" a decision was made in the system [B:nist-ai-100-1:p022:c01].
- **Interpretability** can answer the question of "why" a decision was made by the system and its meaning or context to the user [B:nist-ai-100-1:p022:c01].
- **Citations:** ['B:nist-ai-100-1:p022:c01']
  - Cited `[B:nist-ai-100-1:p022:c01]` (p.22): Risks to interpretability often can be addressed by communicating a description of why an AI system made a particular prediction or recommendation. (See “Four Principles of Explainable Artificial Intelligence” and “Psychological Foundations of Explainability and Interpretability in Artificial Intelligence” found here.)

Transparency, explainability, and interpretability are distinct characteristics that support each other. Transparency can answer the question of “what happened” in the system. Explainability can answer the question of “how” a decision was made in the system. Interpretability can answer the question of “why” a decision was made by the system and its meaning or context to the user.

## q09 (`answerable=True`, `status=answered`, `searches=1`)
- **Question:** What three major categories of AI bias does NIST identify, and do they require discriminatory intent or prejudice to occur?
- **Expected Answer:** Systemic, computational and statistical, and human-cognitive bias; each can occur even in the absence of prejudice, partiality, or discriminatory intent.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 23, 'evidence': 'NIST has identified three major categories of AI bias to be considered and managed: systemic, computational and statistical, and human-cognitive. Each of these can occur in the absence of prejudice, partiality, or discriminatory intent.'}]
- **Agent Answer:** NIST identifies three major categories of AI bias to be considered and managed:
1. Systemic bias
2. Computational and statistical bias
3. Human-cognitive bias [B:nist-ai-100-1:p023:c01].

These biases do not require discriminatory intent or prejudice to occur. NIST states that each of these three categories of bias can occur in the absence of prejudice, partiality, or discriminatory intent [B:nist-ai-100-1:p023:c01].
- **Citations:** ['B:nist-ai-100-1:p023:c01']
  - Cited `[B:nist-ai-100-1:p023:c01]` (p.23): Bias is broader than demographic balance and data representativeness. NIST has identified three major categories of AI bias to be considered and managed: systemic, computational and statistical, and human-cognitive. Each of these can occur in the absence of prejudice, partiality, or discriminatory intent. Systemic bias can be present in AI datasets, the organizational norms, practices, and processes across the AI lifecycle, and the broader society that uses AI systems. Computational and statistical biases can be present in AI datasets and algorithmic processes, and often stem from systematic errors due to non-representative samples. Human-cognitive biases relate to how an individual or group perceives AI system information to make a decision or fill in missing information, or how humans think about purposes and functions of an AI system.

## q10 (`answerable=True`, `status=answered`, `searches=4`)
- **Question:** Why can datasets used to train AI systems create risks that differ from traditional software?
- **Expected Answer:** Training data may not truthfully or appropriately represent the intended context, ground truth may not exist or be available, and datasets can become detached from their original context or become stale relative to deployment.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 43, 'evidence': 'The data used for building an AI system may not be a true or appropriate representation of the context or intended use of the AI system, and the ground truth may either not exist or not be available.'}]
- **Agent Answer:** Datasets used to train AI systems can create risks that differ from traditional software because AI systems may be trained on data that can change over time, sometimes significantly and unexpectedly [B:nist-ai-100-1:p006:c03]. This can impact system functionality and trustworthiness in ways that are hard to understand [B:nist-ai-100-1:p006:c03].
- **Citations:** ['B:nist-ai-100-1:p006:c03']
  - Cited `[B:nist-ai-100-1:p006:c03]` (p.6): While there are myriad standards and best practices to help organizations mitigate the risks of traditional software or information-based systems, the risks posed by AI systems are in many ways unique (See Appendix B). AI systems, for example, may be trained on data that can change over time, sometimes significantly and unexpectedly, affecting system functionality and trustworthiness in ways that are hard to understand. AI systems and the contexts in which they are deployed are frequently complex, making it difficult to detect and respond to failures when they occur. AI systems are inherently socio-technical in nature, meaning they are influenced by societal dynamics and human behavior.

## q11 (`answerable=True`, `status=answered`, `searches=1`)
- **Question:** Under Human-AI interaction considerations in the AI RMF, do all AI systems require human oversight?
- **Expected Answer:** No. Human-AI configurations range from fully autonomous to fully manual; some AI systems may not require human oversight (such as models used to improve video compression), while other systems specifically require it.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 45, 'evidence': 'Some AI systems may not require human oversight, such as models used to improve video compression. Other systems may specifically require human oversight.'}]
- **Agent Answer:** No, under Human-AI interaction considerations in the AI RMF, not all AI systems require human oversight [B:nist-ai-100-1:p045:c02]. Human-AI configurations can range from fully autonomous to fully manual, and while some systems may specifically require human oversight, others may not require it (such as models used to improve video compression) [B:nist-ai-100-1:p045:c02].
- **Citations:** ['B:nist-ai-100-1:p045:c02']
  - Cited `[B:nist-ai-100-1:p045:c02]` (p.45): Issues that merit further consideration and research include:

1. Human roles and responsibilities in decision making and overseeing AI systems need to be clearly defined and differentiated. Human-AI configurations can span from fully autonomous to fully manual. AI systems can autonomously make decisions, defer decision making to a human expert, or be used by a human decision maker as an additional opinion. Some AI systems may not require human oversight, such as models used to improve video compression. Other systems may specifically require human oversight.

## q12 (`answerable=True`, `status=answered`, `searches=1`)
- **Question:** In the 2023 AI RMF Core Framework under the Measure function, what does MEASURE 1.1 require for AI risks or trustworthiness characteristics that will not or cannot be measured?
- **Expected Answer:** Measurement starts with the most significant AI risks identified during MAP, and any risks or trustworthiness characteristics that will not or cannot be measured must be properly documented.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 34, 'evidence': 'MEASURE 1.1: Approaches and metrics for measurement of AI risks enumerated during the MAP function are selected for implementation starting with the most significant AI risks. The risks or trustworthiness characteristics that will not – or cannot – be measured are properly documented.'}]
- **Agent Answer:** In the 2023 AI RMF Core Framework under the Measure function, MEASURE 1.1 requires that AI risks or trustworthiness characteristics that will not – or cannot – be measured are properly documented [B:nist-ai-100-1:p034:c01].
- **Citations:** ['B:nist-ai-100-1:p034:c01']
  - Cited `[B:nist-ai-100-1:p034:c01]` (p.34): Practices related to measuring AI risks are described in the NIST AI RMF Playbook. Table 3 lists the MEASURE function’s categories and subcategories.

Table 3: Categories and subcategories for the MEASURE function.

MEASURE 1: Appropriate methods and metrics are identified and applied.

MEASURE 1.1: Approaches and metrics for measurement of AI risks enumerated during the MAP function are selected for implementation starting with the most significant AI risks. The risks or trustworthiness characteristics that will not – or cannot – be measured are properly documented.

MEASURE 1.2: Appropriateness of AI metrics and effectiveness of existing controls are regularly assessed and updated, including reports of errors and potential impacts on affected communities.

## q13 (`answerable=True`, `status=answered`, `searches=1`)
- **Question:** In the core AI RMF 1.0 framework (not the GAI profile) under the Manage function, what mechanisms must post-deployment AI system monitoring plans include under MANAGE 4.1?
- **Expected Answer:** Post-deployment monitoring plans must include mechanisms for capturing and evaluating input from users and other relevant AI actors, appeal and override, decommissioning, incident response, recovery, and change management.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 38, 'evidence': 'MANAGE 4.1: Post-deployment AI system monitoring plans are implemented, including mechanisms for capturing and evaluating input from users and other relevant AI actors, appeal and override, decommissioning, incident response, recovery, and change management.'}]
- **Agent Answer:** Under MANAGE 4.1 of the core AI RMF 1.0 framework, post-deployment AI system monitoring plans must include mechanisms for:

- Capturing and evaluating input from users and other relevant AI actors [B:nist-ai-100-1:p038:c01]
- Appeal and override [B:nist-ai-100-1:p038:c01]
- Decommissioning [B:nist-ai-100-1:p038:c01]
- Incident response [B:nist-ai-100-1:p038:c01]
- Recovery [B:nist-ai-100-1:p038:c01]
- Change management [B:nist-ai-100-1:p038:c01]
- **Citations:** ['B:nist-ai-100-1:p038:c01']
  - Cited `[B:nist-ai-100-1:p038:c01]` (p.38): Table 4: Categories and subcategories for the MANAGE function. (Continued)

MANAGE 4: Risk treatments, including response and recovery, and communication plans for the identified and measured AI risks are documented and monitored regularly.

MANAGE 4.1: Post-deployment AI system monitoring plans are implemented, including mechanisms for capturing and evaluating input from users and other relevant AI actors, appeal and override, decommissioning, incident response, recovery, and change management.

MANAGE 4.2: Measurable activities for continual improvements are integrated into AI system updates and include regular engagement with interested parties, including relevant AI actors.

## q14 (`answerable=True`, `status=answered`, `searches=1`)
- **Question:** Why are confabulations a natural byproduct of how generative AI models are designed?
- **Expected Answer:** Generative models generate outputs approximating the statistical distribution of their training data (for instance, LLMs predicting the next token or word), which can yield both accurate outputs and factually inaccurate or inconsistent ones.
- **Gold:** [{'source_id': 'nist-ai-600-1', 'page': 10, 'evidence': 'Confabulations are a natural result of the way generative models are designed: they generate outputs that approximate the statistical distribution of their training data; for example, LLMs predict the next token or word in a sentence or phrase.'}]
- **Agent Answer:** Confabulations are a natural result of how generative AI models are designed because they generate outputs that approximate the statistical distribution of their training data (for instance, large language models predict the next token or word in a sentence or phrase) [B:nist-ai-600-1:p010:c02]. While this statistical prediction can yield factually accurate and consistent outputs, it can also produce outputs that are factually inaccurate or internally inconsistent [B:nist-ai-600-1:p010:c02].
- **Citations:** ['B:nist-ai-600-1:p010:c02']
  - Cited `[B:nist-ai-600-1:p010:c02]` (p.10): Confabulations can occur across GAI outputs and contexts.9,10 Confabulations are a natural result of the way generative models are designed: they generate outputs that approximate the statistical distribution of their training data; for example, LLMs predict the next token or word in a sentence or phrase. While such statistical prediction can produce factually accurate and consistent outputs, it can also produce outputs that are factually inaccurate or internally inconsistent. This dynamic is particularly relevant when it comes to open-ended prompts for long-form responses and in domains which require highly contextual and/or domain expertise.

## q15 (`answerable=True`, `status=answered`, `searches=1`)
- **Question:** Can model distillation or compression eliminate the environmental impacts of generative AI models?
- **Expected Answer:** No. Although creating smaller model versions via distillation or compression can reduce environmental impacts at inference time, training and tuning those models may still contribute to their environmental impacts, and there is no agreed-upon method to estimate environmental impacts from GAI.
- **Gold:** [{'source_id': 'nist-ai-600-1', 'page': 12, 'evidence': 'Methods for creating smaller versions of trained models, such as model distillation or compression, could reduce environmental impacts at inference time, but training and tuning such models may still contribute to their environmental impacts.'}]
- **Agent Answer:** No, model distillation or compression cannot eliminate the environmental impacts of generative AI models. While methods for creating smaller versions of trained models, such as model distillation or compression, could reduce environmental impacts at inference time, training and tuning such models may still contribute to their environmental impacts [B:nist-ai-600-1:p012:c02].
- **Citations:** ['B:nist-ai-600-1:p012:c02']
  - Cited `[B:nist-ai-600-1:p012:c02]` (p.12): Current estimates suggest that training a single transformer LLM can emit as much carbon as 300 round-trip flights between San Francisco and New York. In a study comparing energy consumption and carbon emissions for LLM inference, generative tasks (e.g., text summarization) were found to be more energy- and carbon-intensive than discriminative or non-generative tasks (e.g., text classification).

Methods for creating smaller versions of trained models, such as model distillation or compression, could reduce environmental impacts at inference time, but training and tuning such models may still contribute to their environmental impacts. Currently there is no agreed upon method to estimate environmental impacts from GAI.

Trustworthy AI Characteristics: Accountable and Transparent, Safe

## q16 (`answerable=True`, `status=answered`, `searches=3`)
- **Question:** What triggers 'model collapse' when training generative AI models on synthetic data?
- **Expected Answer:** Model collapse occurs when model training over-relies on synthetic data, causing data points to disappear from the new model's output distribution, threatening robustness and amplifying homogenization.
- **Gold:** [{'source_id': 'nist-ai-600-1', 'page': 13, 'evidence': 'Model collapse can occur when model training over-relies on synthetic data, resulting in data points disappearing from the distribution of the new model’s outputs.'}]
- **Agent Answer:** According to NIST AI 600-1, "model collapse" can be triggered when:
- Model training over-relies on synthetic data, causing data points to disappear from the distribution of the new model's outputs [B:nist-ai-600-1:p013:c01].
- Overly homogenized content contributes to model collapse, which can also amplify any homogenization inherited from the model used to generate the synthetic training data [B:nist-ai-600-1:p013:c01].
- **Citations:** ['B:nist-ai-600-1:p013:c01']
  - Cited `[B:nist-ai-600-1:p013:c01]` (p.13): and reduced content diversity). Overly homogenized outputs can themselves be incorrect, or they may lead to unreliable decision-making or amplify harmful biases. These phenomena can flow from foundation models to downstream models and systems, with the foundation models acting as “bottlenecks,” or single points of failure.

Overly homogenized content can contribute to “model collapse.” Model collapse can occur when model training over-relies on synthetic data, resulting in data points disappearing from the distribution of the new model’s outputs. In addition to threatening the robustness of the model overall, model collapse could lead to homogenized outputs, including by amplifying any homogenization from the model used to generate the synthetic training data.

Trustworthy AI Characteristics: Fair with Harmful Bias Managed, Valid and Reliable

## q17 (`answerable=True`, `status=answered`, `searches=1`)
- **Question:** In the Generative AI Profile under the Govern function, what balance must transparency policies under GV-1.2-001 achieve regarding training data origin?
- **Expected Answer:** Transparency policies and processes should document the origin and history of training data and generated data for GAI applications to advance digital content transparency, while balancing the proprietary nature of training approaches.
- **Gold:** [{'source_id': 'nist-ai-600-1', 'page': 18, 'evidence': 'Establish transparency policies and processes for documenting the origin and history of training data and generated data for GAI applications to advance digital content transparency, while balancing the proprietary nature of training approaches.'}]
- **Agent Answer:** Under GV-1.2-001 of the Generative AI Profile, transparency policies and processes for documenting the origin and history of training data and generated data must advance digital content transparency while balancing the proprietary nature of training approaches [B:nist-ai-600-1:p018:c01].
- **Citations:** ['B:nist-ai-600-1:p018:c01']
  - Cited `[B:nist-ai-600-1:p018:c01]` (p.18): GOVERN 1.2: The characteristics of trustworthy AI are integrated into organizational policies, processes, procedures, and practices.

Action ID Suggested Action GAI Risks

GV-1.2-001

Establish transparency policies and processes for documenting the origin and history of training data and generated data for GAI applications to advance digital content transparency, while balancing the proprietary nature of training approaches.

Data Privacy; Information Integrity; Intellectual Property

GV-1.2-002

Establish policies to evaluate risk-relevant capabilities of GAI and robustness of safety measures, both prior to deployment and on an ongoing basis, through internal and external evaluations.

CBRN Information or Capabilities; Information Security

AI Actor Tasks: Governance and Oversight

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

