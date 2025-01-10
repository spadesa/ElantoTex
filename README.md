Below is a complete example README.md file in GitHub-flavored Markdown (GFM). You can copy and paste this directly into your repository as README.md.

markdown
复制代码
# ElantoTex

**ElantoTex** is a Python script for converting ELAN-style interlinear text into [expex](https://ctan.org/pkg/expex) LaTeX syntax.

---

## Usage Instructions

1. **Download** or clone the repository containing `ElantoTex.py`.
2. **Open a terminal** in the same directory as `ElantoTex.py`.
3. **Run**:
   ```bash
   python ElantoTex.py <input_file>
where:

<input_file> is required and must be the path to an ELAN-exported text file in interlinear format.
The script will automatically:

Replace all underscores (_) with periods (.) to avoid LaTeX errors.
Remove extra blank lines after "//".
Create an output file named <input_file>_tex.txt.
Input File Requirements
Export from ELAN in interlinear text format.
Four lines per block, beginning with tx@, wd@, ge@, tf@ for:
tx@ = text
wd@ = word
ge@ = gloss
tf@ = free translation
tx@ must be the first line, and tf@ the last line of each block.
Tabs are not relevant (ignored by the script).
Example input:

kotlin
复制代码
tx@ do da nganəngar be amolia ana va dərnge.
wd@ do da ngan-əngar be a-moli =a a-n =a va dərng =e
ge@ now, here PURP 1SG.NPST-say at ART-person =SG.CL:MASC 3SG.M-with =PAT 3SG.M.POSS old =SG.CL:FEM
tf@ Now I'm going to tell about a man and his wife.
Output
The script creates an output file named <original_filename>_tex.txt, containing your processed expex LaTeX markup. All underscores (_) are replaced with periods (.).

Example output:

tex
复制代码
\ex
\begingl
\gla do da nganəngar be amolia ana va dərnge.//
\glb do da ngan-əngar be a-moli =a a-n =a va dərng =e//
\glc now;here PURP 1SG.NPST-say at ART-person =SG.CL:MASC 3SG.M-with =PAT 3SG.M.POSS old =SG.CL:FEM//
\glft ` Now I'm going to tell about a man and his wife.'//
\endgl
\xe
Use pdflatex or your preferred LaTeX engine to compile a document containing this expex code.

复制代码










Usage Instructions

Download the repository containing ElantoTex.py

Run: run ElantoTex.py <input_file> 

<input_file>: required; the path to your Elan-like text file.



input file requirement:

output from Elan as interlinear text

format: 4 lines, begining with tx@, wd@, ge@, tf@ for text, word, gloss, free-translation.

tx@ has to be first, and tf@ has to be last line; tabs are not relevant.

e.g.

tx@   	do da nganəngar be amolia ana va dərnge.
wd@   	do       	da   	ngan-əngar   	be 	a-moli     	=a          	a-n        	=a   	va         	dərng 	=e
ge@   	now, here 	PURP 	1SG.NPST-say 	at 	ART-person 	=SG.CL:MASC 	3SG.M-with 	=PAT 	3SG.M.POSS 	old   	=SG.CL:FEM
tf@   	Now I'm going to tell about a man and his wife.


All underscores (_) will have been replaced by periods (.) because latex will give errors to "_".



Output: text_tex.txt, now containing your processed expex LaTeX output with the replacements and spacing changes applied.

e.g. 

\ex
\begingl
\gla   	do da nganəngar be amolia ana va dərnge.//
\glb   	 	do       	da   	ngan-əngar   	be 	a-moli     	=a          	a-n        	=a   	va         	dərng 	=e//
\glc   	 	now;here 	PURP 	1SG.NPST-say 	at 	ART-person 	=SG.CL:MASC 	3SG.M-with 	=PAT 	3SG.M.POSS 	old   	=SG.CL:FEM//
\glft `	Now I'm going to tell about a man and his wife.'//
\endgl
\xe

