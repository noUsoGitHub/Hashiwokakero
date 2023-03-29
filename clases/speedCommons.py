class pretty:
    def prettyMatrix(M):
        Splt= str(M).split("[")
        for ln in Splt:
            ln = ln.replace(",","\t")
            if ln !="":
                print("["+ln)
            