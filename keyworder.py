def keyworder(text):
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

    article = text.split(". ")
    appropriate_tags = []
    flag = 0

    for tag in tags:
        for keyword in tags[tag]:
            if keyword in text:
                appropriate_tags.append(tag)
                flag = 1
                for sentence in article:
                    if keyword in sentence:
                        print(sentence)

    # checking condition for string found or not
    if flag == 1:
        print("Appropriate tags: {}".format(str(appropriate_tags)))
    else:
        print("Didn't find any appropriate tags to assign")


art = "".lower()

keyworder(art)



