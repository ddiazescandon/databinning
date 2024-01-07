# Binning-review
## Binning
### MetaBAT 2
```
############################## Co-assembly binning ##############################

mkdir marine_result
cd marine_result
jgi_summarize_bam_contig_depths --outputDepth depth_marine.txt *_co_assembly.sorted.bam
mkdir bins_dir
metabat2 -t 16 -i marine_co_assembly/final.contigs_1000.fa -a depth_marine.txt -o bins_dir/bin

############################## Single-sample binning for each sample ##############################

mkdir ${file}_single_result
cd ${file}_single_result
jgi_summarize_bam_contig_depths --outputDepth depth_${file}_marine.txt ${file}_single.sorted.bam
mkdir bins_dir
metabat2 -t 16 -i ${file}/single_assembly_out/final.contigs_1000.fa -a depth_${file}_marine.txt -o bins_dir/bin

############################## Multi-sample binning for each sample ##############################

mkdir ${file}_multi_result
cd ${file}_multi_result
jgi_summarize_bam_contig_depths --outputDepth depth_${file}_marine.txt multi_map/*.sorted.bam
mkdir bins_dir
metabat2 -t 16 -i ${file}/single_assembly_out/final.contigs_1000.fa -a depth_${file}_marine.txt -o bins_dir/bin
```
### MaxBin 2
```
############################## Co-assembly binning ##############################

mkdir marine_result
run_MaxBin.pl -contig marine_short_co_assembly/final.contigs_1000.fa -abund_list depth_list.txt -out marine_result/myout -thread 16

############################## Single-sample binning for each sample ##############################

mkdir ${file}_single_result
cd ${file}_single_result
run_MaxBin.pl -contig ${file}/single_assembly_out/final.contigs_1000.fa -abund ${file}_depth.txt -out ${file}_single_result/myout -thread 16

############################## Multi-sample binning for each sample ##############################

mkdir ${file}_multi_result
cd ${file}_multi_result
run_MaxBin.pl -contig ${file}/single_assembly_out/final.contigs_1000.fa -abund_list ${file}_depth_list.txt -out ${file}_single_result/myout -thread 16
```
### CONCOCT
```
############################## Co-assembly binning ##############################
mkdir marine_result
cd marine_result
cut_up_fasta.py marine_short_co_assembly/final.contigs_1000.fa -c 10000 -o 0 --merge_last -b contigs_10K.bed > contigs_10K.fa
concoct_coverage_table.py contigs_10K.bed *_co_assembly.sorted.bam > coverage_table.tsv
concoct -t 16 --composition_file contigs_10K.fa --coverage_file coverage_table.tsv -b concoct_output/
merge_cutup_clustering.py concoct_output/clustering_gt1000.csv > concoct_output/clustering_merged.csv
mkdir concoct_output/fasta_bins
extract_fasta_bins.py marine_short_co_assembly/final.contigs_1000.fa concoct_output/clustering_merged.csv --output_path concoct_output/fasta_bins

############################## Single-sample binning for each sample ##############################

mkdir ${file}_single_result
cd ${file}_single_result
cut_up_fasta.py ${file}/single_assembly_out/final.contigs_1000.fa -c 10000 -o 0 --merge_last -b contigs_10K.bed > contigs_10K.fa
concoct_coverage_table.py contigs_10K.bed ${file}/${file}_single.sorted.bam > coverage_table.tsv
concoct -t 16 --composition_file contigs_10K.fa --coverage_file coverage_table.tsv -b concoct_output/
merge_cutup_clustering.py concoct_output/clustering_gt1000.csv > concoct_output/clustering_merged.csv
mkdir concoct_output/fasta_bins
extract_fasta_bins.py ${file}/single_assembly_out/final.contigs_1000.fa concoct_output/clustering_merged.csv --output_path concoct_output/fasta_bins

############################## Multi-sample binning for each sample ##############################

mkdir ${file}_multi_result
cd ${file}_multi_result
cut_up_fasta.py ${file}/single_assembly_out/final.contigs_1000.fa -c 10000 -o 0 --merge_last -b contigs_10K.bed > contigs_10K.fa
concoct_coverage_table.py contigs_10K.bed ${file}/single_assembly_out/multi_map/*.sorted.bam > coverage_table.tsv
concoct -t 16 --composition_file contigs_10K.fa --coverage_file coverage_table.tsv -b concoct_output/
merge_cutup_clustering.py concoct_output/clustering_gt1000.csv > concoct_output/clustering_merged.csv
mkdir concoct_output/fasta_bins
extract_fasta_bins.py ${file}/single_assembly_out/final.contigs_1000.fa concoct_output/clustering_merged.csv --output_path concoct_output/fasta_bins
```
