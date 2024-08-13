# Databinning software
Databinng is a user-friendly metagenomic binning wrapper suite that comprises two efficient binners (MetaBAT 2, MetaDecoder), two high-performance binners (MetaBinner, COMEBin), and a fast bin-refinement tool MAGScoT.
## Installation 
```
conda install mamba
conda create -n databinning
conda activate databinning
mamba install -c conda-forge -c bioconda -c r -c pytorch -c nvidia r-base r-optparse r-dplyr r-readr r-funr hmmer prodigal parallel comebin metabat2 pytorch pytorch-cuda=11.8
pip3 install -U https://github.com/liu-congcong/MetaDecoder/releases/download/v1.0.19/metadecoder-1.0.19-py3-none-any.whl
git clone https://github.com/htaohan/databinning.git
cp -r databinning/databinning/* $CONDA_PREFIX/bin
chmod -R 777 $CONDA_PREFIX/bin
```
## Usage example
```
#run metabat2
databinning.sh -m metabat2 -t 16 -a assembly.fasta -b "*.sorted.bam" -o metabat_result
#run metadecoder
databinning.sh -m metadecoder -t 16 -a assembly.fasta -s "*.sam" -o metadecoder_result
#run MetaBinner
databinning.sh -m metabinner -t 16 -a assembly.fasta -f metabat_result/depth.txt -o metabinner_result
#run COMEBin
databinning.sh -m comebin -t 16 -a assembly.fasta -p bamfiles_path -o comebin_result
#run MAGScot for bin-refinement
databinning.sh -m magscot -t 16 -a assembly.fasta -x metabat_result/bins_dir -y bins_dir2 metadecoder_result/bins -z bins_dir3 comebin_result/comebin_res/comebin_res_bins -o refined_bins
```
# Binning-benchmark
## Assembly
* [Megahit](https://github.com/voutcn/megahit) (version 1.2.9) for short reads.
* [Flye](https://github.com/fenderglass/Flye) (version 2.9.2, --meta) for long reads.
* [metaSPAdes](https://github.com/CSB5/OPERA-MS) (version 0.9.0, --no-polishing) for hybrid data.
## Mapping
* [Bowtie2](https://github.com/BenLangmead/bowtie2) (version 2.5.1) for short reads.
* [minimap2](https://github.com/lh3/minimap2) (version 2.24-r1171, -x map-hifi) for long reads.
* [Samtools](https://github.com/samtools/samtools) (version 1.3.1) for sorting alignment files.
## Binning (co-assembly, single-sample, multi-sample)
### [MetaBAT 2](https://bitbucket.org/berkeleylab/metabat/src/master/) (version 2.15)
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
jgi_summarize_bam_contig_depths --outputDepth depth_${file}_marine.txt ${file}/${file}_single.sorted.bam
mkdir bins_dir
metabat2 -t 16 -i ${file}/single_assembly_out/final.contigs_1000.fa -a depth_${file}_marine.txt -o bins_dir/bin

############################## Multi-sample binning for each sample ##############################

mkdir ${file}_multi_result
cd ${file}_multi_result
jgi_summarize_bam_contig_depths --outputDepth depth_${file}_marine.txt ${file}/single_assembly_out/multi_map/*.sorted.bam
mkdir bins_dir
metabat2 -t 16 -i ${file}/single_assembly_out/final.contigs_1000.fa -a depth_${file}_marine.txt -o bins_dir/bin
```
### [MaxBin 2](https://sourceforge.net/projects/maxbin/) (version 2.27)
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
### [CONCOCT](https://github.com/BinPro/CONCOCT) (version 1.1.0)
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
### [VAMB](https://github.com/RasmussenLab/vamb) (version 3.0.9)
```
############################## Co-assembly binning ##############################
out_file=marine_result
fasta_file=marine_short_co_assembly/final.contigs_1000.fa
depth_file=metabat2.15/marine_result/depth_marine.txt
vamb --outdir ./${out_file} --fasta ${fasta_file} --jgi ${depth_file} --minfasta 200000 -m 2000

############################## Single-sample binning for each sample ##############################

out_file=${file}_single_result
fasta_file=${file}/single_assembly_out/final.contigs_1000.fa
depth_file=metabat2.15/${file}_single_result/depth_${file}_marine.txt
vamb --outdir ./${out_file} --fasta ${fasta_file} --jgi ${depth_file} --minfasta 200000 -m 2000

############################## Multi-sample binning for each sample ##############################

out_file=${file}_multi_result
fasta_file=${file}/single_assembly_out/final.contigs_1000.fa
depth_file=metabat2.15/${file}_multi_result/depth_${file}_marine.txt
vamb --outdir ./${out_file} --fasta ${fasta_file} --jgi ${depth_file} --minfasta 200000 -m 2000 
```
### [CLMB](https://github.com/zpf0117b/CLMB) (version 1.0.0)
```
############################## Co-assembly binning ##############################
out_file=marine_result
fasta_file=marine_short_co_assembly/final.contigs_1000.fa
depth_file=metabat2.15/marine_result/depth_marine.txt
vamb --contrastive --outdir ./${out_file} --fasta ${fasta_file} --jgi ${depth_file}  --minfasta 200000 -m 2000

############################## Single-sample binning for each sample ##############################

out_file=${file}_single_result
fasta_file=${file}/single_assembly_out/final.contigs_1000.fa
depth_file=metabat2.15/${file}_single_result/depth_${file}_marine.txt
vamb --contrastive --outdir ./${out_file} --fasta ${fasta_file} --jgi ${depth_file} --minfasta 200000 -m 2000

############################## Multi-sample binning for each sample ##############################

out_file=${file}_multi_result
fasta_file=${file}/single_assembly_out/final.contigs_1000.fa
depth_file=metabat2.15/${file}_multi_result/depth_${file}_marine.txt
vamb --contrastive --outdir ./${out_file} --fasta ${fasta_file} --jgi ${depth_file} --minfasta 200000 -m 2000 
```
### [MetaDecoder](https://github.com/liu-congcong/MetaDecoder) (version 1.0.16)
```
############################## Co-assembly binning ##############################
mkdir marine_result
cd marine_result
metadecoder coverage --threads 16 -s *_co_assembly.sam -o METADECODER_gsa.COVERAGE
metadecoder seed --threads 16 -f marine_short_co_assembly/final.contigs_1000.fa -o METADECODER_gsa.SEED
metadecoder cluster -f marine_short_co_assembly/final.contigs_1000.fa -c METADECODER_gsa.COVERAGE -s METADECODER_gsa.SEED -o METADECODER_marine

############################## Single-sample binning for each sample ##############################

mkdir ${file}_single_result
cd ${file}_single_result
metadecoder coverage --threads 16 -s ${file}/${file}_single.sam  -o METADECODER_gsa.COVERAGE
metadecoder seed --threads 16 -f ${file}/single_assembly_out/final.contigs_1000.fa -o METADECODER_gsa.SEED
metadecoder cluster -f ${file}/single_assembly_out/final.contigs_1000.fa -c METADECODER_gsa.COVERAGE -s METADECODER_gsa.SEED -o METADECODER_${file}_marine

############################## Multi-sample binning for each sample ##############################

mkdir ${file}_multi_result
cd ${file}_multi_result
metadecoder coverage --threads 16 -s ${file}/single_assembly_out/multi_map/*.sam  -o METADECODER_gsa.COVERAGE
metadecoder seed --threads 16 -f ${file}/single_assembly_out/final.contigs_1000.fa -o METADECODER_gsa.SEED
metadecoder cluster -f ${file}/single_assembly_out/final.contigs_1000.fa -c METADECODER_gsa.COVERAGE -s METADECODER_gsa.SEED -o METADECODER_${file}_marine
```
### [Binny](https://github.com/a-h-b/binny/) (version 2.2.15)
```
############################## Co-assembly binning ##############################
run_name_list=marine_result
yaml_list=config_marine.yaml
binny -l -n ${run_name_list[SLURM_ARRAY_TASK_ID]} -r -t 16 ${yaml_list}

############################## Single-sample binning for each sample ##############################

run_name_list=${file}_single_result
yaml_list=config_${file}_single.yaml
binny -l -n ${run_name_list[SLURM_ARRAY_TASK_ID]} -r -t 16 ${yaml_list}

############################## Multi-sample binning for each sample ##############################

run_name_list=${file}_multi_result
yaml_list=config_${file}_multi.yaml
binny -l -n ${run_name_list[SLURM_ARRAY_TASK_ID]} -r -t 16 ${yaml_list}
```
### [MetaBinner](https://github.com/ziyewang/MetaBinner) (version 1.4.4)
```
############################## Co-assembly binning ##############################
mkdir path/marine_result
cd xx/MetaBinner/scripts
metabinner_path=xx/MetaBinner
python gen_kmer.py marine_short_co_assembly/final.contigs_1000.fa 1000 4 path/marine_result/marine_kmer.tsv
contig_file=marine_short_co_assembly/final.contigs_1000.fa
output_dir=path/marine_result/output
coverage_profiles=path/marine_coverage_profile.tsv
kmer_profile=path/marine_result/marine_kmer.tsv
../run_metabinner.sh -t 16 -a ${contig_file} -o ${output_dir} -d ${coverage_profiles} -k ${kmer_profile} -p ${metabinner_path}

############################## Single-sample binning for each sample ##############################

mkdir path/${file}_single_result
cd xx/MetaBinner/scripts
metabinner_path=xx/MetaBinner
python gen_kmer.py ${file}/single_assembly_out/final.contigs_1000.fa 1000 4 path/${file}_single_result/${file}_marine_kmer.tsv
contig_file=${file}/single_assembly_out/final.contigs_1000.fa
output_dir=path/${file}_single_result/output
coverage_profiles=path/depth_files/${file}_depth_single.txt
kmer_profile=path/${file}_single_result/${file}_marine_kmer.tsv
../run_metabinner.sh -t 16 -a ${contig_file} -o ${output_dir} -d ${coverage_profiles} -k ${kmer_profile} -p ${metabinner_path}

############################## Multi-sample binning for each sample ##############################

mkdir path/${file}_multi_result
cd xx/MetaBinner/scripts
metabinner_path=xx/MetaBinner
python gen_kmer.py ${file}/single_assembly_out/final.contigs_1000.fa 1000 4 path/${file}_multi_result/${file}_marine_kmer.tsv
contig_file=${file}/single_assembly_out/final.contigs_1000.fa
output_dir=path/${file}_multi_result/output
coverage_profiles=path/depth_files/${file}_depth_multi.txt
kmer_profile=path/${file}_multi_result/${file}_marine_kmer.tsv
../run_metabinner.sh -t 16 -a ${contig_file} -o ${output_dir} -d ${coverage_profiles} -k ${kmer_profile} -p ${metabinner_path}
```
### [SemiBin 2](https://github.com/BigDataBiology/SemiBin) (version 1.5.1)
```
############################## Co-assembly binning ##############################
mkdir marine_result
cd marine_result
SemiBin2 single_easy_bin -t 16 -i marine_short_co_assembly/final.contigs_1000.fa -b *_co_assembly.sorted.bam -o marine_result/output --compression none

############################## Single-sample binning for each sample ##############################

mkdir ${file}_single_result
cd ${file}_single_result
SemiBin2 single_easy_bin -t 16 -i ${file}/single_assembly_out/final.contigs_1000.fa -b ${file}/${file}_single.sorted.bam -o marine_${file}/output --compression none

############################## Multi-sample binning for each sample ##############################

mkdir ${file}_multi_result
cd ${file}_multi_result
SemiBin2 single_easy_bin -t 16 -i ${file}/single_assembly_out/final.contigs_1000.fa -b ${file}/single_assembly_out/multi_map/*.sorted.bam -o marine_${file}/output --compression none
```
### [COMEBin](https://github.com/ziyewang/COMEBin) (version 1.0.3)
```
############################## Co-assembly binning ##############################
run_comebin.sh -t 16 -a marine_short_co_assembly/final.contigs_1000.fa -o path/Comebin_result -p path/Comebin_result/bam_files

############################## Single-sample binning for each sample ##############################

run_comebin.sh -t 16 -a ${file}/single_assembly_out/final.contigs_1000.fa -o path/Comebin_result/${file}_single_result -p path/Comebin_result/${file}_single_result/bam_files

############################## Multi-sample binning for each sample ##############################

run_comebin.sh -t 16 -a ${file}/single_assembly_out/final.contigs_1000.fa -o path/Comebin_result/${file}_multi_result -p path/Comebin_result/${file}_multi_result/bam_files
```
## Refinement
* [DAS Tool](https://github.com/cmks/DAS_Tool) (version 1.1.6).
* [MetaWRAP](https://github.com/bxlab/metaWRAP) (version 1.3.2).
* [MAGScoT](https://github.com/ikmb/MAGScoT) (version 1.0.0).
## Evaluation and annotation
* [CheckM 2](https://github.com/chklovski/CheckM2) (version 1.0.2) for assessing the completeness and contamination of metagenome-assembled genomes.
* [Aragorn](http://www.ansikte.se/ARAGORN/) (version 1.2.41) for identifing tRNAs.
* [Barrnap](https://github.com/tseemann/barrnap) (version 0.9) for predicting the location of 5S, 16S, and 23S rRNA genes.
* [dRep](https://github.com/MrOlm/drep) (version 3.4.3) for dereplicating.
* [RGI](https://github.com/arpcard/rgi) (version 6.0.2) for identifing ARGs.
* [antiSMASH](https://github.com/antismash/antismash) (version 6.1.1) for identifing BGCs.
