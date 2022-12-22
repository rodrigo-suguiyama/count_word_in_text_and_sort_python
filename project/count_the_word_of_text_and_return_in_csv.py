from csv import writer

sorted_dict = {}
with open("Lorem Ipsum.txt") as t:
    txt = t.read()
    txt_without_dot_comma = txt.replace(".", "").replace(",", " ")
    unique_words = set(txt_without_dot_comma.split())
    dict_list = {}
    for word in unique_words:
        dict_list[word] = txt.count(word)
        sorted_dict = sorted(dict_list.items(), key=lambda x: x[1], reverse=True)

with open("sorted_csv_file.csv", 'w') as csv_file:
    writer = writer(csv_file)
    writer.writerow(["name", "quantity"])
    for i in sorted_dict:
        writer.writerow(i)
