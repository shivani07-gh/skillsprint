import csv
import os
from typing import List, Dict, Any
from pathlib import Path

class CSVLoader:
    """Load and parse CSV files from datasets directory"""
    
    # Difficulty mapping
    DIFFICULTY_MAP = {
        'easy': 'Easy',
        'medium': 'Medium',
        'hard': 'Hard',
        'EASY': 'Easy',
        'MEDIUM': 'Medium',
        'HARD': 'Hard',
    }
    
    def __init__(self):
        self.backend_dir = Path(__file__).parent.parent.parent
        self.project_root = self.backend_dir.parent
        self.datasets_path = self.project_root / 'datasets' / 'raw'
        
        print(f"📁 Project root: {self.project_root}")
        print(f"📁 Datasets path: {self.datasets_path}")
    
    def load_csv(self, filename: str) -> List[Dict[str, Any]]:
        """Load a single CSV file and return list of dictionaries"""
        file_path = self.datasets_path / filename
        if not file_path.exists():
            print(f"⚠️ File not found: {file_path}")
            return []
        
        data = []
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    cleaned_row = self._clean_row(row)
                    data.append(cleaned_row)
            print(f"✅ Loaded {len(data)} rows from {filename}")
        except Exception as e:
            print(f"❌ Error loading {filename}: {e}")
        
        return data
    
    def load_all_datasets(self) -> Dict[str, List[Dict[str, Any]]]:
        """Load all CSV files from the datasets folder"""
        datasets = {}
        
        csv_files = ['arithmetic.csv', 'reasoning.csv', 'verbal.csv']
        subject_map = {
            'arithmetic': 'Arithmetic',
            'reasoning': 'Logical Reasoning',
            'verbal': 'Verbal Ability'
        }
        
        for filename in csv_files:
            data = self.load_csv(filename)
            if data:
                subject_key = filename.replace('.csv', '').lower()
                datasets[subject_map.get(subject_key, subject_key.capitalize())] = data
        
        return datasets
    
    def _clean_row(self, row: Dict[str, str]) -> Dict[str, Any]:
        """Clean and normalize a CSV row"""
        cleaned = {}
        for key, value in row.items():
            if value is None:
                cleaned[key] = ''
            else:
                cleaned[key] = value.strip()
        
        # Normalize options
        options = []
        for opt in ['option_a', 'option_b', 'option_c', 'option_d']:
            if opt in cleaned and cleaned[opt]:
                options.append(cleaned[opt])
            else:
                options.append('')
        
        while len(options) < 4:
            options.append('')
        
        cleaned['options'] = options
        
        # Convert correct_option to integer (0-3)
        if 'correct_option' in cleaned:
            try:
                val = str(cleaned['correct_option']).upper().strip()
                if val in ['A', 'B', 'C', 'D']:
                    cleaned['correct_option'] = ord(val) - 65
                else:
                    cleaned['correct_option'] = int(val)
            except (ValueError, TypeError):
                cleaned['correct_option'] = 0
        
        # Normalize difficulty
        if 'difficulty' in cleaned and cleaned['difficulty']:
            diff = cleaned['difficulty'].strip()
            # Try to match with our mapping
            if diff.lower() in ['easy', 'medium', 'hard']:
                cleaned['difficulty'] = self.DIFFICULTY_MAP.get(diff.lower(), 'Medium')
            else:
                cleaned['difficulty'] = 'Medium'
        else:
            cleaned['difficulty'] = 'Medium'
        
        # Ensure all required fields exist
        required_fields = ['question', 'topic', 'subtopic', 'explanation']
        for field in required_fields:
            if field not in cleaned:
                cleaned[field] = ''
        
        return cleaned
    
    def get_subject_metadata(self) -> Dict[str, Dict]:
        """Get metadata about each subject"""
        return {
            'Arithmetic': {
                'name': 'Arithmetic',
                'icon': 'fa-calculator',
                'description': 'Master quantitative aptitude with comprehensive topic coverage',
                'color': '#667eea'
            },
            'Logical Reasoning': {
                'name': 'Logical Reasoning',
                'icon': 'fa-brain',
                'description': 'Enhance your logical and analytical thinking abilities',
                'color': '#f45c43'
            },
            'Verbal Ability': {
                'name': 'Verbal Ability',
                'icon': 'fa-comment-dots',
                'description': 'Improve your language skills for placement exams',
                'color': '#764ba2'
            }
        }

# Singleton instance
csv_loader = CSVLoader()