import sys
import os
import codecs

def transtotex(filename):

	"""
    Transfer Elan-like output (with tier markers tx@, wd@, ge@, tf@, etc.) to LaTeX (expex package) syntax,
    then write the results to 'output_file'.
	
	- export format in Elan: interlinear text, tf@ last position, including tier names, wrap block - each block) 

    - Underscores are replaced by periods (e.g., '_' -> '.'; error in latex if use '_').
    - Extra blank lines after "//" are removed.

	The output file is generated as <basename>_tex.txt

    """
	
    # Read lines, stripping the trailing newline
	
	with codecs.open(filename, 'r', encoding='utf-8') as f:
		oldlist = [line.rstrip('\n') for line in f]
		
	newlist = []

	for line in oldlist:
		line_stripped = line.strip('\r')

		if line_stripped.startswith("tx@"):
			replaced = line_stripped.replace("tx@", "\\ex\n\\begingl\n\\gla")
			newlist.append(replaced + "//")

		elif line_stripped.startswith("wd@"):
			replaced = line_stripped.replace("wd@", "\\glb")
			newlist.append(replaced + "//")

		elif line_stripped.startswith("ge@"):
			replaced = line_stripped.replace("ge@", "\\glc")
			newlist.append(replaced + "//")

		elif line_stripped.startswith("tf@"):
            # Replace "tf@   " with a line break and "\glft `"
			replaced = line_stripped.replace("tf@   ", "\n\\glft `")
			newlist.append(
				replaced + "'" + "//" + "\n" + "\\endgl\n\\xe\n\n"
            )

    # 1) Combine everything into one string
	final_text = "\n".join(newlist)

    # 2) Remove extra new lines after "//", turning "//\n\n" into "//\n"
	final_text = final_text.replace("//\n\n", "//\n")

    # 3) Replace all underscores with periods
	final_text = final_text.replace('_', '.')

    # Build the output filename: original base name + "_tex.txt"
	base, ext = os.path.splitext(filename)
	output_file = f"{base}_tex.txt"

    # Write the cleaned text to <base>_tex.txt
	with open(output_file, 'w', encoding='utf-8') as f:
		f.write(final_text)

	print(f"Created output file: {output_file}")


if __name__ == "__main__":
    # Usage: python yourscript.py <input_file>
    # The script will automatically create <base>_tex.txt as output.
	if len(sys.argv) < 2:
		print("Usage: python yourscript.py <input_file>")
		sys.exit(1)

	input_file = sys.argv[1]
	transtotex(input_file)
