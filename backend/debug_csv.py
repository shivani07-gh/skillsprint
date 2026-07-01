"""
Debug script to check CSV loading
Run: python debug_csv.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from app.utils.csv_loader import csv_loader

print("=" * 60)
print("🔍 Debugging CSV Loader")
print("=" * 60)

print(f"\n📁 Project root: {csv_loader.project_root}")
print(f"📁 Datasets path: {csv_loader.datasets_path}")
print(f"📁 Path exists: {csv_loader.datasets_path.exists()}")

if csv_loader.datasets_path.exists():
    print("\n📂 Files in datasets/raw:")
    for file in csv_loader.datasets_path.iterdir():
        print(f"  • {file.name}")
    
    print("\n🔄 Attempting to load CSV files...")
    datasets = csv_loader.load_all_datasets()
    
    print(f"\n✅ Loaded {len(datasets)} subjects:")
    for subject, data in datasets.items():
        print(f"  • {subject}: {len(data)} questions")
else:
    print("❌ Datasets path not found!")
    print(f"   Expected: {csv_loader.datasets_path}")
    
    # Try alternative paths
    alt_paths = [
        Path(__file__).parent.parent / 'datasets' / 'raw',
        Path(__file__).parent / 'datasets' / 'raw',
        Path.cwd() / 'datasets' / 'raw',
        Path.cwd().parent / 'datasets' / 'raw',
    ]
    print("\n🔍 Checking alternative paths:")
    for alt in alt_paths:
        exists = alt.exists()
        print(f"  {'✅' if exists else '❌'} {alt}")