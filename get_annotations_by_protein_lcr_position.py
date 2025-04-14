def get_annotations_by_lcr_by_position(begin, end, protein_id):
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





if __name__ == '__main__':
    begin = 262
    end = 294
    protein_id = "Q6GZX3"
    sequence = "PPPPPPKPTPPTPPTPPTPPTPPTPPTPPTPR"
    print(get_annotations_by_lcr_by_position(1, 2, protein_id))
    print(get_annotations_by_lcr_by_position(begin, end, protein_id))
    print("#1 ---s-l-----l-s")
    print(get_annotations_by_lcr_by_position(begin - 1, end + 1, protein_id))
    print("#2 ----l-s----l-s")
    print(get_annotations_by_lcr_by_position(begin + 1, end + 1, protein_id))
    print("#3 ---s-l----s-l-")
    print(get_annotations_by_lcr_by_position(begin - 1, end - 1, protein_id))
    print(#4  ----l-s---s-l-")
    print(get_annotations_by_lcr_by_position(begin + 1, end - 1, protein_id))
