from graphviz import Digraph

# Create a Digraph object
flowchart = Digraph("Sentiment_Analysis_Flowchart", format="png")

# Set global graph attributes
flowchart.attr(rankdir='TB', splines='ortho', fontname='Arial', fontsize='12')

# Add nodes
flowchart.node("Start", "Start", shape="ellipse", style="bold", color="black")
flowchart.node("User", "User Submits Text for Analysis", shape="box", style="bold", color="black")
flowchart.node("Tool", "Sentiment Analysis Tool", shape="box", style="bold", color="black")
flowchart.node("Preprocessor", "Preprocessor:\n- Remove Stopwords\n- Tokenize\n- Stem Words", shape="box", style="bold", color="black")
flowchart.node("CleanedText", "Cleaned Text Sent to Sentiment Model", shape="box", style="bold", color="black")
flowchart.node("Model", "Sentiment Model:\n- Load Model\n- Predict Sentiment", shape="box", style="bold", color="black")
flowchart.node("Report", "Generate Sentiment Report:\n- Sentiment Score\n- Overall Sentiment", shape="box", style="bold", color="black")
flowchart.node("Database", "Database:\n- Store/Fetch/Update Report", shape="box", style="bold", color="black")
flowchart.node("Display", "Display Sentiment Report to User", shape="box", style="bold", color="black")
flowchart.node("End", "End", shape="ellipse", style="bold", color="black")

# Add edges
flowchart.edge("Start", "User")
flowchart.edge("User", "Tool")
flowchart.edge("Tool", "Preprocessor")
flowchart.edge("Preprocessor", "CleanedText")
flowchart.edge("CleanedText", "Model")
flowchart.edge("Model", "Report")
flowchart.edge("Report", "Database")
flowchart.edge("Database", "Display")
flowchart.edge("Display", "End")

# Render the flowchart and save the image
file_path = "sentiment_analysis_flowchart"
flowchart.render(file_path, cleanup=True)

file_path + ".png"
