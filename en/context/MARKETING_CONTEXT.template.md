# Brand context record

The AI builds this record from the brand website, the current conversation, attachments and authorized sources. Keep one record per brand. Start with the identity, representative products, public terms and sources required for the current task, then fill gaps required by the selected method

## Version and identity

- Brand key, name and official website
- Revision, update time and last checked time
- Market, product ID and product version

## Shared data

| Data ID | Object and field | Text or numeric value | Product / Persona / market / period | Evidence state | Source and original excerpt | Retrieval time and validity | Confirmation record | Dependency IDs |
|---|---|---|---|---|---|---|---|---|

Objects include brand, product, offer, Persona, claim and proof, content asset, business rule, data source, consent rule and operating constraint. Evidence states are source_stated, brand_claim, user_confirmed, data_supported and hypothesis. Preserve each item's actual state. Store monetary values with numeric value, unit and currency

## Source index

For each source, save its ID, type, actual URL or file location, original excerpt, retrieval time, SHA-256 and scope. Preserve previous versions and identify both sources when they conflict

## SNS and YouTube source review

Discover candidate accounts from actual website links, footers, about pages and sameAs. Show the account URL, profile and a few post or video samples. Ask the user to confirm its relationship to the company, brand, founder or product and the permitted use before collecting relevant content. Reuse existing account confirmations

| Source ID | Platform and stable ID | Account URL | Relationship and permitted use | Discovery evidence | Account revision and original confirmation | Collection date, count and coverage | Content review confirmation |
|---|---|---|---|---|---|---|---|

Show extracted fields with original links and excerpts for a separate content review before writing them into the context. Preserve company identity, founder views, brand claims, customer statements and Persona hypotheses separately. Video titles and descriptions provide metadata_only coverage. Transcripts retain language, origin and timestamps

Machine snapshots include source_accounts, source_reviews and evidence.social. Follow social_evidence in the method contract for fields and the identity digest. Recheck dependent records when a source is withdrawn or changes. Preserve independently supported and separately user-confirmed facts, and retain the last successful collection when access fails

## Missing data

List the necessary missing fields, accessible sources and next actions for the selected Skill and stage. Reuse known data and resume the original task after collecting what is needed

## Separate task record

Task Context stores the task_id, original request, Skill and stage, scope, data references, pending decisions, used context IDs and digests, and output references and digests. Leave bulk orders and personal lists in their source systems

Record video evidence by the coverage actually obtained and its time range. Transcripts include language and origin; audiovisual analysis includes the reader, audio/visual modes and execution receipt. Accounts found through search retain the original discovery excerpt and enter pending source confirmation
