# ==========================================================
# 🎀 SAKURA GENOMICS QUALITY CONTROL TOOL 🎀
# Author: Portfolio Project | Day 3 Stable (With Emoji Support!)
# ==========================================================

# --- SAFETY CHECK ---
try:
    with open("sequences.fasta", "r", encoding="utf-8") as test_file:
        pass
except FileNotFoundError:
    with open("sequences.fasta", "w", encoding="utf-8") as make_file:
        make_file.write(">hcv_virus_segment_1\natgctagcatgctagc\n>mutated_sample_2\nNNNNNNNNNNATGC\n>human_chromosome_extract\nGCGCGCGCATATAT\n")

# --- MAIN ENGINE ---
def run_sakura_qc_and_save(input_file, output_file):
    print(f"[!] Processing data from: {input_file}")
    
    # 🌟 FIX: We added encoding="utf-8" here so Windows can handle your cute emojis safely!
    with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
        
        outfile.write("=" * 45 + "\n")
        outfile.write("🌸 ✨ SAKURA GENOMICS QC REPORT ✨ 🌸\n")
        outfile.write("=" * 45 + "\n")
        
        for line in infile:
            cleaned_line = line.strip()
            
            if cleaned_line.startswith(">"):
                continue
            else:
                strand = cleaned_line
                clean_strand = strand.upper()
                length = len(clean_strand)
                n_count = clean_strand.count("N")
                n_percentage = (n_count / length) * 100
                
                if n_percentage > 20:
                    outfile.write("\n   🌧️ [Alert] High Error Base Count!\n")
                    outfile.write(f"   🧁 Strand : {clean_strand}\n")
                    outfile.write(f"   ⭐ Status : Flagged ({n_percentage:.1f}% N-bases)\n")
                    outfile.write("   " + "• " * 18 + "\n")
                else:
                    g_count = clean_strand.count("G")
                    c_count = clean_strand.count("C")
                    gc_percentage = ((g_count + c_count) / length) * 100
                    
                    outfile.write("\n   🌸 [Passed] Analysis Successful!\n")
                    outfile.write(f"   🧁 Strand : {clean_strand}\n")
                    outfile.write(f"   📏 Length : {length} base pairs\n")
                    outfile.write(f"   💖 GC %   : {gc_percentage:.1f}%\n")
                    outfile.write("   " + "• " * 18 + "\n")

        outfile.write("\n" + "=" * 45 + "\n")
        outfile.write("✨ ALL DONE! YOUR GENOMES ARE RADIANT! ✨\n")
        outfile.write("=" * 45 + "\n")
        
    print(f"[✔] Analysis Complete! Your beautiful report is saved as: {output_file}")

# Execute the tool
run_sakura_qc_and_save("sequences.fasta", "sakura_report.txt")
