from extractor import main as process_news
from analyzer import main as analyze_polarity

# Run the main function from the polarity analyzer
if __name__ == "__main__":
    process_news()
    analyze_polarity()
