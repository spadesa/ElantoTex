# ElantoTex

**ElantoTex** is a Python script for converting ELAN-style interlinear text into [expex](https://ctan.org/pkg/expex) LaTeX syntax.



## Usage Instructions

1. **Download** or clone the repository containing `ElantoTex.py`.
   
3. **Open a terminal** in the same directory as `ElantoTex.py`.
   
5. **Run**:
   `run ElantoTex.py <input_file>`

where:

1. `<input_file>` is required and must be the path to an **ELAN-exported text file in interlinear format**.
   
3. The script will:
* Replace all underscores (`_`) with periods (`.`) to avoid LaTeX errors.
* Remove extra blank lines after "`//`".
* Create an output file named `<input_file>_tex.txt`.

## Input File Requirements

1. Export from ELAN in interlinear text format.
2. Four lines per block, beginning with `tx@`, `wd@`, `ge@`, `tf@` for:

   `tx@` = text.</br>
   `wd@` = word.</br>
   `ge@` = gloss.</br>
   `tf@` = free translation.

4. `tx@` must be the **first** line, and `tf@` the **last** line of each block.
5. `Tabs` are not relevant (ignored by the script).

#### Example input:

   ```
   tx@ do da nganəngar be amolia ana va dərnge.
   wd@ do da ngan-əngar be a-moli =a a-n =a va dərng =e
   ge@ now, here PURP 1SG.NPST-say at ART-person =SG.CL:MASC 3SG.M-with =PAT 3SG.M.POSS old =SG.CL:FEM
   tf@ Now I'm going to tell about a man and his wife.
   ```

## Output

The script creates an output file named `<original_filename>_tex.txt`, containing your processed expex LaTeX markup. All underscores (`_`) are replaced with periods (`.`).

#### Example output:

```
\ex
\begingl
\gla do da nganəngar be amolia ana va dərnge.//
\glb do da ngan-əngar be a-moli =a a-n =a va dərng =e//
\glc now;here PURP 1SG.NPST-say at ART-person =SG.CL:MASC 3SG.M-with =PAT 3SG.M.POSS old =SG.CL:FEM//
\glft ` Now I'm going to tell about a man and his wife.'//
\endgl
\xe
```

Use pdflatex or your preferred LaTeX engine to compile a document containing this expex code.




