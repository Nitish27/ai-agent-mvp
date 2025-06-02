from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import Tool
from datetime import datetime

def save_to_text(date: str, filename: str = "research_output.txt"):
    """
    Save content to a text file with the given date and filename.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\nDate: {date}\n\n"
    with open(filename, "a", encoding="utf-8") as file:
        file.write(formatted_text)
    return f"Content saved to {date}_{filename}.txt"

save_tool = Tool(
    name="save_text_to_file",
    func=save_to_text,
    description="Saves structured research output to a text file with a timestamp and date.",
)

search = DuckDuckGoSearchRun()

search_tool = Tool(
    name="search",
    func=search.run,
    description="Searches the web for information related to the query.",
)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)