


def getDegree_type(degree_type):
    try:
        # if "Associate Degree" in degree_type:
        #     degree_type = "Associate Degree"
        # elif "Bachelor" in degree_type:
        #     degree_type = "Bachelor"
        # elif "Master" in degree_type:
        #     degree_type = "Master"
        # elif "Doctor" in degree_type:
        #     degree_type = "Doctor"
        if "BSc" in degree_type:
            degree_type = 'Bsc'
        elif "MSc" in degree_type:
            degree_type = "MSc"
        elif "BA" in degree_type:
            degree_type = 'BA'
        elif "MNSW" in degree_type:
            degree_type = 'MNSW'
        elif "PGCert" in degree_type:
            degree_type = 'PGCert'
        elif "MBA" in degree_type:
            degree_type = 'MBA'
        elif "MA" in degree_type:
            degree_type = 'MA'
        elif "MComp" in degree_type:
            degree_type = 'MComp'
        elif "PhD" in degree_type:
            degree_type = 'PhD'
        elif "FdA" in degree_type:
            degree_type = 'FdA'
        elif "PGCE" in degree_type:
            degree_type = 'PGCE'
        elif "IFP" in degree_type:
            degree_type = 'IFP'
        elif "LLB" in degree_type:
            degree_type = 'LLB'
        elif "MHealth Res" in degree_type:
            degree_type = 'MHealth Res'
        elif "MRes" in degree_type:
            degree_type = 'MRes'
        elif "MMed" in degree_type:
            degree_type = 'MMed'
        elif "MSci" in degree_type:
            degree_type = 'MSci'
        elif "MCh" in degree_type:
            degree_type = 'MCh'
        elif "LLM" in degree_type:
            degree_type = "LLM"
        elif "Y2QF" in degree_type:
            degree_type = "Y2QF"
        elif "Y2QG" in degree_type:
            degree_type = "Y2QG"
        elif "HND" in degree_type:
            degree_type = 'HND'
        elif "LLB+BSc" in degree_type:
            degree_type = 'LLB+BSc'
        elif "(LLB)+(BSc)" in degree_type:
            degree_type = '(LLB)+(BSc)'
        elif "(BCrim)+(BA)" in degree_type:
            degree_type = '(BCrim)+(BA)'
        elif "BCrim+BCommun" in degree_type:
            degree_type = 'BCrim+BCommun'
        elif "BCrMedia" in degree_type:
            degree_type = 'BCrMedia'
        elif "BBus" in degree_type:
            degree_type = 'BBus'
        elif "(BEd)+(BA)" in degree_type:
            degree_type = '(BEd)+(BA)'
        elif "(BE(Hons))" in degree_type:
            degree_type = '(BE(Hons))'
        elif "BCrMedia" in degree_type:
            degree_type = 'BCrMedia'
        elif "(BEd)+(BSc)" in degree_type:
            degree_type = '(BEd)+(BSc)'
        elif "LLB/LLB(Hons)" in degree_type:
            degree_type = 'LLB/LLB(Hons)'
        elif "(BSc)+(BClinChiro)" in degree_type:
            degree_type = '(BSc)+(BClinChiro)'
        elif "(BCommun)" in degree_type:
            degree_type = '(BCommun)'
        elif "(BCrim)" in degree_type:
            degree_type = '(BCrim)'
        elif "BSc/BLabMed" in degree_type:
            degree_type = 'BSc/BLabMed'
        elif "BSportExSc" in degree_type:
            degree_type = 'BSportExSc'
        elif "BCommun+LLB" in degree_type:
            degree_type = 'BCommun+LLB'
        elif "MBiol" in degree_type:
            degree_type = 'MBiol'
        elif "BEng" in degree_type:
            degree_type = 'BEng'
        elif "MEng" in degree_type:
            degree_type = 'MEng'
        elif "BEng" in degree_type:
            degree_type = 'BEng'
        elif "BDS" in degree_type:
            degree_type = 'BDS'
        elif "MEarthSci" in degree_type:
            degree_type = 'MEarthSci'
        elif "MEnv" in degree_type:
            degree_type = 'MEnv'
        elif "MMath" in degree_type:
            degree_type = 'MMath'
        elif "MMathStat" in degree_type:
            degree_type = 'MMathStat'
        elif "MBBS" in degree_type:
            degree_type = 'MBBS'
        elif "BMus" in degree_type:
            degree_type = 'BMus'
        elif "MPharm" in degree_type:
            degree_type = 'MPharm'
        elif "MPhys" in degree_type:
            degree_type = 'MPhys'
        elif "(BBus)" in degree_type:
            degree_type = '(BBus)'
        elif "(BEd)+(BA)" in degree_type:
            degree_type = '(BEd)+(BA)'
        elif "(BCrMedia)" in degree_type:
            degree_type = '(BCrMedia)'
        elif "(BE(Hons))" in degree_type:
            degree_type = '(BE(Hons))'
        elif "(BA)" in degree_type:
            degree_type = '(BA)'
        elif "(BEd)+(BSc)" in degree_type:
            degree_type = '(BEd)+(BSc)'
        elif "(LLB/LLB(Hons))" in degree_type:
            degree_type = '(LLB/LLB(Hons))'
        elif "(BSc)" in degree_type:
            degree_type = '(BSc)'
        elif "(BSc)+(BClinChiro)" in degree_type:
            degree_type = '(BSc)+(BClinChiro)'
        elif "(BCommun)" in degree_type:
            degree_type = '(BCommun)'
        elif "(BCrMedia)" in degree_type:
            degree_type = '(BCrMedia)'
        elif "(BCrim)" in degree_type:
            degree_type = '(BCrim)'
        elif "Media [Combined] (BCrMedia)+(BCommun)" in degree_type:
            degree_type = 'Media [Combined] (BCrMedia)+(BCommun)'
        elif "(BEd)+(BA)" in degree_type:
            degree_type = '(BEd)+(BA)'
        elif "(BSc/BLabMed)" in degree_type:
            degree_type = '(BSc/BLabMed)'
        elif "(BSportExSc)+(BSc)" in degree_type:
            degree_type = '(BSportExSc)+(BSc)'
        elif "(LLB)+(BBus)" in degree_type:
            degree_type = '(LLB)+(BBus)'
        elif "(Combined)" in degree_type:
            degree_type = '(Combined)'
        elif "" in degree_type:
            degree_type = ''
        elif "" in degree_type:
            degree_type = ''
        elif "" in degree_type:
            degree_type = ''
        elif "" in degree_type:
            degree_type = ''
        elif "" in degree_type:
            degree_type = ''
        elif "" in degree_type:
            degree_type = ''
        elif "" in degree_type:
            degree_type = ''
        elif "" in degree_type:
            degree_type = ''
        elif "" in degree_type:
            degree_type = ''
        elif "" in degree_type:
            degree_type = ''
        elif "" in degree_type:
            degree_type = ''
        elif "" in degree_type:
            degree_type = ''
        elif "" in degree_type:
            degree_type = ''
        elif "" in degree_type:
            degree_type = ''
        elif "" in degree_type:
            degree_type = ''
        elif "" in degree_type:
            degree_type = ''
        elif "" in degree_type:
            degree_type = ''
        elif "" in degree_type:
            degree_type = ''
        elif "" in degree_type:
            degree_type = ''
        elif "" in degree_type:
            degree_type = ''
        elif "" in degree_type:
            degree_type = ''
        elif "" in degree_type:
            degree_type = ''
        elif "" in degree_type:
            degree_type = ''
        elif "" in degree_type:
            degree_type = ''
        elif "" in degree_type:
            degree_type = ''
        elif "" in degree_type:
            degree_type = ''
        elif "" in degree_type:
            degree_type = ''
        elif "" in degree_type:
            degree_type = ''
        elif len(degree_type) == 0:
            degree_type = 'NULL'
        else:
            degree_type = "NULL"
    except:
        degree_type = "报错!"
    return degree_type