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

## Missing data

List the necessary missing fields, accessible sources and next actions for the selected Skill and stage. Reuse known data and resume the original task after collecting what is needed

## Separate task record

Task Context stores the task_id, original request, Skill and stage, scope, data references, pending decisions, used context IDs and digests, and output references and digests. Leave bulk orders and personal lists in their source systems
