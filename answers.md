# CMPS 2200 Recitation 6
## Answers

**Name:**_Shayne Shelton_____


Place all written answers from `recitation-06.md` here for easier grading.

- **d.**

File           | Fixed-Length Coding | Huffman Coding | Huffman vs. Fixed-Length
----------------------------------------------------------------------
f1.txt          | 1340                  | 826             | 0.616
alice29.txt     | 1039367               | 676374          | 0.651
asyoulik.txt    | 876253                | 606448          | 0.692
grammar.lsp     | 78050                 | 56206           | 0.720
fields.c        | 26047                 | 17356           | 0.666

The Huffman Coding cost is consistantly less than the fixed-length coding cost. The Huffman cost are consistantly about 40% less that the fixed length costs.

- **e.**

If all of the characters had the same weight, we should expect the Huffman Coding cost to be about, if not exactly, the same as the fixed length coding. This should create a pretty balanced Huffman Tree with all characters having a code of about uniform length. While some cost may be saved, this may be negiligable with longer documents as the diffrence will not be that noticable. This understanding should be consistant accross all of th documents.
