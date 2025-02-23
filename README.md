# .XCopmose file for TLA+

Bindings correspond to how operators are written in TLA+. For example:
| TLA+ Notation | Symbol |
|---------------|--------|
| `A`, `forall` | `∀`    |
| `=>`          | `⇒`    |
| `subseteq`    | `⊆`    |


> `\` is not included in compose sequence, but can be included by setting `ignore_backslash=False` in python script.

Based on translation table that I got from this repo:
https://github.com/tlaplus-community/tlauc/

To use it in vs code I had to run it with `GTK_IM_MODULE="xim"`, otherwise some symbols do not work. 

For vs code I am using Julia Mono font, it seems to render well all math.