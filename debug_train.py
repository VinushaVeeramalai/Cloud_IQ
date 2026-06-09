from config import DATA_DIR, CURRENT_WEEK_CSV, ENABLE_AI_AGENT
from src.reader import CSVReader
from src.detector import ResourceDetector
from src.llm_analyzer import LLMAnalyzer
from src.ai_agent import AIAnalyzerAgent
from pathlib import Path
import traceback

try:
    reader = CSVReader()
    detector = ResourceDetector()
    analyzer = LLMAnalyzer()
    resources = reader.load_resources(Path(DATA_DIR) / CURRENT_WEEK_CSV)
    findings = detector.generate_report_data(resources)
    print('findings', len(findings))
    print(AIAnalyzerAgent(ENABLE_AI_AGENT, analyzer).train(findings))
except Exception:
    traceback.print_exc()
