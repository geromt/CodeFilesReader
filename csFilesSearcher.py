import json
import os
import pprint

main_path = "C:\\Users\\SPARTAN PC\\wkspaces\\PoseTrackerTest\\Assets"
extension = ".cs"


def find_files_with_extension(path, extension):
    files_found = {}
    files_list = []
    for f in os.listdir(path):
        abspath = os.path.join(path, f)
        if os.path.isdir(abspath):
            files_dict = find_files_with_extension(abspath, extension)
            if files_dict:
                if path in files_found:
                    files_found[path].append(files_dict)
                else:
                    files_found[path] = [files_dict]
        elif os.path.isfile(abspath):
            name, ext = os.path.splitext(f)
            if ext == extension:
                files_list.append(f)

    if files_list:
        if path in files_found:
            files_found[path].append(files_list)
        else:
            files_found[path] = files_list

    with open("filesTree.json", 'w') as f:
        f.write(json.dumps(files_found))

    return files_found


if __name__ == "__main__":
    pprint.pprint(find_files_with_extension(main_path, extension))
