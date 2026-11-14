# Audit Worksheet (test) — `results\agent_test_hybrid_smart_b2400\traces.json`

## t01 (`answerable=True`, `status=answered`, `searches=4`)
- **Question:** Why is using the NIST AI RMF alone insufficient for effective AI risk management, and what challenge can smaller organizations face?
- **Expected Answer:** Organizations must establish accountability mechanisms, roles and responsibilities, culture, and incentive structures backed by senior-level commitment; using the AI RMF alone does not create these incentives or cultural changes, and small to medium-sized organizations may face different challenges than large ones depending on capabilities and resources.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 14, 'evidence': 'Organizations need to establish and maintain the appropriate accountability mechanisms, roles and responsibilities, culture, and incentive structures for risk management to be effective. Use of the AI RMF alone will not lead to these changes or provide the appropriate incentives. Effective risk management is realized through organizational commitment at senior levels and may require cultural change within an organization or industry. In addition, small to medium-sized organizations managing AI risks or implementing the AI RMF may face different challenges than large organizations, depending on their capabilities and resources.'}]
- **Agent Answer:** Using the NIST AI RMF alone is insufficient because it will not lead to the necessary accountability mechanisms, roles and responsibilities, culture, and incentive structures that organizations must establish and maintain for risk management to be effective, nor does it provide the appropriate incentives [B:nist-ai-100-1:p014:c01]. Effective risk management relies on senior-level organizational commitment and may require cultural change within an organization or industry [B:nist-ai-100-1:p014:c01]. 

Furthermore, small to medium-sized organizations managing AI risks or implementing the AI RMF may face different challenges compared to large organizations, depending on their capabilities and resources [B:nist-ai-100-1:p014:c01].
- **Citations:** ['B:nist-ai-100-1:p014:c01']
  - Cited `[B:nist-ai-100-1:p014:c01]` (p.14): Organizations need to establish and maintain the appropriate accountability mechanisms, roles and responsibilities, culture, and incentive structures for risk management to be effective. Use of the AI RMF alone will not lead to these changes or provide the appropriate incentives. Effective risk management is realized through organizational commitment at senior levels and may require cultural change within an organization or industry. In addition, small to medium-sized organizations managing AI risks or implementing the AI RMF may face different challenges than large organizations, depending on their capabilities and resources.

## t02 (`answerable=True`, `status=answered`, `searches=2`)
- **Question:** Does the NIST AI RMF mandate a fixed template for AI RMF cross-sectoral profiles?
- **Expected Answer:** No. The NIST AI RMF does not prescribe profile templates, allowing for flexibility in implementation.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 39, 'evidence': 'This Framework does not prescribe profile templates, allowing for flexibility in implementation.'}]
- **Agent Answer:** No. The NIST AI RMF explicitly does not mandate or prescribe profile templates, which allows for flexibility in implementation [B:nist-ai-100-1:p039:c01].
- **Citations:** ['B:nist-ai-100-1:p039:c01']
  - Cited `[B:nist-ai-100-1:p039:c01]` (p.39): AI RMF cross-sectoral profiles cover risks of models or applications that can be used across use cases or sectors. Cross-sectoral profiles can also cover how to govern, map, measure, and manage risks for activities or business processes common across sectors such as the use of large language models, cloud-based services or acquisition.

This Framework does not prescribe profile templates, allowing for flexibility in implementation.

## t03 (`answerable=True`, `status=answered`, `searches=1`)
- **Question:** How do indirect prompt injection attacks differ from direct prompt injections in GAI systems, and what exploits have security researchers demonstrated?
- **Expected Answer:** Direct prompt injections input malicious prompts directly into a GAI system, whereas indirect prompt injection attacks remotely exploit LLM-integrated applications without a direct interface by injecting prompts into data likely to be retrieved; researchers have demonstrated exploiting vulnerabilities to steal proprietary data or run malicious code remotely.
- **Gold:** [{'source_id': 'nist-ai-600-1', 'page': 15, 'evidence': 'In direct prompt injections, attackers might craft malicious prompts and input them directly to a GAI system, with a variety of downstream negative consequences to interconnected systems. Indirect prompt injection attacks occur when adversaries remotely (i.e., without a direct interface) exploit LLM-integrated applications by injecting prompts into data likely to be retrieved. Security researchers have already demonstrated how indirect prompt injections can exploit vulnerabilities by stealing proprietary data or running malicious code remotely on a machine.'}]
- **Agent Answer:** In generative AI (GAI) systems, prompt injection involves altering the input provided to the system so that it behaves in unintended ways [B:nist-ai-600-1:p015:c02]. Direct and indirect prompt injections differ in how the malicious input is delivered:

- **Direct prompt injections:** Attackers craft malicious prompts and input them directly into a GAI system, which can lead to a variety of downstream negative consequences for interconnected systems [B:nist-ai-600-1:p015:c02].
- **Indirect prompt injections:** Adversaries exploit LLM-integrated applications remotely without a direct interface by injecting prompts into data that is likely to be retrieved by the system [B:nist-ai-600-1:p015:c02].

