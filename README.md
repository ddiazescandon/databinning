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

mkdir ${file}_single_result
cd ${file}_single_result
run_MaxBin.pl -contig ${file}/single_assembly_out/final.contigs_1000.fa -abund_list ${file}_depth_list.txt -out ${file}_single_result/myout -thread 16
```
###
