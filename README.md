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