**Demonstrated Exploits:**
Security researchers have demonstrated that indirect prompt injections can exploit vulnerabilities to:
1. Steal proprietary data [B:nist-ai-600-1:p015:c02].
2. Run malicious code remotely on a machine [B:nist-ai-600-1:p015:c02].
- **Citations:** ['B:nist-ai-600-1:p015:c02']
  - Cited `[B:nist-ai-600-1:p015:c02]` (p.15): For instance, prompt injection involves modifying what input is provided to a GAI system so that it behaves in unintended ways. In direct prompt injections, attackers might craft malicious prompts and input them directly to a GAI system, with a variety of downstream negative consequences to interconnected systems. Indirect prompt injection attacks occur when adversaries remotely (i.e., without a direct interface) exploit LLM-integrated applications by injecting prompts into data likely to be retrieved. Security researchers have already demonstrated how indirect prompt injections can exploit vulnerabilities by stealing proprietary data or running malicious code remotely on a machine. Merely querying a closed production model can elicit previously undisclosed information about that model.

## t04 (`answerable=True`, `status=answered`, `searches=1`)
- **Question:** Under MEASURE 2.6 in NIST AI 600-1, what must be demonstrated about safety before deploying an AI system, and what do safety metrics reflect?
- **Expected Answer:** The system must be demonstrated to be safe with residual negative risk not exceeding risk tolerance and able to fail safely (especially beyond its knowledge limits); safety metrics reflect system reliability and robustness, real-time monitoring, and response times for AI system failures.
- **Gold:** [{'source_id': 'nist-ai-600-1', 'page': 36, 'evidence': 'The AI system to be deployed is demonstrated to be safe, its residual negative risk does not exceed the risk tolerance, and it can fail safely, particularly if made to operate beyond its knowledge limits. Safety metrics reflect system reliability and robustness, real-time monitoring, and response times for AI system failures.'}]
- **Agent Answer:** Under MEASURE 2.6 in NIST AI 600-1, before an AI system is deployed, it must be demonstrated that [B:nist-ai-600-1:p036:c01]:
- The AI system is safe,
- Its residual negative risk does not exceed the risk tolerance, and
- It can fail safely, particularly if made to operate beyond its knowledge limits.

Additionally, safety metrics reflect system reliability and robustness, real-time monitoring, and response times for AI system failures [B:nist-ai-600-1:p036:c01].
- **Citations:** ['B:nist-ai-600-1:p036:c01']
  - Cited `[B:nist-ai-600-1:p036:c01]` (p.36): MEASURE 2.6: The AI system is evaluated regularly for safety risks – as identified in the MAP function. The AI system to be deployed is demonstrated to be safe, its residual negative risk does not exceed the risk tolerance, and it can fail safely, particularly if made to operate beyond its knowledge limits. Safety metrics reflect system reliability and robustness, real-time monitoring, and response times for AI system failures.

Action ID Suggested Action GAI Risks

MS-2.6-001

Assess adverse impacts, including health and wellbeing impacts for value chain or other AI Actors that are exposed to sexually explicit, offensive, or violent information during GAI training and maintenance.

Human-AI Configuration; Obscene, Degrading, and/or Abusive Content; Value Chain and Component Integration; Dangerous, Violent, or Hateful Content

## t05 (`answerable=True`, `status=answered`, `searches=1`)
- **Question:** In the 2023 AI RMF Core Framework under the Map function, what must be understood and documented under MAP 1.1?
- **Expected Answer:** Intended purposes, potentially beneficial uses, context-specific laws, norms and expectations, and prospective deployment settings for the AI system must be understood and documented.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 31, 'evidence': 'MAP 1.1: Intended purposes, potentially beneficial uses, context-specific laws, norms and expectations, and prospective settings in which the AI system will be deployed are understood and documented.'}]
- **Agent Answer:** Under MAP 1.1 of the 2023 AI RMF Core Framework, the following must be understood and documented:

- Intended purposes [B:nist-ai-100-1:p031:c01]
- Potentially beneficial uses [B:nist-ai-100-1:p031:c01]
- Context-specific laws, norms, and expectations [B:nist-ai-100-1:p031:c01]
- Prospective settings in which the AI system will be deployed [B:nist-ai-100-1:p031:c01]

Additionally, considerations under MAP 1.1 include:
- The specific set or types of users along with their expectations [B:nist-ai-100-1:p031:c01]
- Potential positive and negative impacts of system uses to individuals, communities, organizations, society, and the planet [B:nist-ai-100-1:p031:c01]
- Assumptions and related limitations about AI system purposes, uses, and risks across the development or product AI lifecycle [B:nist-ai-100-1:p031:c01]
- Related test, evaluation, verification, and validation (TEVV) and system metrics [B:nist-ai-100-1:p031:c01]
- **Citations:** ['B:nist-ai-100-1:p031:c01']
  - Cited `[B:nist-ai-100-1:p031:c01]` (p.31): Table 2: Categories and subcategories for the MAP function.

