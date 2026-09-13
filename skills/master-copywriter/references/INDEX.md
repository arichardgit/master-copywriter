# Library Index

Fourteen sources. Every one is distilled in `references/books/` and every one has its full raw text in `references/source/` as structured JSON.

## Read all fourteen distillations, every time

Together they run about 35,000 words. That is the corpus, and reading it whole is what makes cross-referencing possible. A copywriter who has read only Halbert writes like Halbert; a copywriter who has read all fourteen can tell which of them the assignment actually calls for.

## Routing table

| Assignment | Read these distillations closest | Deep-read the raw JSON of |
|---|---|---|
| Headline | breakthrough-advertising, scientific-advertising, 21-bullet-secrets, take-their-money | breakthrough-advertising, 21-bullet-secrets |
| Lead / opening | great-leads, persuasion-hitman, adweek-copywriting-handbook | great-leads |
| Bullets, fascinations | 21-bullet-secrets, 7-figure-marketing-copy | 21-bullet-secrets |
| Long-form sales letter | ultimate-sales-letter, adweek-copywriting-handbook, 16-word-sales-letter, take-their-money | ultimate-sales-letter, adweek-copywriting-handbook |
| VSL script | 16-word-sales-letter, take-their-money, 7-figure-marketing-copy, dotcom-secrets | 16-word-sales-letter |
| Email, single | persuasion-hitman, dotcom-secrets | confessions-of-a-persuasion-hitman |
| Email sequence | dotcom-secrets, persuasion-hitman, 7-figure-marketing-copy | dotcom-secrets |
| Ad copy (Meta, YouTube, native) | take-their-money, great-leads, halbert-maximum-money | great-leads |
| Landing page | 7-figure-marketing-copy, adweek-copywriting-handbook, breakthrough-advertising | 7-figure-marketing-copy |
| Direct mail | halbert-maximum-money, ultimate-sales-letter, scientific-advertising | halbert-maximum-money |
| Offer construction, pricing | hormozi-ltv-cac, dotcom-secrets, ultimate-sales-letter | hormozi_ltv_cac_transcript |
| Upsells, downsells, funnel | dotcom-secrets, hormozi-ltv-cac, persuasion-hitman | dotcom-secrets |
| Webinar | dotcom-secrets, 7-figure-marketing-copy | dotcom-secrets |
| Guarantees, risk reversal | ultimate-sales-letter, take-their-money, adweek-copywriting-handbook | ultimate-sales-letter |
| Qualification, high-ticket, B2B | high-probability-selling, ultimate-sales-letter | high-probability-selling |
| Advertorial | halbert-maximum-money, breakthrough-advertising, great-leads | breakthrough-advertising |
| Critique or rewrite of existing copy | doctrine.md checklist, then whichever rows above match the asset | as needed |

## The fourteen

| File | Author | Its one job |
|---|---|---|
| `scientific-advertising.md` | Claude C. Hopkins | Specificity, testing, and the salesman test. The foundation everything else rests on. |
| `breakthrough-advertising.md` | Eugene Schwartz | Awareness, sophistication, mass desire, mechanism. What the headline is allowed to say. |
| `adweek-copywriting-handbook.md` | Joseph Sugarman | The slippery slide and the 31 psychological triggers. How to hold a reader. |
| `ultimate-sales-letter.md` | Dan Kennedy | The step-by-step letter system, headline formulas, guarantees, the P.S. |
| `great-leads.md` | Masterson & Forde | The six lead types matched to awareness. How to open. |
| `16-word-sales-letter.md` | Evaldo Albuquerque | One belief plus ten questions. The fastest way to outline a whole promo. |
| `21-bullet-secrets.md` | Clayton Makepeace | The bullet formula library and the headline-harvest method. |
| `halbert-maximum-money.md` | Gary Halbert | Voice. Sounding like a human being, and getting the message seen at all. |
| `take-their-money.md` | Kyle Milligan | Subtext: New, Easy, Safe, Big. The modern promo decoder. |
| `persuasion-hitman.md` | Ian Stanley | Email, story-selling, emotion, and average order value. |
| `7-figure-marketing-copy.md` | Sean Vosler | The framework encyclopedia and the Contrarian Copy Structure. |
| `dotcom-secrets.md` | Russell Brunson | Funnels, value ladders, email sequences, upsell and webinar scripts. |
| `high-probability-selling.md` | Werth & Ruben | Disqualification and honest takeaway. The antidote to hype. |
| `hormozi-ltv-cac.md` | Alex Hormozi | The economics that decide what the copy must do. |

## Raw source JSON

Each file in `references/source/` has a `title`, `author`, and a `parts` array (or `sections`/`front_matter` for the Halbert file); each part carries a `text` field with the full original prose. Read a raw file when you need the author's actual voice at length, a longer verbatim example than the distillation carries, or exhaustive coverage of a narrow technique.

Practical way to read one without flooding context:

```bash
python3 -c "
import json,sys
d=json.load(open('references/source/great-leads-michael-masterson.json'))
for p in d.get('parts',[]): print('###',p.get('label',''),p.get('title',''),'|',p.get('word_count'))
"
```

Then print only the parts you need by index.
