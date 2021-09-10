def import_gt(path):
    gt_lists = []

    with open(path, "r") as stream:
        for line in stream:
            cmty = line.split("\t")
            cmty[-1] = cmty[-1].replace("\n", "")
            gt_lists.append([int(id) for id in cmty])

    _gt_communites = gt_lists

    nodes = set([node for com in _gt_communites for node in com])

    x = 1

if __name__ == "__main__":
    path = "../storage_old/com-dblp.all.cmty.txt"
    import_gt(path)