import os

files_in_dir = []
episodes = []
subtitles = []
directory = "Placeholder"

while not os.path.isdir(directory) and not len(directory) == 0:
    directory = input("Paste your series directory (press enter for current directory):\n")

if len(directory) == 0:
    directory = "."


def find_ep_from_filename(filename):
    counter = 1

    while counter <= eps_count:

        if len(str(counter)) == 1:
            uppercase_search_for = f"E0{counter}"
            lowercase_search_for = f"e0{counter}"
        else:
            uppercase_search_for = f"E{counter}"
            lowercase_search_for = f"e{counter}"

        if lowercase_search_for in filename or uppercase_search_for in filename:
            return counter, filename

        counter += 1

    return -1, filename


for item in os.listdir(directory):
    if os.path.isfile(f"{directory}/{item}"):
        files_in_dir.append(item)


for file in files_in_dir:
    if file[-3:] == "mkv" or file[-3:] == "mp4":
        episodes.append(file)
    if file[-3:] == "srt":
        subtitles.append(file)

episodes_tuples = []
subtitles_tuples = []

eps_count = len(episodes)

for i in episodes:
    episodes_tuples.append(find_ep_from_filename(i))

for i in subtitles:
    subtitles_tuples.append((find_ep_from_filename(i)))

for ep in episodes_tuples:
    for sub in subtitles_tuples:
        if ep[0] == sub[0] and ep[0] > 0:
            os.rename(f"{directory}/{sub[1]}", f"{directory}/{ep[1][:-3]}srt")
            print(f"Renamed {sub[1]} to {ep[1][:-3]}srt")

