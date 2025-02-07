from graphviz import Digraph

# Initialize a directed graph
flowchart = Digraph("Startup Matchmaking Flowchart", format="png")
flowchart.attr(rankdir="TB", size="8")

# Define nodes
flowchart.node("A", "User Onboarding\n(Startups, Investors, Professionals)", shape="ellipse", style="filled", color="lightblue")
flowchart.node("B", "Profile Creation\n(Details: Vision, Skills, Preferences)", shape="box", style="rounded,filled", color="lightgray")
flowchart.node("C", "AI-Driven Matchmaking\n(Shared Goals & Interests)", shape="box", style="rounded,filled", color="lightgray")
flowchart.node("D", "Suggestions & Matches\n(Customized Recommendations)", shape="box", style="rounded,filled", color="lightgray")
flowchart.node("E", "Engagement\n(Swipe Up, Express Interest)", shape="box", style="rounded,filled", color="lightgray")
flowchart.node("F", "Direct Communication\n(Chat & Collaboration Tools)", shape="box", style="rounded,filled", color="lightgray")
flowchart.node("G", "Partnership\n(Successful Match or Feedback)", shape="ellipse", style="filled", color="lightblue")

# Define edges
flowchart.edges([
    ("A", "B"),
    ("B", "C"),
    ("C", "D"),
    ("D", "E"),
    ("E", "F"),
    ("F", "G")
])

# Save and render the flowchart
flowchart.render("startup_matchmaking_flowchart", view=True)