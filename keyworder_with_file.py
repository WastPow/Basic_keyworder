def keyworder(file):
    f = open(file, "r")
    tags = {
        "#kost": [
            "kost",
            "mat",
            "matvana",
            "läsk",
            "socker",
            "kalorier",
            "saft",
            "onyttig",
            "fett",
            "kolhydrater",
            "cola",
            "godis"
        ],
        "#barnfetma": [
            #insert keywords here...
        ],
        "#fetma": [
            #insert keywords here...
        ],
        #insert more tags here...
    }

    appropriate_tags = []
    flag = 0

    for line in f:
        for tag in tags:
            for keyword in tags[tag]:
                if keyword in line:
                    appropriate_tags.append(tag)
                    flag = 1
                    print(line)

    # checking condition for string found or not
    if flag == 1:
        print("Appropriate tags: {}".format(str(appropriate_tags)))
    else:
        print("Didn't find any appropriate tags to assign")

keyworder(#insert file name here)
