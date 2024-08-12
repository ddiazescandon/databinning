#!/usr/bin/env bash

##############################################################################################################################################################
# This script is meant to be run COMEBin after obtaining the bam files.
# Author of pipeline: Haitao Han.
# For questions, bugs, and suggestions, contact me at htaohan@163.com
##############################################################################################################################################################
VERSION="1.0.0"

help_message () {
  echo ""
  echo "databinning version: $VERSION"
  echo "Usage: bash run_comebin.sh [options] -a contig_file -o output_dir -p bam_file_path"
	echo "Options:"
	echo ""
	echo "  -a STR          metagenomic assembly file"
	echo "  -o STR          output directory"
	echo "  -p STR          path to access to the bam files"
	echo "";}

while getopts a:o:p:m:b:t:s:h:x:y:z: OPT; do
 case ${OPT} in
  a) contig_file=$(realpath ${OPTARG})
    ;;
  o) output_dir=$(realpath ${OPTARG})
    ;;
  p) bam_file_path=$(realpath ${OPTARG})
    ;;
  b) bam_files=${OPTARG}
    ;;
  m) binner=${OPTARG}
    ;;
  t) threads=${OPTARG}
    ;;
  s) sam_files=${OPTARG}
    ;;
  h) depth_file=$(realpath ${OPTARG})
    ;;
  x) bin1_dir=$(realpath ${OPTARG})
    ;;
  y) bin2_dir=$(realpath ${OPTARG})
    ;;
  z) bin3_dir=$(realpath ${OPTARG})
    ;;
  \?)
    exit 1
 esac
done



case ${binner} in
    metabat2)
#        if [ -z "${contig_file}" ] || [ -z "${output_dir}" ]; then
#            echo "Error: For mode 'metabat', both -a <file> and -b <dir> are required."
#            help_message
#        fi
        echo "Executing MetaBat 2 with threads ${threads} contigfile ${contig_file} -bamfile ${bam_files}"
        mkdir -p ${output_dir}
        cd ${output_dir}
        jgi_summarize_bam_contig_depths --outputDepth depth.txt ${bam_files}
        mkdir bins_dir
        metabat2 -t ${threads} -i ${contig_file} -a depth.txt -o bins_dir/bin
        ;;
    comebin)
#        if [ -z "${contig_file}" ] || [ -z "${output_dir}" ]; then
#            echo "Error: For mode 'metabat', both -a <file> and -b <dir> are required."
#            help_message
#        fi
        echo "Executing COMEBin with threads ${threads} contigfile ${contig_file} -bamfile ${bam_files}"
        mkdir -p ${output_dir}
        cd ${output_dir}
        run_comebin.sh -t ${threads} -a ${contig_file} -o ${output_dir} -p ${bam_file_path}
        ;;
    metadecoder)
#        if [ -z "${contig_file}" ] || [ -z "${output_dir}" ]; then
#            echo "Error: For mode 'metabat', both -a <file> and -b <dir> are required."
#            help_message
#        fi
        echo "Executing COMEBin with threads ${threads} contigfile ${contig_file} -samfile ${sam_files}"
        mkdir -p ${output_dir}/bins
        cd ${output_dir}
        metadecoder coverage --threads ${threads} -s ${sam_files}  -o METADECODER_gsa.COVERAGE
        metadecoder seed --threads ${threads} -f ${contig_file} -o METADECODER_gsa.SEED
        metadecoder cluster -f ${contig_file} -c METADECODER_gsa.COVERAGE -s METADECODER_gsa.SEED -o bins/METADECODER
        ;;
    metabinner)
