# Audit Worksheet (test) — `results\agent_test_baseline_dense_b800\traces.json`

## t01 (`answerable=True`, `status=abstain`, `searches=4`)
- **Question:** Why is using the NIST AI RMF alone insufficient for effective AI risk management, and what challenge can smaller organizations face?
- **Expected Answer:** Organizations must establish accountability mechanisms, roles and responsibilities, culture, and incentive structures backed by senior-level commitment; using the AI RMF alone does not create these incentives or cultural changes, and small to medium-sized organizations may face different challenges than large ones depending on capabilities and resources.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 14, 'evidence': 'Organizations need to establish and maintain the appropriate accountability mechanisms, roles and responsibilities, culture, and incentive structures for risk management to be effective. Use of the AI RMF alone will not lead to these changes or provide the appropriate incentives. Effective risk management is realized through organizational commitment at senior levels and may require cultural change within an organization or industry. In addition, small to medium-sized organizations managing AI risks or implementing the AI RMF may face different challenges than large organizations, depending on their capabilities and resources.'}]
- **Agent Answer:** Không đủ bằng chứng để trả lời.
- **Citations:** []

## t02 (`answerable=True`, `status=answered`, `searches=1`)
- **Question:** Does the NIST AI RMF mandate a fixed template for AI RMF cross-sectoral profiles?
- **Expected Answer:** No. The NIST AI RMF does not prescribe profile templates, allowing for flexibility in implementation.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 39, 'evidence': 'This Framework does not prescribe profile templates, allowing for flexibility in implementation.'}]
- **Agent Answer:** No, the NIST AI RMF does not mandate a fixed template for AI RMF cross-sectoral profiles. The Framework explicitly does not prescribe profile templates, allowing for flexibility in implementation [B:nist-ai-100-1:p039:c01].
- **Citations:** ['B:nist-ai-100-1:p039:c01']
  - Cited `[B:nist-ai-100-1:p039:c01]` (p.39): AI RMF cross-sectoral profiles cover risks of models or applications that can be used across use cases or sectors. Cross-sectoral profiles can also cover how to govern, map, measure, and manage risks for activities or business processes common across sectors such as the use of large language models, cloud-based services or acquisition.

This Framework does not prescribe profile templates, allowing for flexibility in implementation.

## t03 (`answerable=True`, `status=abstain`, `searches=4`)
- **Question:** How do indirect prompt injection attacks differ from direct prompt injections in GAI systems, and what exploits have security researchers demonstrated?
- **Expected Answer:** Direct prompt injections input malicious prompts directly into a GAI system, whereas indirect prompt injection attacks remotely exploit LLM-integrated applications without a direct interface by injecting prompts into data likely to be retrieved; researchers have demonstrated exploiting vulnerabilities to steal proprietary data or run malicious code remotely.
- **Gold:** [{'source_id': 'nist-ai-600-1', 'page': 15, 'evidence': 'In direct prompt injections, attackers might craft malicious prompts and input them directly to a GAI system, with a variety of downstream negative consequences to interconnected systems. Indirect prompt injection attacks occur when adversaries remotely (i.e., without a direct interface) exploit LLM-integrated applications by injecting prompts into data likely to be retrieved. Security researchers have already demonstrated how indirect prompt injections can exploit vulnerabilities by stealing proprietary data or running malicious code remotely on a machine.'}]
- **Agent Answer:** Không đủ bằng chứng để trả lời.
- **Citations:** []

## t04 (`answerable=True`, `status=abstain`, `searches=4`)
- **Question:** Under MEASURE 2.6 in NIST AI 600-1, what must be demonstrated about safety before deploying an AI system, and what do safety metrics reflect?
- **Expected Answer:** The system must be demonstrated to be safe with residual negative risk not exceeding risk tolerance and able to fail safely (especially beyond its knowledge limits); safety metrics reflect system reliability and robustness, real-time monitoring, and response times for AI system failures.
- **Gold:** [{'source_id': 'nist-ai-600-1', 'page': 36, 'evidence': 'The AI system to be deployed is demonstrated to be safe, its residual negative risk does not exceed the risk tolerance, and it can fail safely, particularly if made to operate beyond its knowledge limits. Safety metrics reflect system reliability and robustness, real-time monitoring, and response times for AI system failures.'}]
- **Agent Answer:** Không đủ bằng chứng để trả lời.
- **Citations:** []

## t05 (`answerable=True`, `status=answered`, `searches=1`)
- **Question:** In the 2023 AI RMF Core Framework under the Map function, what must be understood and documented under MAP 1.1?
- **Expected Answer:** Intended purposes, potentially beneficial uses, context-specific laws, norms and expectations, and prospective deployment settings for the AI system must be understood and documented.
- **Gold:** [{'source_id': 'nist-ai-100-1', 'page': 31, 'evidence': 'MAP 1.1: Intended purposes, potentially beneficial uses, context-specific laws, norms and expectations, and prospective settings in which the AI system will be deployed are understood and documented.'}]
- **Agent Answer:** Under MAP 1.1 of the 2023 AI RMF Core Framework, the following must be understood and documented:

- Intended purposes,
- Potentially beneficial uses,
- Context-specific laws, norms, and expectations, and
- Prospective settings in which the AI system will be deployed [B:nist-ai-100-1:p031:c01].

Additionally, considerations under MAP 1.1 include the specific set or types of users along with their expectations; potential positive and negative impacts of system uses to individuals, communities, organizations, society, and the planet; assumptions and related limitations regarding AI system purposes, uses, and risks across the development or product AI lifecycle; and related TEVV (test, evaluation, verification, and validation) and system metrics [B:nist-ai-100-1:p031:c01].
- **Citations:** ['B:nist-ai-100-1:p031:c01']
  - Cited `[B:nist-ai-100-1:p031:c01]` (p.31): Table 2: Categories and subcategories for the MAP function.

MAP 1: Context is established and understood.

MAP 1.1: Intended purposes, potentially beneficial uses, context-specific laws, norms and expectations, and prospective settings in which the AI system will be deployed are understood and documented. Considerations include: the specific set or types of users along with their expectations; potential positive and negative impacts of system uses to individuals, communities, organizations, society, and the planet; assumptions and related limitations about AI system purposes, uses, and risks across the development or product AI lifecycle; and related TEVV and system metrics.

## t06 (`answerable=True`, `status=abstain`, `searches=4`)
- **Question:** In the Generative AI Profile under the Manage function, what types of controls does MG-3.1-001 mention for applying organizational risk tolerances to third-party GAI resources?
- **Expected Answer:** Controls include acquisition and procurement processes, assessing personnel credentials and qualifications, performing background checks, filtering GAI inputs and outputs, grounding, fine tuning, and retrieval-augmented generation.
- **Gold:** [{'source_id': 'nist-ai-600-1', 'page': 46, 'evidence': 'Apply organizational risk tolerances and controls (e.g., acquisition and procurement processes; assessing personnel credentials and qualifications, performing background checks; filtering GAI input and outputs, grounding, fine tuning, retrieval-augmented generation) to third-party GAI resources'}]
- **Agent Answer:** Không đủ bằng chứng để trả lời.
- **Citations:** []

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

