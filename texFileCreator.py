import json
import os.path

main_path = "C:\\Users\\SPARTAN PC\\wkspaces\\PoseTrackerTest\\Assets"
extension = ".cs"


def create_tex_file():
    with open("filesTree.json", "r") as json_file:
        files_data = json.loads(json_file.read())

    tex_text = []
    with open("portada.tex", "r") as portada_file:
        tex_text.append(portada_file.read())

    for data in files_data:
        tex_text.append("\\section{" + data["Name"] + "}")
        for file_name in data["Files"]:
            tex_text.append("\\subsection{" + file_name + "}")
            tex_text.append("\\begin{lstlisting}[language={[Sharp]C}]")
            abspath = os.path.join(data["DirPath"], file_name)
            with open(abspath, 'r') as f:
                tex_text.append(f.read())
            tex_text.append("\\end{lstlisting}")

    final_text = str.join("\n", tex_text)

    with open("main.tex", "w") as tex_file:
        tex_file.write(final_text)


if __name__ == "__main__":
    create_tex_file()