#        if [ -z "${contig_file}" ] || [ -z "${output_dir}" ]; then
#            echo "Error: For mode 'metabat', both -a <file> and -b <dir> are required."
#            help_message
#        fi
        echo "Executing COMEBin with threads ${threads} contigfile ${contig_file} -samfile ${sam_files}"
        mkdir -p ${output_dir}
        awk -F'\t' '{OFS="\t"; output=""; for(i=1; i<=NF; i++) if (i == 1 || (i >= 4 && (i-4) % 2 == 0)) { if (output != "") output = output OFS; output = output $i } print output}' ${depth_file} > ${output_dir}/coverage_profile.tsv
        cd $CONDA_PREFIX/bin/MetaBinner/scripts
        metabinner_path=$CONDA_PREFIX/bin/MetaBinner
        python gen_kmer.py ${contig_file} 1000 4 ${output_dir}/kmer.tsv

        ../run_metabinner.sh -t ${threads} -a ${contig_file} -o ${output_dir} -d ${output_dir}/coverage_profile.tsv -k ${output_dir}/kmer.tsv -p ${metabinner_path}
        ;;
    magscot)
#        if [ -z "${contig_file}" ] || [ -z "${output_dir}" ]; then
#            echo "Error: For mode 'metabat', both -a <file> and -b <dir> are required."
#            help_message
#        fi
        echo "Executing COMEBin with threads ${threads} contigfile ${contig_file} "
        MAGScoT_folder=${CONDA_PREFIX}/bin/MAGScoT

        cd ${output_dir}
        gzip -c ${contig_file} > example.contigs.fasta.gz
        mkdir -p tmp_workfolder
        zcat example.contigs.fasta.gz | parallel -j ${threads} --block 999k --recstart '>' --pipe prodigal -p meta -a tmp_workfolder/example.{\#}.faa -d tmp_workfolder/example.{\#}.ffn -o tmpfile
        cat tmp_workfolder/example.*.faa > example.prodigal.faa
        cat tmp_workfolder/example.*.ffn > example.prodigal.ffn
        rm -r tmp_workfolder tmpfile

        hmmsearch -o example.hmm.tigr.out --tblout example.hmm.tigr.hit.out --noali --notextw --cut_nc --cpu ${threads} $MAGScoT_folder/hmm/gtdbtk_rel207_tigrfam.hmm example.prodigal.faa
        hmmsearch -o example.hmm.pfam.out --tblout example.hmm.pfam.hit.out --noali --notextw --cut_nc --cpu ${threads} $MAGScoT_folder/hmm/gtdbtk_rel207_Pfam-A.hmm example.prodigal.faa

        cat example.hmm.tigr.hit.out | grep -v "^#" | awk '{print $1"\t"$3"\t"$5}' > example.tigr
        cat example.hmm.pfam.hit.out | grep -v "^#" | awk '{print $1"\t"$4"\t"$5}' > example.pfam
        cat example.pfam example.tigr > example.hmm

        Contigs_to_bin_tsv.py --path ${bin1_dir} -o ${bin1_dir}/contig_to_bins.tsv
        Contigs_to_bin_tsv.py --path ${bin2_dir} -o ${bin2_dir}/contig_to_bins.tsv
        Contigs_to_bin_tsv.py --path ${bin3_dir} -o ${bin3_dir}/contig_to_bins.tsv
        chmod -R 777 ${bin1_dir}/contig_to_bins.tsv
        chmod -R 777 ${bin2_dir}/contig_to_bins.tsv
        chmod -R 777 ${bin3_dir}/contig_to_bins.tsv

        awk '{print $2"\t"$1"\tBinner1"}'  ${bin1_dir}/contig_to_bins.tsv > example.contigs_to_bin.tsv
        awk '{print $2"\t"$1"\tBinner2"}'  ${bin2_dir}/contig_to_bins.tsv >> example.contigs_to_bin.tsv
        awk '{print $2"\t"$1"\tBinner3"}'  ${bin3_dir}/contig_to_bins.tsv >> example.contigs_to_bin.tsv

        Rscript $MAGScoT_folder/MAGScoT.R -i example.contigs_to_bin.tsv --hmm example.hmm

        mkdir resulted_bins
        MAGScot_extract_fasta_bins.py ${contig_file} MAGScoT.refined.contig_to_bin.out --output_path resulted_bins

        ;;
    *)
        echo "Error: Invalid binner '${binner}'."
        help_message
        ;;
esac