import requests

# Available columns:
# lcr
#             "LCR Sequence",
#             "LCR ID",
#             "Start of LCR",
#             "End of LCR",
#             "LCR length",
#             "Identification method",
#             "Number of annotations"
# annotation
#             "Annotation ID",
#             "Annotation",
#             "Category",
#             "Source ID",
#             "Gene Ontology",
#             "Start of annotation",
#             "End of annotation",
#             "Source database"
columns = ["Start of LCR",
           "End of LCR",
           "Start of annotation",
           "End of annotation",
           "LCR ID",
           'Annotation ID',
           'UniProtACC',
           'Annotation',
           'Category',
           'Source ID',
           "Gene Ontology",
           "Source database",
           'Organism',
           'Protein name',
           ]


def get_annotations_by_exact_lcr(begin, end, protein_id):
    data = {
        "result_data": "annotations",
        "columns": columns,

        "search_by_column": {
            "Start of LCR": [begin],
            "End of LCR": [end],
            "UniProtACC": [protein_id],
        },
    }
    result = requests.post("https://lcrannotdb.lcr-lab.org/api/lcrs/", json=data).text

    return result


def get_annotations_by_lcr_by_position(begin, end, protein_id):
    print(begin, end, protein_id)
    header = ""
    search_by_column = [
        {
            "End of LCR_contain": end,
            "Start of LCR_contain": begin,
            "UniProtACC": [protein_id],
        },
    ]
    result = []
    for search_query in search_by_column:
        data = {
            "result_data": "annotations",
            "columns": columns,
            "search_by_column": search_query

        }
        result2 = requests.post("https://lcrannotdb.lcr-lab.org/api/lcrs/", json=data).text
        for line in result2.split("\r\n"):
            header = ""
            if line:
                if "Start of LCR" not in line:
                    if line + "\r\n" not in result:
                        result.append(line + "\r\n")
                else:
                    header = line
    return header + "\r\n" + ''.join(result)


def get_annotations_by_lcr_sequence(sequence, protein_id):
    data = {
        "result_data": "annotations",
        "columns": columns,
        "search_by_column": {
            "LCR Sequence": [sequence],
            "UniProtACC": [protein_id],
        },
    }
    result = requests.post("https://lcrannotdb.lcr-lab.org/api/lcrs/", json=data).text
    return result


if __name__ == '__main__':
    begin = 262
    end = 294
    protein_id = "Q6GZX3"
    sequence = "PPPPPPKPTPPTPPTPPTPPTPPTPPTPPTPR"
    print(get_annotations_by_lcr_by_position(263, 268, "Q6GZX3"))
