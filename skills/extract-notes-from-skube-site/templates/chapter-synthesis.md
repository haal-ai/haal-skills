# Chapter Synthesis Note

## Metadata
- **Input URL**: {{input_url}}
- **Chapter**: {{chapter_number}} - {{chapter_title}}
- **Run ID**: {{run_id}}
- **Agent**: {{agent_name}}
- **Created**: {{timestamp}}

---

## 1. Chapter Summary
{{chapter_summary}}

---

## 2. SKube-specific (What SKube adds/changes)
You MUST write clear statements starting with:
- "This is SKube-specific because ..."

### What it does
{{skube_specific_what_it_does}}

### Why it exists (value vs Quarkus)
{{skube_specific_why}}

---

## 3. SKube-specific synthesis (portable takeaways)
You MUST extract concise, reusable SKube-specific takeaways that can be aggregated across chapters.

You MUST format as a short list:
- **Takeaway**: <statement>

{{skube_takeaways}}

### SKube references
List references back to SKube docs.
- **SKube doc**: {{skube_ref_1}}
- **SKube doc**: {{skube_ref_2}}

---

## 4. Quarkus-baseline (What is standard Quarkus)
You MUST write clear statements starting with:
- "This is Quarkus-baseline (not SKube) because ..."

### What it does
{{quarkus_baseline_what_it_does}}

### Official Quarkus documentation
You MUST link official Quarkus documentation pages.
- **Quarkus doc**: {{quarkus_doc_1}}
- **Quarkus doc**: {{quarkus_doc_2}}

---

## 5. Practical Guidance (SKube vs Quarkus)
- **If you are using SKube**: {{practical_skube}}
- **If you are using plain Quarkus**: {{practical_quarkus}}

---

## 6. Open Questions / Uncertainty
{{open_questions}}
