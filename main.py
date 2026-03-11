"""
AI Resume Screening System
===========================
Main entry point that loads a job description, parses PDF resumes,
computes similarity scores, and displays ranked candidates.
"""

import os
import sys
from resume_parser import load_all_resumes
from similarity_engine import compute_similarity


# ──────────────────────────── Configuration ────────────────────────────

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JOB_DESC_FILE = os.path.join(BASE_DIR, "job_description.txt")
RESUMES_FOLDER = os.path.join(BASE_DIR, "resumes")


# ──────────────────────────── Helpers ──────────────────────────────────

def load_job_description(filepath):
    """Read the job description from a text file."""
    if not os.path.isfile(filepath):
        print(f"[ERROR] Job description file not found: '{filepath}'")
        sys.exit(1)
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read().strip()


def display_results(results):
    """Print a formatted ranking table."""
    print("\n" + "=" * 55)
    print("        AI RESUME SCREENING - RESULTS")
    print("=" * 55)

    if not results:
        print("\n  No results to display.\n")
        return

    print(f"\n  {'Rank':<6} {'Resume File':<30} {'Match %':>8}")
    print("  " + "-" * 48)

    for rank, (filename, score) in enumerate(results, start=1):
        bar_len = int(score / 5)  # simple visual bar (max 20 chars)
        bar = "#" * bar_len
        print(f"  {rank:<6} {filename:<30} {score:>6.2f}%  {bar}")

    print("\n" + "=" * 55)

    # Highlight the top candidate
    top_name, top_score = results[0]
    print(f"\n  * Best Match: {top_name} ({top_score:.2f}%)")
    print()


# ──────────────────────────── Main ─────────────────────────────────────

def main():
    print("\n" + "=" * 55)
    print("     AI RESUME SCREENING SYSTEM")
    print("=" * 55)

    # Step 1: Load job description
    print(f"\n[1] Loading job description from '{os.path.basename(JOB_DESC_FILE)}' ...")
    job_description = load_job_description(JOB_DESC_FILE)
    print(f"    -> {len(job_description)} characters loaded.")

    # Step 2: Load and parse resumes
    print(f"\n[2] Loading resumes from '{os.path.basename(RESUMES_FOLDER)}/' folder ...")
    resumes = load_all_resumes(RESUMES_FOLDER)

    if not resumes:
        print("\n[ERROR] No resumes could be loaded. Exiting.")
        sys.exit(1)

    print(f"    -> {len(resumes)} resume(s) loaded successfully.")

    # Step 3: Compute similarity
    print("\n[3] Computing similarity scores ...")
    results = compute_similarity(job_description, resumes)

    # Step 4: Display ranked results
    display_results(results)


if __name__ == "__main__":
    main()