MAP 1: Context is established and understood.

MAP 1.1: Intended purposes, potentially beneficial uses, context-specific laws, norms and expectations, and prospective settings in which the AI system will be deployed are understood and documented. Considerations include: the specific set or types of users along with their expectations; potential positive and negative impacts of system uses to individuals, communities, organizations, society, and the planet; assumptions and related limitations about AI system purposes, uses, and risks across the development or product AI lifecycle; and related TEVV and system metrics.

## t06 (`answerable=True`, `status=answered`, `searches=1`)
- **Question:** In the Generative AI Profile under the Manage function, what types of controls does MG-3.1-001 mention for applying organizational risk tolerances to third-party GAI resources?
- **Expected Answer:** Controls include acquisition and procurement processes, assessing personnel credentials and qualifications, performing background checks, filtering GAI inputs and outputs, grounding, fine tuning, and retrieval-augmented generation.
- **Gold:** [{'source_id': 'nist-ai-600-1', 'page': 46, 'evidence': 'Apply organizational risk tolerances and controls (e.g., acquisition and procurement processes; assessing personnel credentials and qualifications, performing background checks; filtering GAI input and outputs, grounding, fine tuning, retrieval-augmented generation) to third-party GAI resources'}]
- **Agent Answer:** In the Generative AI Profile under the Manage function (MANAGE 3.1), action MG-3.1-001 mentions the following examples of controls for applying organizational risk tolerances to third-party GAI resources:

- Acquisition and procurement processes [B:nist-ai-600-1:p046:c02]
- Assessing personnel credentials and qualifications, and performing background checks [B:nist-ai-600-1:p046:c02]
- Filtering GAI input and outputs [B:nist-ai-600-1:p046:c02]
- Grounding [B:nist-ai-600-1:p046:c02]
- Fine tuning [B:nist-ai-600-1:p046:c02]
- Retrieval-augmented generation [B:nist-ai-600-1:p046:c02]

Additionally, MG-3.1-001 specifies applying organizational risk tolerances across the following areas [B:nist-ai-600-1:p046:c02]:
- The utilization of third-party datasets and other GAI resources [B:nist-ai-600-1:p046:c02]
- Fine-tuned third-party models [B:nist-ai-600-1:p046:c02]
- Existing third-party models adapted to a new domain [B:nist-ai-600-1:p046:c02]
- Reassessing risk measurements after fine-tuning third-party GAI models [B:nist-ai-600-1:p046:c02]
- **Citations:** ['B:nist-ai-600-1:p046:c02']
  - Cited `[B:nist-ai-600-1:p046:c02]` (p.46): MANAGE 3.1: AI risks and benefits from third-party resources are regularly monitored, and risk controls are applied and documented.

Action ID Suggested Action GAI Risks

MG-3.1-001

Apply organizational risk tolerances and controls (e.g., acquisition and procurement processes; assessing personnel credentials and qualifications, performing background checks; filtering GAI input and outputs, grounding, fine tuning, retrieval-augmented generation) to third-party GAI resources: Apply organizational risk tolerance to the utilization of third-party datasets and other GAI resources; Apply organizational risk tolerances to fine-tuned third-party models; Apply organizational risk tolerance to existing third-party models adapted to a new domain; Reassess risk measurements after fine-tuning third-party GAI models.

Value Chain and Component Integration; Intellectual Property

## u_test_01 (`answerable=False`, `status=abstain`, `searches=4`)
- **Question:** How does NIST AI 600-1 prescribe aligning its suggested actions with EU AI Act Article 5 prohibited AI practices and ISO/IEC 42001 certification audit requirements?
- **Absence Reason:** Checked all physical pages of both PDFs: 'eu ai act', 'article 5', '42001', 'prohibited ai', and 'certification audit' occur 0 times.
- **Agent Answer:** Không đủ bằng chứng để trả lời.
- **Citations:** []

## u_test_02 (`answerable=False`, `status=abstain`, `searches=4`)
- **Question:** What specific GPU cluster power cap (in megawatts or kilowatt-hours) or cooling water budget (in liters per token) is required by NIST AI 600-1 for foundation model training?
- **Absence Reason:** Checked all physical pages of both PDFs: 'gpu', 'megawatt', and 'kilowatt' occur 0 times; 'liter' only appears in 'literacy' (p.37) and 'Literature' (p.59), and 'watt' only in an excluded bibliography citation (p.60). While MS-2.12-003 suggests measuring energy/water consumption, no numeric caps are specified.
- **Agent Answer:** Không đủ bằng chứng để trả lời.
- **Citations:** []

