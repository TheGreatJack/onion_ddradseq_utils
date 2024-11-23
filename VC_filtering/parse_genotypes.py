import argparse
import sys


def file_reader(file_path):

    genotype_dict = {}
    genotype_count = 0
    while True:
        line = file_path.readline()
        if not line:
            break
        line = line.strip().split("\t")

        genotypes = line[5:]
        traduced_genotypes = []

        for genotype in genotypes:
            if genotype in genotype_dict:
                traduced_genotypes.append(genotype_dict[genotype])
            else:
                genotype_dict[genotype] = genotype_count
                traduced_genotypes.append(genotype_count)
                genotype_count += 1


        to_print = line[0:5]
        to_print.extend(traduced_genotypes)
        print(*to_print,sep = "\t")




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read the output of the following command from Bcftools: 'bcftools query -f '\t%CHROM\t%POS\t%REF\t%ALT\tGT[\t%GT]\n' stacks_gg_run20_minAD3.DP6.vcf | sed 's+\./\.+\.+g' | python ../parse_genotypes.py > stacks_gg_run20_minAD3_DP6_parsed_genotypes.tsv'." + 
                                                " The idea is the get the per allele snp statistics. ")
    parser.add_argument("filename", nargs="?", type=argparse.FileType('r'),
                        help="File to read. If omitted, reads from standard input.")
    args = parser.parse_args()

    # Use standard input if no filename provided
    if args.filename is None:
        file = sys.stdin
    else:
        file = args.filename
#    line_procceser_eff(file)

    file_reader(file)

    # Close the file if it's not standard input
    if file != sys.stdin:
        file.close()